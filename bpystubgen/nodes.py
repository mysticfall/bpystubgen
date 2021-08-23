from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from io import StringIO
from typing import Final, Optional, Sequence, Set, cast

from docutils.nodes import Element, Inline, TextElement


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

    @property
    @abstractmethod
    def has_body(self) -> bool:
        pass


class APICollection(Element, ABC):

    @property
    def members(self) -> Sequence[APIMember]:
        return tuple(self.traverse(APIMember, include_self=False, ascend=False))


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

        return f"{name}: {type_info if type_info else 'typing.Any'} = ..."

    def create_ref(self, simple: bool = False) -> Optional[Reference]:
        name = self.full_name

        if not name:
            return None

        if simple:
            name = "~" + name

        return DataRef(text=name)


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
    def signature(self) -> str:
        name = self.name

        if not name or not any(name):
            raise ValueError("Class node does not have a name.")

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
            arg_text.append(f"{arg.name}: {arg.type if arg.type else 'typing.Any'}")

        if any(arg_text):
            out.write(", ".join(arg_text))

        out.write(") -> ")
        out.write(type_info if type_info else "None")
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


class Argument(Typed, Named, Element):
    tagname = "argument"


class Reference(Inline, TextElement, ABC):

    def astext(self) -> str:
        name = super().astext()
        ref_type = self.tagname[:-3]

        if name.startswith("~"):
            title = name.split(".")[-1]
            target = name[1:]

            return "".join([":", ref_type, ":`", title, " <", target, ">`"])
        elif not name.startswith("!"):
            return "".join([":", ref_type, ":`", name, "`"])

        return name


class ClassRef(Reference):
    tagname = "classref"


class ModuleRef(Reference):
    tagname = "modref"


class FunctionRef(Reference):
    tagname = "funcref"


class DataRef(Reference):
    tagname = "dataref"


class MethodRef(Reference):
    tagname = "methref"


class AttributeRef(Reference):
    tagname = "attrref"
