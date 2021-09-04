from inspect import cleandoc

from docutils.frontend import OptionParser
from docutils.nodes import document
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from pytest import fixture

from bpystubgen.nodes import Class, DocString, Module, Property


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
        .. property::  loggerName  

           A name used to create the logger instance.

           :type:  str  
    """)

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    prop = document.children[0]

    assert isinstance(prop, Property)

    assert prop.name == "loggerName"
    assert prop.type == "str"

    assert len(prop.children) == 1

    docstring = prop.children[0]

    assert isinstance(docstring, DocString)
    assert docstring.astext() == "A name used to create the logger instance."


# noinspection DuplicatedCode
def test_parse_missing_type(parser: Parser, document: document):
    source = cleandoc("""
        .. property:: logger

           A logger instance that can be used to log messages related to this object (read-only).
    """)

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    data = document.children[0]

    assert isinstance(data, Property)

    assert data.name == "logger"
    assert data.type == "typing.Any"

    assert len(data.children) > 0

    docstring = data.children[0]

    assert isinstance(docstring, DocString)
    assert len(docstring.children) > 0
    assert docstring.children[0].astext() == \
           "A logger instance that can be used to log messages related to this object (read-only)."


def test_signature():
    prop = Property(name="value")
    assert prop.signature == "@property\ndef value(self) -> typing.Any:"

    prop.type = "str"
    assert prop.signature == "@property\ndef value(self) -> str:"


def test_type_resolution():
    prop1 = Property(name="prop1", type="mymodule.LocalClass1")
    prop2 = Property(name="prop2", type="mymodule.LocalClass2")
    prop3 = Property(name="prop3", type="other.ExternalClass")

    module = Module(name="mymodule")

    module += Class(name="LocalClass1")
    module += Class(name="LocalClass2")

    module += prop1
    module += prop2
    module += prop3

    assert prop1.signature == "@property\ndef prop1(self) -> LocalClass1:"
    assert prop2.signature == "@property\ndef prop2(self) -> LocalClass2:"
    assert prop3.signature == "@property\ndef prop3(self) -> other.ExternalClass:"
