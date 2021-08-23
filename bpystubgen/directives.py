import re
from abc import ABC
from typing import Any, Dict, Final, List, Optional

from docutils import nodes
from docutils.nodes import Element, Node, paragraph
from docutils.parsers.rst import Directive
from docutils.statemachine import StringList
from docutils.transforms import Transform

from bpystubgen.nodes import APIMember, Argument, Class, Data, DocString, Documentable, Function, FunctionScope, \
    Import, Module, Typed
from bpystubgen.parser import known_data_types, parse_type

_option_pattern: Final = re.compile("^\\s*:([a-zA-Z0-9_]+)(\\s+([a-zA-Z0-9_]+))?:\\s+([^$]+)\\s*$")

_func_sig_pattern: Final = re.compile("^\\s*([a-zA-Z0-9_]+)\\(([^)]*)\\)\\s*$")

_func_arg_pattern: Final = re.compile(
    "^\\s*([a-zA-Z0-9_]+)(\\s*:\\s*([a-zA-Z0-9_:`~]+))?(\\s*=\\s*([a-zA-Z0-9_(),.:`~]+))?\\s*$")


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

            referred_types = filter(lambda t: t not in known_data_types, module.referred_types)
            types_to_import = set(map(lambda t: t.split(".")[0], referred_types))
            imports = map(lambda t: Import(text=t), types_to_import)

            for i in imports:
                module.insert(0, i)

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


class APIMemberDirective(Directive, ABC):

    # noinspection PyMethodMayBeStatic
    def set_type(self, elem: Typed, type_info: Optional[str]) -> None:
        elem.type = type_info if type_info and any(type_info) else "typing.Any"

    def parse_docstring(self, elem: Documentable, content: StringList) -> None:
        self.state.nested_parse(content, self.content_offset, elem)

        if any(elem.children):
            docstring = DocString()

            for child in tuple(filter(lambda c: not isinstance(c, APIMember), elem.children)):
                elem.remove(child)
                docstring += child

            elem.insert(0, docstring)


class DataDirective(APIMemberDirective):
    has_content = True

    required_arguments = 1

    def run(self) -> List[Node]:
        elem = Data(name=self.arguments[0].strip())

        comments = []

        for line in self.content.data:
            result = _option_pattern.match(line)

            if result:
                if result.group(1) == "type":
                    type_info = parse_type(result.group(4))
                    self.set_type(elem, type_info)
            else:
                comments.append(line.strip())

        self.parse_docstring(elem, StringList(comments))

        if not elem.type:
            elem.type = "typing.Any"

        return [elem]


class FunctionDirective(APIMemberDirective):
    has_content = True

    required_arguments = 1

    final_argument_whitespace = True

    def run(self) -> List[Node]:
        # noinspection DuplicatedCode
        document = self.state_machine.document
        reporter = document.reporter

        signature = self.arguments[0]
        result = _func_sig_pattern.match(signature)

        if not result:
            msg = reporter.error(f"Invalid function signature: {signature}", base_node=document)

            return [msg]

        name = result.group(1)

        args_texts = result.group(2).split(",")
        args: Dict[str, Argument] = {}

        elem = Function(name=name)
        comments = []

        if self.name == "classmethod":
            elem.scope = FunctionScope.Class
        elif self.name == "method":
            elem.scope = FunctionScope.Instance
        else:
            elem.scope = FunctionScope.Module

        arg_matches = filter(lambda a: a, map(_func_arg_pattern.match, args_texts))

        for match in arg_matches:
            name = match.group(1)
            arg = Argument(name=name)

            args[name] = arg

        for line in self.content.data:
            result = _option_pattern.match(line)
            option = result.group(1) if result else None

            if not option:
                comments.append(line.strip())
            elif option == "rtype":
                type_info = parse_type(result.group(4))

                self.set_type(elem, type_info)
            elif option == "return":
                elem.returns = result.group(4)
            elif option == "arg":
                name = result.group(3)

                if name in args:
                    arg = args[name]

                    self.parse_docstring(arg, StringList(result.group(4).split("\n")))
            elif option == "type":
                name = result.group(3)

                if name in args:
                    arg = args[name]
                    arg.type = parse_type(result.group(4))

        self.parse_docstring(elem, self.content)

        for arg in args.values():
            elem += arg

        return [elem]


class ClassDirective(APIMemberDirective):
    has_content = True

    required_arguments = 1

    final_argument_whitespace = True

    def run(self) -> List[Node]:
        # noinspection DuplicatedCode
        document = self.state_machine.document
        reporter = document.reporter

        signature = self.arguments[0]
        result = _func_sig_pattern.match(signature)

        if not result:
            msg = reporter.error(f"Invalid class signature: {signature}", base_node=document)

            return [msg]

        name = result.group(1)
        elem = Class(name=name)

        self.parse_docstring(elem, self.content)

        return [elem]
