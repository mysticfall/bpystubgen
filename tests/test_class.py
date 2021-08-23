from inspect import cleandoc

from docutils.frontend import OptionParser
from docutils.nodes import document
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from pytest import fixture

from bpystubgen.nodes import Class, Data, DocString, Module


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
        GPU Types (gpu.types)
        =====================

        .. module:: gpu.types

        .. class:: Buffer(format, dimensions, data)

           For Python access to GPU functions requiring a pointer.

           :arg format: Format type to interpret the buffer.
           :type type: str
           :arg dimensions: Array describing the dimensions.
           :type dimensions: int
           :arg data: Optional data array.
           :type data: sequence

           return the buffer as a list

           .. attribute:: dimensions
    """)

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    module = document.children[0]

    assert isinstance(module, Module)
    assert module.name == "gpu.types"

    cls = module.children[-1]

    assert isinstance(cls, Class)
    assert cls.name == "Buffer"

    assert len(cls.children) == 2

    (docstring, data) = cls.children

    assert isinstance(docstring, DocString)
    assert isinstance(data, Data)
