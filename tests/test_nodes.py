import shutil
import tempfile
from pathlib import Path
from typing import Type

from docutils.frontend import OptionParser, Values
from docutils.parsers import Parser
from pytest import fixture, mark
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment

from bpystubgen import nodes
from bpystubgen.nodes import Argument, Class, ClassRef, Data, DocString, Documentable, Function, Import, Module, \
    ModuleRef, Named, Property, Typed


# noinspection DuplicatedCode
@fixture
def env() -> BuildEnvironment:
    dest_path = Path(tempfile.tempdir) / "bpystubgen-test"
    app = Sphinx(srcdir=".", confdir=None, outdir=str(dest_path), doctreedir=".", buildername="text")

    yield app.env

    shutil.rmtree(dest_path)


@fixture
def settings(env: BuildEnvironment) -> Values:
    components = (Parser,)
    settings = OptionParser(components=components).get_default_values()

    settings.line_length_limit = 15000
    settings.report_level = 5
    settings.traceback = True
    settings.env = env
    settings.pep_references = None
    settings.rfc_references = None

    return settings


@fixture
def rst_path() -> Path:
    return Path(__file__).parent / "fixtures" / "rst"


# noinspection DuplicatedCode
def test_from_path(rst_path: Path, settings: Values, env: BuildEnvironment):
    source = rst_path / "bge.types.KX_GameObject.rst"

    doc = nodes.from_path(source, settings, env)

    assert doc

    cls = next(iter(doc.traverse(Class)))

    assert cls.name == "KX_GameObject"
    assert cls.docstring
    assert cls.docstring.astext().startswith("All game objects")

    members = dict(map(lambda m: (m.name, m), cls.members))

    assert len(members) == 106
    assert isinstance(members["name"], Data)
    assert isinstance(members["applyForce"], Function)


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


def test_members():
    bge = Module(name="bge")
    types = Module(name="types")
    game_obj = Class(name="KX_GameObject")
    scene = Class(name="KX_Scene")

    bge += types
    types += game_obj
    types += scene

    name = Data(name="name")
    apply_force = Function(name="applyForce")

    game_obj += name
    game_obj += apply_force

    add_object = Function(name="addObject")

    scene += add_object

    assert not any(bge.members)
    assert set(types.members) == {game_obj, scene}
    assert set(game_obj.members) == {name, apply_force}
    assert set(scene.members) == {add_object}


def test_references():
    assert ModuleRef(text="bpy.types").target == "bpy.types"
    assert ModuleRef(text="~bpy.types").target == "bpy.types"
    assert ModuleRef(text="!bpy.types").target == "bpy.types"

    assert ModuleRef(text="bpy.types").astext() == ":mod:`bpy.types`"
    assert ModuleRef(text="~bpy.types").astext() == ":mod:`~bpy.types`"
    assert ModuleRef(text="!bpy.types").astext() == ":mod:`!bpy.types`"

    assert ClassRef(text="bpy.types.Object").target == "bpy.types.Object"
    assert ClassRef(text="~bpy.types.Object").target == "bpy.types.Object"
    assert ClassRef(text="!bpy.types.Object").target == "bpy.types.Object"

    assert ClassRef(text="bpy.types.Object").astext() == ":class:`bpy.types.Object`"
    assert ClassRef(text="~bpy.types.Object").astext() == ":class:`~bpy.types.Object`"
    assert ClassRef(text="!bpy.types.Object").astext() == ":class:`!bpy.types.Object`"
