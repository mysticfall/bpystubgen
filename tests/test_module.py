from inspect import cleandoc

from docutils.frontend import OptionParser
from docutils.nodes import document, paragraph, section, title
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from pytest import fixture

from bpystubgen.nodes import Class, Data, DataRef, DocString, Function, Import, Module


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
    assert len(module.children) == 4

    (docstring, imp, data, cls) = module.children

    assert isinstance(docstring, DocString)
    assert isinstance(imp, Import)
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

    assert imp.astext() == "typing"

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
