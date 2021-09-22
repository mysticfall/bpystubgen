import shutil
import tempfile
from pathlib import Path

from docutils.frontend import OptionParser, Values
from docutils.parsers.rst import Parser
from docutils.writers import Writer
from pytest import fixture
from sphinx.application import Sphinx
from sphinxcontrib.builders.rst import RstBuilder

from bpystubgen.nodes import Class, Data, Function, Module
from bpystubgen.tasks import ClassTask, ModuleTask, ParserTask, Task
from bpystubgen.writer import StubWriter


@fixture
def app() -> Sphinx:
    dest_path = Path(tempfile.tempdir) / "bpystubgen-test"

    yield Sphinx(srcdir=".", confdir=None, outdir=str(dest_path), doctreedir=".", buildername="text")

    shutil.rmtree(dest_path)


@fixture
def settings(app: Sphinx) -> Values:
    components = (Parser,)
    settings = OptionParser(components=components).get_default_values()

    settings.line_length_limit = 15000
    settings.report_level = 5
    settings.traceback = True
    settings.env = app.env

    return settings


@fixture
def writer(app: Sphinx) -> Writer:
    builder = RstBuilder(app)
    builder.config.rst_indent = 2

    return StubWriter(builder)


@fixture
def rst_path() -> Path:
    return Path(__file__).parent / "fixtures" / "rst"


@fixture
def stub_path() -> Path:
    return Path(__file__).parent / "fixtures" / "stub"


def test_create(rst_path: Path):
    modules = Task.create(rst_path)

    assert type(modules) == Task
    assert set(modules.keys()) == {"bge", "bgl", "mathutils"}

    bge = modules["bge"]

    assert type(bge) == ModuleTask
    assert set(bge.keys()) == {"logic", "types"}

    logic = bge["logic"]

    assert type(logic) == ModuleTask
    assert not any(logic.keys())

    types = bge["types"]

    assert type(types) == ModuleTask
    assert set(types.keys()) == {"KX_Scene", "KX_GameObject", "KX_PythonComponent"}
    assert all(map(lambda c: isinstance(c, ClassTask), types.values()))

    bgl = modules["bgl"]

    assert type(bgl) == ModuleTask
    assert not any(bgl.keys())

    mathutils = modules["mathutils"]

    assert type(mathutils) == ModuleTask
    assert mathutils.keys() == {"geometry"}


def test_create_with_pattern(rst_path: Path):
    root = Task.create(rst_path, "bge*.rst")

    assert set(root.keys()) == {"bge"}

    bge = root["bge"]

    assert type(bge) == ModuleTask
    assert set(bge.keys()) == {"logic", "types"}


def test_full_name():
    grand_parent = Task("bge")
    parent = Task("types", grand_parent)
    child = Task("KX_GameObject", parent)

    assert grand_parent.full_name == "bge"
    assert parent.full_name == "bge.types"
    assert child.full_name == "bge.types.KX_GameObject"


def test_get_item():
    bge = Task("bge")
    types = Task("types", parent=bge)

    assert bge["types"] == types


def test_hierarchy():
    bge = Task("bge")
    types = Task("types", bge)
    game_object = Task("KX_GameObject", types)
    component = Task("KX_PythonComponent", types)

    assert tuple(bge.ancestors) == ()
    assert bge.keys() == {"types"}
    assert bge["types"] == types

    assert tuple(types.ancestors) == (bge,)
    assert types.keys() == {"KX_GameObject", "KX_PythonComponent"}
    assert types["KX_GameObject"] == game_object
    assert types["KX_PythonComponent"] == component

    assert tuple(game_object.ancestors) == (bge, types)
    assert not any(game_object.keys())

    assert tuple(component.ancestors) == (bge, types)
    assert not any(component.keys())


