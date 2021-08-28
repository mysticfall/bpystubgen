from inspect import cleandoc

from docutils.frontend import OptionParser
from docutils.nodes import document, field_list
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from pytest import fixture

from bpystubgen.nodes import Class, Data, DocString, Function, FunctionScope


@fixture
def parser() -> Parser:
    return Parser()


@fixture
def document() -> document:
    components = (Parser,)
    settings = OptionParser(components=components).get_default_values()
    return new_document("", settings=settings)


def test_parse(parser: Parser, document: document):
    source = cleandoc("""
        .. class:: Buffer

           For Python access to GPU functions requiring a pointer.

           .. attribute:: dimensions

           .. method:: draw()
   
              Run the drawing program with the parameters assigned to the batch.
    """)

    # noinspection DuplicatedCode
    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    cls = document.children[0]

    assert isinstance(cls, Class)
    assert cls.name == "Buffer"

    assert len(cls.children) == 3

    (docstring, data, func) = cls.children

    assert isinstance(docstring, DocString)
    assert isinstance(data, Data)
    assert isinstance(func, Function)

    assert docstring.astext() == "For Python access to GPU functions requiring a pointer."
    assert data.name == "dimensions"
    assert func.name == "draw"


def test_parse_constructor(parser: Parser, document: document):
    source = cleandoc("""
        .. class:: Buffer(format, dimensions, data)

           For Python access to GPU functions requiring a pointer.

           :arg format: Format type to interpret the buffer.
           :type format: str
           :arg dimensions: Array describing the dimensions.
           :type dimensions: int
           :arg data: Optional data array.
           :type data: (Unparseable string)

           .. method:: draw()
    """)

    # noinspection DuplicatedCode
    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    cls = document.children[0]

    assert isinstance(cls, Class)
    assert cls.name == "Buffer"

    assert len(cls.children) == 3

    (docstring, ctor, meth) = cls.children

    assert docstring.astext() == "For Python access to GPU functions requiring a pointer."

    assert isinstance(docstring, DocString)
    assert isinstance(ctor, Function)
    assert isinstance(meth, Function)

    assert ctor.name == "__init__"
    assert ctor.type == "None"

    docstring = ctor.children[0]

    assert isinstance(docstring, DocString)

    assert len(docstring.children) == 1
    assert isinstance(docstring.children[0], field_list)

    args = ctor.arguments

    assert len(args) == 3

    assert args[0].name == "format"
    assert args[0].type == "str"

    assert args[1].name == "dimensions"
    assert args[1].type == "int"

    assert args[2].name == "data"
    assert args[2].type == "typing.Any"

    assert meth.name == "draw"
    assert meth.scope == FunctionScope.Instance


def test_parse_non_constructor(parser: Parser, document: document):
    source = cleandoc("""
        .. class:: KX_Camera(KX_GameObject)

           A Camera object.
    """)

    # noinspection DuplicatedCode
    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    cls = document.children[0]

    assert isinstance(cls, Class)

    assert len(cls.children) == 1
    assert isinstance(cls.children[0], DocString)
