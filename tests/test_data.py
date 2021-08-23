from inspect import cleandoc

from docutils.frontend import OptionParser
from docutils.nodes import document
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from pytest import fixture

from bpystubgen.nodes import Data, DocString


@fixture
def parser() -> Parser:
    return Parser()


@fixture
def document() -> document:
    components = (Parser,)
    settings = OptionParser(components=components).get_default_values()

    return new_document("", settings=settings)


# noinspection DuplicatedCode
def test_parse(parser: Parser, document: document):
    source = cleandoc("""
        .. data::  upbge_version_string  

           The UPBGE version formatted as a string, eg. "0.0 (sub 3)".

           :type:  str  
    """)

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    data = document.children[0]

    assert isinstance(data, Data)

    assert data.name == "upbge_version_string"
    assert data.type == "str"

    assert len(data.children) == 1

    docstring = data.children[0]

    assert isinstance(docstring, DocString)
    assert docstring.astext() == "The UPBGE version formatted as a string, eg. \"0.0 (sub 3)\"."


# noinspection DuplicatedCode
def test_parse_missing_type(parser: Parser, document: document):
    source = cleandoc("""
        .. data:: mouse

           The current mouse wrapped in an :class:`bge.types.SCA_PythonMouse` object.
    """)

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    data = document.children[0]

    assert isinstance(data, Data)

    assert data.name == "mouse"
    assert data.type == "typing.Any"

    assert len(data.children) > 0

    docstring = data.children[0]

    assert isinstance(docstring, DocString)
    assert len(docstring.children) > 0
    assert docstring.children[0].astext() == \
           "The current mouse wrapped in an :class:`bge.types.SCA_PythonMouse` object."


def test_signature():
    data = Data(name="value")
    assert data.signature == "value: typing.Any = ..."

    data.type = "str"
    assert data.signature == "value: str = ..."
