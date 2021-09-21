from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from graphlib import TopologicalSorter
from io import StringIO
from pathlib import Path
from typing import Final, Mapping, Optional, Sequence, Set, TextIO, Tuple, cast

from docutils.core import publish_doctree
from docutils.frontend import Values
from docutils.io import FileInput
from docutils.nodes import Element, Inline, TextElement, document
from sphinx.environment import BuildEnvironment

from bpystubgen.parser import _known_types


def from_path(source: Path, settings: Values, env: BuildEnvironment) -> Optional[document]:
    return from_io(source.open("r"), str(source), settings, env)


def from_io(source: TextIO, source_path: str, settings: Values, env: BuildEnvironment) -> Optional[document]:
    env.project.docnames.add(source_path)
    env.prepare_settings(source_path)

    doctree = publish_doctree(
        source,
        source_class=FileInput,
        source_path=source_path,
        settings=settings)

    return doctree


class Referencing(ABC):

    @property
    def referred_types(self) -> Set[str]:
        return {"typing"}


class Typed(Element, Referencing, ABC):

    @property
    def type(self) -> Optional[str]:
        return self.attributes["type"] if self.hasattr("type") else None

    @type.setter
    def type(self, value: Optional[str]) -> None:
        if value:
            self.attributes["type"] = value
        elif "type" in self.attributes:
            del self.attributes["type"]

    @property
    def referred_types(self) -> Set[str]:
        references = super().referred_types

        rtype = self.type

        if rtype and rtype != "None":
            references.add(rtype)

        return references


class Named(Element, ABC):

    @property
    def name(self) -> Optional[str]:
        return self.attributes["name"] if self.hasattr("name") else None

    @name.setter
    def name(self, value: Optional[str]) -> None:
        if value:
            self.attributes["name"] = value
        elif "name" in self.attributes:
            del self.attributes["name"]

    @property
    def full_name(self) -> Optional[str]:
        name = self.name

        if not name:
            return None

        identifiers = [name]
        parent = self.parent

        while isinstance(parent, Named):
            name = parent.name

            if name:
                identifiers.append(name)
            else:
                return None

            parent = parent.parent

        identifiers.reverse()

        return ".".join(identifiers)


class Documentable(Element, ABC):

    @property
    def docstring(self) -> Optional[DocString]:
        try:
            docstring = next(filter(lambda c: isinstance(c, DocString), self.children))

            return cast(DocString, docstring)
        except StopIteration:
            return None


class Referencable(Named, ABC):

    @abstractmethod
    def create_ref(self) -> Optional[Reference]:
        pass


class APIMember(Documentable, Referencable, Typed, Element, ABC):

    @property
    @abstractmethod
    def signature(self) -> str:
        pass

    @property
    @abstractmethod
    def has_body(self) -> bool:
        pass

    @property
    def module(self) -> Optional[Module]:
        parent = self.parent

        while parent:
            if isinstance(parent, Module):
                return parent

            parent = parent.parent

        return None

    def localise_name(self, name: str) -> str:
        module = self.module

        return module.localise_name(name) if module else name


class APICollection(Element, ABC):

    @property
    def members(self) -> Sequence[APIMember]:
        return tuple(map(lambda m: cast(APIMember, m), filter(lambda c: isinstance(c, APIMember), self.children)))


