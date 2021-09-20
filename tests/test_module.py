from inspect import cleandoc

from docutils.frontend import OptionParser
from docutils.nodes import document, paragraph, section, title
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from pytest import fixture

from bpystubgen.nodes import Argument, Class, Data, DataRef, DocString, Function, Module


@fixture
def parser() -> Parser:
    return Parser()


@fixture
def document() -> document:
    components = (Parser,)
    settings = OptionParser(components=components).get_default_values()
    return new_document("", settings=settings)


def test_members():
    mod = Module(name="mymodule")

    mod += DocString(text="Test Module")

    mod += Data(name="mydata")
    mod += Function(name="myfunction")

    assert len(mod.members) == 2

    (data, func) = mod.members

    assert data.name == "mydata"
    assert func.name == "myfunction"


def test_parse(parser: Parser, document: document):
    source = cleandoc("""

        .. module::   bpy.ops.logic   
    """)

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    module = document.children[0]

    assert isinstance(module, Module)
    assert module.name == "bpy.ops.logic"


# noinspection DuplicatedCode
def test_transform(parser: Parser, document: document):
    source = cleandoc("""
        Game Logic (bge.logic)
        ======================

        .. module:: bge.logic

        Module to access logic functions, imported automatically into the 
        python controllers namespace.

        .. data:: mouse

           The current mouse wrapped in an :class:`~bge.types.SCA_PythonMouse` object.

        .. class:: Buffer

           For Python access to GPU functions requiring a pointer.

           .. attribute:: dimensions
    """)

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    module = document.children[0]

    assert isinstance(module, Module)

    module.import_types()

    assert len(module.children) == 4

    (docstring, imp, data, cls) = module.children

    assert isinstance(docstring, DocString)
    assert isinstance(data, Data)
    assert isinstance(cls, Class)

    assert module.name == "bge.logic"

    assert len(docstring.children) == 1

    s = docstring.children[0]

    assert isinstance(s, section)

    assert len(s.children) == 4

    (t, p, r, c) = s.children

    assert isinstance(t, title)
    assert isinstance(p, paragraph)
    assert isinstance(r, paragraph)

    assert t.astext() == "Game Logic (bge.logic)"
    assert p.astext().replace("\n", " ") == \
           "Module to access logic functions, imported automatically " \
           "into the python controllers namespace."

    assert imp.astext() == "import typing"

    assert data.name == "mouse"
    assert data.docstring and data.docstring.astext() == \
           "The current mouse wrapped in an :class:`SCA_PythonMouse " \
           "<bge.types.SCA_PythonMouse>` object."

    assert len(r.children) == 1

    ref = r.children[0]

    assert isinstance(ref, DataRef)
    assert ref.astext() == ":data:`mouse`"

    assert cls.name == "Buffer"

    assert len(cls.children) == 2

    (d, a) = cls.children

    assert isinstance(d, DocString)
    assert isinstance(a, Data)

    assert a.name == "dimensions"


def test_import():
    module = Module(name="myproject")

    module += DocString(text="My Module")

    var1 = Data(name="var1")
    var1.type = "class:`bge.types.KX_GameObject`"

    module += var1

    var2 = Data(name="var2")
    var2.type = "class:`~bge.types.KX_Camera`"

    module += var2

    cls = Class(name="LocalClass")

    module += cls

    cls_lc = Class(name="local_class")

    module += cls_lc

    func1 = Function(name="func1")
    func1.type = "str"

    arg1 = Argument(name="obj", type="class:`bpy.types.Object`")
    arg2 = Argument(name="value1", type="class:`LocalClass`")
    arg3 = Argument(name="value2", type="class:`local_class`")

    func1 += arg1
    func1 += arg2
    func1 += arg3

    module += func1

    var3 = Data(name="var3")
    var3.type = "class:`myproject.LocalClass`"

    module += var3

    var4 = Data(name="var4")
    var4.type = "class:`LocalClass`"

    module += var4

    var5 = Data(name="var5")
    var5.type = "class:`myproject.local_class`"

    module += var5

    var6 = Data(name="var6")
    var6.type = "class:`local_class`"

    module += var6

    module.import_types()

    imports = module.imports

    assert isinstance(module.children[0], DocString)
    assert imports and len(imports) == 3

    ordered = sorted(map(lambda i: i.astext(), imports))

    assert ordered[0] == "import bge"
    assert ordered[1] == "import bpy"
    assert ordered[2] == "import typing"


def test_sort_members():
    module = Module(name="mymodule")

    def define_class(name, base_types):
        cls = Class(name=name)
        cls.base_types = base_types

        return cls

    module += define_class("TypeA", {"TypeC", "TypeB"})
    module += define_class("TypeB", {"bpy.types.Object"})
    module += define_class("TypeC", {"TypeB"})
    module += define_class("TypeD", {"TypeA"})
    module += define_class("TypeE", {})

    module.sort_members()

    members = tuple(map(lambda m: m.name, module.members))

    assert members == ("TypeB", "TypeE", "TypeC", "TypeA", "TypeD")


def test_localise_name():
    module = Module(name="bpy")

    assert module.localise_name("Object") == "Object"
    assert module.localise_name("bpy.Object") == "Object"
    assert module.localise_name("bpy.types.Object") == "types.Object"

    submodule = Module(name="bpy.types")

    assert submodule.localise_name("Object") == "Object"
    assert submodule.localise_name("bpy.Object") == "bpy.Object"
    assert submodule.localise_name("bpy.types.Object") == "Object"


# noinspection DuplicatedCode
def test_referred_types():
    func = Function(name="func")
    func.type = "ClassA"

    func += Argument(name="arg1", type="ClassB")

    data = Data(name="data")
    data.type = "ClassC"

    cls = Class(name="MyClass")

    cls += func
    cls += data

    module = Module(name="MyModule")

    data2 = Data(name="data2")
    data2.type = "ClassD"

    module += cls
    module += data2

    assert module.referred_types == {"typing", "ClassA", "ClassB", "ClassC", "ClassD"}
