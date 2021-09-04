from typing import Type

from pytest import mark

from bpystubgen.nodes import Argument, Class, ClassRef, Data, DocString, Documentable, Function, Import, Module, \
    ModuleRef, Named, Property, Typed


@mark.parametrize("node_type", (Module, Data, Property, Function, Argument))
def test_named(node_type: Type[Named]):
    node = node_type()

    assert isinstance(node, Named)
    assert not node.name

    node.name = "name"
    assert node.name == "name"

    node.name = None
    assert not node.name


def test_full_name():
    mod = Module()
    data = Data()

    assert not data.full_name

    data.name = "mydata"

    assert data.full_name == "mydata"

    mod += data

    assert not data.full_name

    mod.name = "mymodule"

    assert data.full_name == "mymodule.mydata"


@mark.parametrize("node_type", (Data, Property, Function, Argument))
def test_typed(node_type: Type[Typed]):
    node = node_type()

    assert isinstance(node, Typed)
    assert not node.type

    node.type = "type"
    assert node.type == "type"

    node.type = None
    assert not node.type


@mark.parametrize("node_type", (Module, Data, Property, Function))
def test_docstring(node_type: Type[Documentable]):
    node = node_type()

    assert isinstance(node, Documentable)
    assert not node.docstring

    docstring = DocString("comment")

    node += docstring

    assert node.docstring == docstring


def test_module():
    module = Module(name="mymodule")

    func = Function("myfunc")
    cls = Class(name="MyClass")
    attr = Data(name="attr")

    assert not func.module
    assert not cls.module
    assert not attr.module

    cls += attr

    module += func
    module += cls

    assert func.module == module
    assert cls.module == module
    assert attr.module == module


def test_import():
    assert Import(module="bpy").astext() == "import bpy"
    assert Import(module="bpy.types", types="Camera").astext() == "from bpy.types import Camera"
    assert Import(module="bpy.types", types="Camera, Object").astext() == "from bpy.types import Camera, Object"
    assert Import(module="bpy.types", types="Camera,Object").astext() == "from bpy.types import Camera, Object"

    i = Import()
    i.module = "bpy.types"
    i.types = ("Camera", "Object")

    assert i.attributes["module"] == "bpy.types"
    assert i.attributes["types"] == "Camera, Object"

    assert i.astext() == "from bpy.types import Camera, Object"


def test_references():
    assert ModuleRef(text="bpy.types").target == "bpy.types"
    assert ModuleRef(text="~bpy.types").target == "bpy.types"
    assert ModuleRef(text="!bpy.types").target == "bpy.types"

    assert ModuleRef(text="bpy.types").astext() == ":mod:`bpy.types`"
    assert ModuleRef(text="~bpy.types").astext() == ":mod:`types <bpy.types>`"
    assert ModuleRef(text="!bpy.types").astext() == "bpy.types"

    assert ClassRef(text="bpy.types.Object").target == "bpy.types.Object"
    assert ClassRef(text="~bpy.types.Object").target == "bpy.types.Object"
    assert ClassRef(text="!bpy.types.Object").target == "bpy.types.Object"

    assert ClassRef(text="bpy.types.Object").astext() == ":class:`bpy.types.Object`"
    assert ClassRef(text="~bpy.types.Object").astext() == ":class:`Object <bpy.types.Object>`"
    assert ClassRef(text="!bpy.types.Object").astext() == "bpy.types.Object"
