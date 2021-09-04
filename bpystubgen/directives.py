import ast
import re
from abc import ABC, abstractmethod
from ast import AST, FunctionDef, arguments
from dataclasses import dataclass
from itertools import chain
from typing import Any, List, Mapping, Optional, OrderedDict, Sequence, cast

from docutils import nodes
from docutils.nodes import Element, Node, field_list, paragraph
from docutils.parsers.rst import Directive
from docutils.transforms import Transform

from bpystubgen.nodes import APIMember, Argument, Class, ClassRef, Data, DocString, Function, FunctionScope, \
    Module, Property
from bpystubgen.parser import parse_type


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
            try:
                fields_elem = next(iter(docstring.traverse(field_list, ascend=False)))

                for field in fields_elem.children:
                    (f_name, f_body) = cast(Element, field).children

                    fields[f_name.astext().strip()] = f_body.astext().strip()

                docstring.remove(fields_elem)
            except StopIteration:
                pass

        return DocStringInfo(docstring, fields, fields_elem, members)


class DataLikeDirective(APIMemberDirective, ABC):
    has_content = True

    required_arguments = 1

    @abstractmethod
    def create_elem(self, name: str) -> APIMember:
        pass

    def run(self) -> List[Node]:
        ds = self.parse_docstring()

        elem = self.create_elem(self.arguments[0].strip())
        elems = [elem]

        if any(ds.docstring.children):
            elem.insert(0, ds.docstring)

        if "type" in ds.fields:
            type_info = parse_type(ds.fields["type"])

            if type_info:
                elem.type = type_info
            else:
                elem.type = "typing.Any"

                document = self.state_machine.document
                reporter = document.reporter

                msg = reporter.warning(
                    f"Data {elem.name} has invalid type: {ds.fields['type']}", base_node=self.state.parent)

                elems.append(msg)
        else:
            elem.type = "typing.Any"

        return elems


class DataDirective(DataLikeDirective):

    def create_elem(self, name: str) -> APIMember:
        return Data(name=name)


class PropertyDirective(DataLikeDirective):

    def create_elem(self, name: str) -> APIMember:
        return Property(name=name)


class FunctionLikeDirective(APIMemberDirective, ABC):
    has_content = True

    required_arguments = 1

    final_argument_whitespace = True

    _optional_func_pattern = re.compile("^(\\w+)\\s*\\(\\s*\\[?([\\w\\s,]*)(\\[[^)]+])]?\\)$")

    @classmethod
    def parse_func(cls, line: str) -> FunctionDef:
        line = str(line).strip()

        match = cls._optional_func_pattern.match(line)

        if match:
            required = map(str, filter(any, map(lambda s: s.strip(), match.group(2).split(","))))
            optional = map(
                lambda a: a + "=None",
                filter(any, map(lambda a: a.strip(), match.group(3).replace("[", "").replace("]", "").split(","))))

            args = chain(required, optional)
            line = "".join([match.group(1), "(", ", ".join(args), ")"])

        source = "".join(["def ", line, "\n" if line.endswith(":") else ":\n", "   ...\n"])

        tree = ast.parse(source)

        return cast(FunctionDef, tree.body[0])

    def parse_args(self, args: arguments, fields: Mapping[str, str]) -> (OrderedDict[str, Argument], Sequence[Node]):
        elems = OrderedDict[str, Argument]()
        messages = []

        count = len(args.args)
        offset = count - len(args.defaults)

        for i in range(count):
            arg = args.args[i]
            default: Optional[AST] = args.defaults[i - offset] if i >= offset else None

            if arg.arg == "self":
                continue

            elem = Argument(name=arg.arg)

            key = f"type {elem.name}"

            if key in fields:
                type_info = parse_type(fields[key])

                if type_info:
                    elem.type = type_info
                else:
                    elem.type = "typing.Any"

                    document = self.state_machine.document
                    reporter = document.reporter

                    msg = reporter.warning(f"Invalid argument type: {fields[key]}", base_node=self.state.parent)
                    messages.append(msg)

            if default:
                elem.default = ast.unparse(default)

            elems[elem.name] = elem

        return elems, messages


class FunctionDirective(FunctionLikeDirective):

    def run(self) -> List[Node]:
        document = self.state_machine.document
        reporter = document.reporter

        ds = self.parse_docstring()

        elems = []

        for line in filter(any, self.arguments[0].replace("\\\n", " ").split("\n")):
            try:
                func = self.parse_func(str(line))

                elem = Function(name=func.name)

                if self.name == "classmethod":
                    elem.scope = FunctionScope.Class
                elif self.name == "staticmethod":
                    elem.scope = FunctionScope.Static
                elif self.name == "method":
                    elem.scope = FunctionScope.Instance
                else:
                    elem.scope = FunctionScope.Module

                if "rtype" in ds.fields:
                    type_info = parse_type(ds.fields["rtype"])

                    if type_info:
                        elem.type = type_info
                    else:
                        elem.type = "typing.Any"

                        msg = reporter.warning(
                            f"Function {func.name} has invalid return type: {ds.fields['rtype']}",
                            base_node=self.state.parent)

                        elems.append(msg)

                if "return" in ds.fields:
                    elem.returns = ds.fields["return"]

                if any(ds.docstring.children):
                    elem.insert(0, ds.docstring)

                (args, messages) = self.parse_args(func.args, ds.fields)

                for arg in args.values():
                    elem += arg

                elems.append(elem)
                elems.extend(messages)
            except SyntaxError:
                msg = reporter.error(f"Invalid function signature: {line}", base_node=self.state.parent)
                elems.append(msg)

        return elems


class ClassDirective(FunctionLikeDirective):

    def run(self) -> List[Node]:
        signature = self.arguments[0].strip()

        ds = self.parse_docstring()

        elem: Optional[Class] = None
        elems = []

        if "(" in signature:
            parent = cast(Element, self.state.parent)

            try:
                func = self.parse_func(signature)

                name = func.name
                elem = Class(name=name)

                if any(parent.children):
                    last_sibling = parent.children[-1]

                    if last_sibling and last_sibling.astext().startswith("base class"):
                        base_types = set(map(lambda t: t.target, last_sibling.traverse(ClassRef, descend=True)))
                        elem.base_types = base_types

                (args, messages) = self.parse_args(func.args, ds.fields)

                elems.extend(messages)

                # Ignore when base classes are used instead of constructor arguments.
                if any(ds.fields):
                    ctor = Function(name="__init__", type="None")

                    ctor.scope = FunctionScope.Instance

                    if ds.fields_list:
                        docstring = DocString()
                        docstring += ds.fields_list

                        ctor += docstring

                    for arg in args.values():
                        ctor += arg

                    elem.insert(0, ctor)
                elif any(args) and not any(elem.base_types):
                    elem.base_types = set(args)

                if any(ds.docstring.children):
                    elem.insert(0, ds.docstring)
            except SyntaxError:
                document = self.state_machine.document
                reporter = document.reporter

                msg = reporter.error(f"Invalid class signature: {signature}", base_node=parent)

                elems.append(msg)
        else:
            name = signature.strip()
            elem = Class(name=name)

            if any(ds.docstring.children):
                elem.insert(0, ds.docstring)

        if elem:
            elems.append(elem)

            for member in ds.remainder:
                elem += member

        return elems


class CurrentModuleDirective(Directive):
    has_content = True

    required_arguments = 1

    def run(self) -> List[Node]:
        return []