class Module(Referencable, Referencing, Documentable, APICollection):
    tagname = "module"

    def create_ref(self, simple: bool = False) -> Optional[Reference]:
        name = self.name

        if not name:
            return None

        if simple:
            name = "~" + name

        return ModuleRef(text=name)

    @property
    def referred_types(self) -> Set[str]:
        references = super().referred_types

        for member in self.members:
            references = references.union(member.referred_types)

        return references

    @property
    def imports(self) -> Sequence[Import]:
        return tuple(self.traverse(Import, include_self=False, ascend=False))

    def import_types(self):
        types_to_imports = set()

        local_types = set(map(lambda c: c.name, filter(lambda m: isinstance(m, Class), self.members)))

        for tpe in self.referred_types:
            name = tpe.replace('"', "")

            if name.startswith("class:"):
                name = name.split(":")[1] \
                    .replace("`", "") \
                    .replace("!", "") \
                    .replace("~", "")

            if name[0].isupper() or \
                    name in _known_types or \
                    name in local_types or \
                    name.startswith(self.name):
                continue

            types_to_imports.add(name.split(".")[0])

        for i in self.imports:
            i.parent.remove(i)

        index = 1 if self.docstring else 0

        for tpe in sorted(types_to_imports):
            self.insert(index, Import(module=tpe))

    def localise_name(self, name: str) -> str:
        prefix = self.name + "."

        if name.startswith(prefix):
            return name[len(prefix):]

        # XXX: Hack to replace types in containers (e.g. typing.List[bge.types.KX_GameObject])
        if prefix in name and "typing" in name:
            for cls in filter(lambda m: isinstance(m, Class), self.members):
                name = name.replace(cls.full_name, cls.name)

        return name

    def sort_members(self) -> None:
        classes = tuple(filter(lambda m: isinstance(m, Class), self.members))

        if not any(classes):
            return

        local_types: Mapping[str, Class] = dict(map(lambda cl: (cl.name, cl), classes))

        def collect_deps(tpe: str, deps: Set[str], add_self: bool = True) -> Set[str]:
            if tpe in local_types:
                if add_self:
                    deps.add(tpe)

                for r in local_types[tpe].referred_types:
                    local_name = self.localise_name(r)
                    deps = deps.union(collect_deps(local_name, deps))

            return deps

        def create_entry(m: APIMember) -> Tuple[str, Set[str]]:
            cls = cast(Class, m)
            types = set(filter(lambda t: t in local_types and t != m.name, map(self.localise_name, cls.base_types)))
            return m.name, types

        graph = dict(map(create_entry, classes))
        ordered = TopologicalSorter(graph).static_order()

        pos = self.children.index(classes[0])

        for ch in classes:
            ch.parent.remove(ch)

        for name in ordered:
            self.insert(pos, local_types[name])
            pos += 1


class Data(APIMember):
    tagname = "data"

    @property
    def has_body(self) -> bool:
        return False

    @property
    def signature(self) -> str:
        name = self.name
        type_info = self.type

        if not name or not any(name):
            raise ValueError("Data node does not have a name.")

        type_info = self.localise_name(type_info) if type_info else "typing.Any"

        return f"{name}: {type_info} = ..."

    def create_ref(self, simple: bool = False) -> Optional[Reference]:
        name = self.full_name

        if not name:
            return None

        if simple:
            name = "~" + name

        return DataRef(text=name)


class Property(APIMember):
    tagname = "data"

    @property
    def has_body(self) -> bool:
        return True

    @property
    def signature(self) -> str:
        name = self.name
        type_info = self.type

        if not name or not any(name):
            raise ValueError("Property node does not have a name.")

        out = StringIO()

        out.write("@property\n")
        out.write("def ")
        out.write(name)
        out.write("(self) -> ")
        out.write(self.localise_name(type_info) if type_info else "typing.Any")
        out.write(":")

        return out.getvalue()

    def create_ref(self, simple: bool = False) -> Optional[Reference]:
        name = self.full_name

        if not name:
            return None

        if simple:
            name = "~" + name

        return PropertyRef(text=name)


class FunctionLike(APIMember, ABC):

    @property
    def arguments(self) -> Sequence[Argument]:
        # noinspection PyTypeChecker
        return tuple(filter(lambda c: isinstance(c, Argument), self.children))

    @property
    def has_body(self) -> bool:
        return True

    @property
    def referred_types(self) -> Set[str]:
        references = super().referred_types

        for arg in self.arguments:
            rtype = arg.type

            if rtype:
                references.add(rtype)

        return references


class Class(FunctionLike, APICollection):
    tagname = "class"

    @property
    def base_types(self) -> Sequence[str]:
        if not self.hasattr("base_types"):
            return ()

        value = str(self.attributes["base_types"]).split(",")

        return tuple(map(lambda v: v.strip(), value))

    @base_types.setter
    def base_types(self, value: Sequence[str]) -> None:
        if value and any(value):
            self.attributes["base_types"] = ", ".join(value)
        elif "base_types" in self.attributes:
            del self.attributes["base_types"]

    @property
    def referred_types(self) -> Set[str]:
        references = super().referred_types

        for member in self.members:
            references = references.union(member.referred_types)

        references = references.union(self.base_types)

        return references

    @property
    def signature(self) -> str:
        name = self.name

        if not name or not any(name):
            raise ValueError("Class node does not have a name.")

        base_types = self.base_types

        if any(base_types):
            parents = ", ".join(map(self.localise_name, base_types))

            return "".join(["class ", name, "(", parents, "):"])
        else:
            return "".join(["class ", name, ":"])

    def create_ref(self, simple: bool = False) -> Optional[Reference]:
        name = self.full_name

        if not name:
            return None

        if simple:
            name = "~" + name

        return ClassRef(text=name)


