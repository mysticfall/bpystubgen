import re
from abc import ABC
from dataclasses import dataclass
from typing import Any, Final, List, Mapping, Optional, OrderedDict, Sequence, cast

from docutils import nodes
from docutils.nodes import Element, Node, field_list, paragraph
from docutils.parsers.rst import Directive
from docutils.transforms import Transform

from bpystubgen.nodes import APIMember, Argument, Class, Data, DocString, Function, FunctionScope, \
    Module
from bpystubgen.parser import parse_type

_func_sig_pattern: Final = re.compile("^\\s*(\\w+)\\((.*)\\)\\s*$")

_func_arg_pattern: Final = re.compile("(\\w+)((?:\\s*=\\s*(.+))?)+")


class ModuleTransform(Transform):
    default_priority = 1

    def apply(self, **kwargs: Any) -> None:
        siblings = tuple(self.startnode.traverse(include_self=False, siblings=True, ascend=True))

        if not any(siblings):
            return

        module = siblings[0]

        def is_class_member(m: APIMember) -> bool:
            p = m.parent
            while p:
                if isinstance(p, Class):
                    return True
                p = p.parent

            return False

        if isinstance(module, Module):
            members = filter(lambda s: isinstance(s, APIMember) and not is_class_member(s), siblings)

            module.parent.remove(module)

            for member in tuple(members):
                ref = member.create_ref()

                if ref:
                    para = paragraph()
                    para += member.create_ref()

                    member.replace_self(para)
                else:
                    member.parent.remove(member)

                module += member

            self.startnode.parent.remove(self.startnode)

            if any(self.document.children):
                docstring = DocString()

                for child in tuple(self.document.children):
                    child.parent.remove(child)
                    docstring += child

                module.insert(0, docstring)

            self.document += module
        else:
            reporter = self.document.reporter
            msg = reporter.error("Missing module element.", base_node=self.document)

            assert isinstance(self.startnode, Element)

            self.startnode.replace_self(msg)


class ModuleDirective(Directive):
    has_content = True

    required_arguments = 1

    def run(self) -> List[Node]:
        name = self.arguments[0]

        elem = Module(name=name)

        # noinspection PyTypeChecker
        pending = nodes.pending(ModuleTransform)
        pending.details.update(self.options)

        document = self.state_machine.document
        document.note_pending(pending)

        return [pending, elem]


@dataclass
class DocStringInfo:
    docstring: DocString

    fields: Mapping[str, str]

    fields_list: Optional[field_list]

    remainder: Sequence[APIMember]


class APIMemberDirective(Directive, ABC):

    def parse_docstring(self) -> DocStringInfo:
        docstring = DocString()
        members = []

        self.state.nested_parse(self.content, self.content_offset, docstring)

        for member in tuple(filter(lambda c: isinstance(c, APIMember), docstring.children)):
            members.append(cast(APIMember, member))
            docstring.remove(member)

        fields = dict()
        fields_elem: Optional[field_list] = None

        if any(docstring.children):
            last = docstring.children[-1]

            if isinstance(last, field_list):
                fields_elem = last

                for field in fields_elem.children:
                    (f_name, f_body) = cast(Element, field).children

                    fields[f_name.astext().strip()] = f_body.astext().strip()

                docstring.remove(fields_elem)

        return DocStringInfo(docstring, fields, fields_elem, members)


class DataDirective(APIMemberDirective):
    has_content = True

    required_arguments = 1

    def run(self) -> List[Node]:
        ds = self.parse_docstring()

        elem = Data(name=self.arguments[0].strip())

        if any(ds.docstring.children):
            elem.insert(0, ds.docstring)

        if "type" in ds.fields:
            elem.type = parse_type(ds.fields["type"], "typing.Any")
        else:
            elem.type = "typing.Any"

        return [elem]


class FunctionDirective(APIMemberDirective):
    has_content = True

    required_arguments = 1

    final_argument_whitespace = True

    @classmethod
    def parse_args(cls, text: str, fields: Mapping[str, str]) -> OrderedDict[str, Argument]:
        args = OrderedDict[str, Argument]()
        match = _func_arg_pattern.search(text)

        while match:
            name = match.group(1)

            if name != "self":
                arg = Argument(name=name)
                key = f"type {arg.name}"

                if key in fields:
                    arg.type = parse_type(fields[key], "typing.Any")

                default = match.group(3)

                if default:
                    arg.default = default

                args[name] = arg

            match = _func_arg_pattern.search(text, pos=match.end() + 1)

        return args

    def run(self) -> List[Node]:
        document = self.state_machine.document
        reporter = document.reporter

        signature = self.arguments[0]
        result = _func_sig_pattern.match(signature)

        if not result:
            msg = reporter.error(f"Invalid function signature: {signature}", base_node=document)

            return [msg]

        name = result.group(1)

        elem = Function(name=name)

        if self.name == "classmethod":
            elem.scope = FunctionScope.Class
        elif self.name == "method":
            elem.scope = FunctionScope.Instance
        else:
            elem.scope = FunctionScope.Module

        ds = self.parse_docstring()

        if "rtype" in ds.fields:
            elem.type = parse_type(ds.fields["rtype"], "typing.Any")

        if "return" in ds.fields:
            elem.returns = ds.fields["return"]

        if any(ds.docstring.children):
            elem.insert(0, ds.docstring)

        args = self.parse_args(result.group(2), ds.fields)

        for arg in args.values():
            elem += arg

        return [elem]


class ClassDirective(APIMemberDirective):
    has_content = True

    required_arguments = 1

    final_argument_whitespace = True

    def run(self) -> List[Node]:
        signature = self.arguments[0]
        result = _func_sig_pattern.match(signature)

        ds = self.parse_docstring()

        if result:
            name = result.group(1)
            elem = Class(name=name)

            args = FunctionDirective.parse_args(result.group(2), ds.fields)

            ctor = Function(name="__init__", type="None")

            ctor.scope = FunctionScope.Instance

            if ds.fields_list:
                docstring = DocString()
                docstring += ds.fields_list

                ctor += docstring

            for arg in args.values():
                ctor += arg

            elem.insert(0, ctor)

            if any(ds.docstring.children):
                elem.insert(0, ds.docstring)
        else:
            name = signature.strip()
            elem = Class(name=name)

            if any(ds.docstring.children):
                elem.insert(0, ds.docstring)

        for member in ds.remainder:
            elem += member

        return [elem]


class CurrentModuleDirective(Directive):
    has_content = True

    required_arguments = 1

    def run(self) -> List[Node]:
        return []