def test_iter(rst_path: Path):
    names = tuple(map(lambda t: t.full_name, Task.create(rst_path)))

    assert names == ("bge.logic",
                     "bge.types.KX_GameObject",
                     "bge.types.KX_PythonComponent",
                     "bge.types.KX_Scene",
                     "bge.types",
                     "bge",
                     "bgl",
                     "mathutils.geometry",
                     "mathutils")


# noinspection DuplicatedCode
def test_parse(rst_path: Path, settings: Values, app: Sphinx):
    modules = Task.create(rst_path, "bge.types.KX_GameObject.rst")
    obj = modules["bge"]["types"]["KX_GameObject"]

    assert isinstance(obj, ParserTask)

    doc = obj.parse(settings, app.env)

    assert doc

    cls = next(iter(doc.traverse(Class)))

    assert cls.name == "KX_GameObject"
    assert cls.docstring
    assert cls.docstring.astext().startswith("All game objects")

    members = dict(map(lambda m: (m.name, m), cls.members))

    assert len(members) == 106
    assert isinstance(members["name"], Data)
    assert isinstance(members["applyForce"], Function)


def test_parse_module(rst_path: Path, settings: Values, app: Sphinx):
    bge = Task.create(rst_path, "bge.types.*")["bge"]

    assert isinstance(bge, ModuleTask)
    assert len(bge.keys()) == 1

    types = bge["types"]

    assert isinstance(types, ModuleTask)
    assert len(types.keys()) == 3

    children = (types["KX_GameObject"], types["KX_PythonComponent"], types["KX_Scene"])
    classes = {}

    for child in children:
        assert isinstance(child, ClassTask)
        assert not any(child.keys())

        child.parse(settings, app.env)

        classes[child.name] = next(iter(child.doctree.traverse(Class)))

    assert classes.keys() == {"KX_GameObject", "KX_PythonComponent", "KX_Scene"}

    module = next(iter(types.parse(settings, app.env).traverse(Module)))
    imports = module.imports

    assert set(map(lambda i: i.module, imports)) == {"logging", "bpy", "typing", "mathutils"}

    assert len(module.members) == 3
    assert all(map(lambda c: classes[c.name] == c, module.traverse(Class)))

    module = next(iter(bge.parse(settings, app.env)))
    imports = module.imports

    assert len(imports) == 2
    assert dict(map(lambda i: (i.module, i.types), imports)) == {".": ("types",), "typing": ()}


def test_target_path(rst_path: Path):
    dest_dir = Path("/target")
    modules = Task.create(rst_path)

    bge = modules["bge"]

    assert isinstance(bge, ModuleTask)
    assert bge.target_path(dest_dir) == dest_dir / "bge" / "__init__.pyi"

    types = bge["types"]

    assert isinstance(types, ModuleTask)
    assert types.target_path(dest_dir) == dest_dir / "bge" / "types.pyi"

    logic = bge["logic"]

    assert isinstance(logic, ModuleTask)
    assert logic.target_path(dest_dir) == dest_dir / "bge" / "logic.pyi"

    bgl = modules["bgl"]

    assert isinstance(bgl, ModuleTask)
    assert bgl.target_path(dest_dir) == dest_dir / "bgl.pyi"


def test_generate(rst_path: Path, stub_path: Path, writer: StubWriter, settings: Values, app: Sphinx):
    root = Task.create(rst_path)

    dest_dir = Path(app.outdir)

    for task in root:
        if isinstance(task, ParserTask):
            task.parse(settings, app.env)

        if isinstance(task, ModuleTask):
            task.generate(dest_dir, writer)

    expected_files = set(map(lambda p: p.relative_to(stub_path), stub_path.glob("**/*")))
    generated_files = set(map(lambda p: p.relative_to(dest_dir), dest_dir.glob("**/*")))

    assert len(expected_files) == 11
    assert generated_files == expected_files

    for path in generated_files:
        abs_path = dest_dir / path

        if abs_path.is_dir():
            continue

        generated = abs_path.read_text("UTF-8")
        expected = (stub_path / path).read_text("UTF-8")

        assert generated == expected