class FunctionScope(Enum):
    Module: Final = "module"
    Instance: Final = "instance"
    Class: Final = "class"
    Static: Final = "static"


class Function(FunctionLike):
    tagname = "function"

    @property
    def scope(self) -> FunctionScope:
        value = str.capitalize(self.attributes["scope"]) if self.hasattr("scope") else None

        return FunctionScope[value] if value in FunctionScope.__members__ else FunctionScope.Module

    @scope.setter
    def scope(self, value: FunctionScope) -> None:
        if value and value != FunctionScope.Module:
            self.attributes["scope"] = str.lower(value.name)
        elif "scope" in self.attributes:
            del self.attributes["scope"]

    @property
    def signature(self) -> str:
        scope = self.scope
        name = self.name
        type_info = self.type

        if not name or not any(name):
            raise ValueError("Function node does not have a name.")

        out = StringIO()

        if scope == FunctionScope.Class:
            out.write("@classmethod\n")
        elif scope == FunctionScope.Static:
            out.write("@staticmethod\n")

        out.write("def ")
        out.write(name)
        out.write("(")

        arg_text = []

        if scope == FunctionScope.Instance:
            arg_text.append("self")
        elif scope == FunctionScope.Class:
            arg_text.append("cls")

        args = self.arguments

        for arg in args:
            buffer = [arg.name]

            arg_type = arg.type

            buffer.append(": ")
            buffer.append(self.localise_name(arg_type) if arg_type else "typing.Any")

            default = arg.default

            if default:
                buffer.append(" = ")
                buffer.append(default)

            arg_text.append("".join(buffer))

        if any(arg_text):
            out.write(", ".join(arg_text))

        out.write(") -> ")
        out.write(self.localise_name(type_info) if type_info else "None")
        out.write(":")

        return out.getvalue()

    def create_ref(self, simple: bool = False) -> Optional[Reference]:
        name = self.full_name

        if not name:
            return None

        if simple:
            name = "~" + name

        return FunctionRef(text=name)


class DocString(TextElement):
    tagname = "docstring"


class Import(TextElement):
    tagname = "import"

    @property
    def module(self) -> Optional[str]:
        return self.attributes["module"] if self.hasattr("module") else None

    @module.setter
    def module(self, value: Optional[str]) -> None:
        if value:
            self.attributes["module"] = value
        elif "module" in self.attributes:
            del self.attributes["module"]

    @property
    def types(self) -> Sequence[str]:
        if not self.hasattr("types"):
            return ()

        value = str(self.attributes["types"]).split(",")

        return tuple(map(lambda v: v.strip(), value))

    @types.setter
    def types(self, value: Sequence[str]) -> None:
        if value and any(value):
            self.attributes["types"] = ", ".join(value)
        elif "types" in self.attributes:
            del self.attributes["types"]

    def astext(self) -> str:
        module = self.module
        types = self.types

        if any(types):
            return f"from {module} import {', '.join(types)}"
        else:
            return " ".join(("import", module))


class Argument(Typed, Named, Element):
    tagname = "argument"

    @property
    def default(self) -> Optional[str]:
        return self.attributes["default"] if self.hasattr("default") else None

    @default.setter
    def default(self, value: Optional[str]) -> None:
        if value:
            self.attributes["default"] = value
        elif "default" in self.attributes:
            del self.attributes["default"]


class Reference(Inline, TextElement):
    tagname = "ref"

    @property
    def target(self) -> str:
        name = super().astext()

        if name.startswith("~"):
            target = name[1:]

            return target
        elif name.startswith("!"):
            return name[1:]

        return name

    def astext(self) -> str:
        name = super().astext()
        ref_type = self.tagname[:-3]

        return "".join([":", ref_type, ":`", name, "`"])


class PythonRef(Reference, ABC):
    pass


class ClassRef(PythonRef):
    tagname = "classref"


class ModuleRef(PythonRef):
    tagname = "modref"


class FunctionRef(PythonRef):
    tagname = "funcref"


class DataRef(PythonRef):
    tagname = "dataref"


class PropertyRef(PythonRef):
    tagname = "propref"


class MethodRef(PythonRef):
    tagname = "methref"


class AttributeRef(PythonRef):
    tagname = "attrref"
