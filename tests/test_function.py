from inspect import cleandoc

from docutils.frontend import OptionParser
from docutils.nodes import document
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from pytest import fixture

from bpystubgen.nodes import Argument, Function, FunctionScope


@fixture
def parser() -> Parser:
    return Parser()


@fixture
def document() -> document:
    components = (Parser,)
    settings = OptionParser(components=components).get_default_values()

    return new_document("", settings=settings)


# noinspection DuplicatedCode
def test_parse_simple(parser: Parser, document: document):
    source = cleandoc("""
        .. function:: loadGlobalDict()

           Loads :class:`~bge.logic.globalDict` from a file.
    """)

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    func = document.children[0]

    assert isinstance(func, Function)

    assert func.name == "loadGlobalDict"
    assert not func.type
    assert func.docstring and func.docstring.astext() == \
           "Loads :class:`globalDict <bge.logic.globalDict>` from a file."


# noinspection DuplicatedCode
def test_parse_with_rtype(parser: Parser, document: document):
    source = cleandoc("""
        .. function:: LibList()

           Returns a list of currently loaded libraries.

           :rtype: list [str]
    """)

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    func = document.children[0]

    assert isinstance(func, Function)

    assert func.name == "LibList"
    assert func.type == "typing.List[str]"


def test_parse_with_args(parser: Parser, document: document):
    source = cleandoc("""
    .. function:: LibNew(name, type, data)

       Uses existing datablock data and loads in as a new library.

       :arg name: A unique library name used for removal later
       :type name: string
       :arg type: The datablock type (currently only "Mesh" is supported)
       :type type: string
       :arg data: A list of names of the datablocks to load
       :type data: list of strings
    """)

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    func = document.children[0]

    assert isinstance(func, Function)

    assert func.name == "LibNew"
    assert not func.type
    assert func.docstring and func.docstring.children[0].astext() == \
           "Uses existing datablock data and loads in as a new library."

    args = func.arguments

    assert len(args) == 3

    assert args[0].name == "name"
    assert args[0].type == "str"

    assert args[1].name == "type"
    assert args[1].type == "str"

    assert args[2].name == "data"
    assert args[2].type == "typing.List[str]"


def test_signature():
    func = Function(name="my_func")
    assert func.signature == "def my_func() -> None:"

    func.type = "str"
    assert func.signature == "def my_func() -> str:"

    func.scope = FunctionScope.Class
    assert func.signature == "@classmethod\ndef my_func(cls) -> str:"

    func.scope = FunctionScope.Instance
    assert func.signature == "def my_func(self) -> str:"

    func.scope = FunctionScope.Module
    assert func.signature == "def my_func() -> str:"

    arg1 = Argument(name="arg1")
    func += arg1

    assert func.signature == "def my_func(arg1: typing.Any) -> str:"

    arg1.type = "int"

    arg2 = Argument(name="arg2", type="str")
    func += arg2

    assert func.signature == "def my_func(arg1: int, arg2: str) -> str:"
