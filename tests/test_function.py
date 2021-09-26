from inspect import cleandoc

from docutils.frontend import OptionParser
from docutils.nodes import document
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from pytest import fixture, mark

from bpystubgen.nodes import Argument, Class, Function, FunctionScope, Module


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
           "Loads :class:`~bge.logic.globalDict` from a file."


@mark.parametrize("signature", (
        ".. function:: glBlendFunc(sfactor, dfactor)  ",
        ".. function::   glBlendFunc(sfactor, dfactor)",
        ".. function:: glBlendFunc(sfactor, dfactor):",
        ".. function:: glBlendFunc  (sfactor, dfactor) : "))
def test_parse_with_spaces(parser: Parser, document: document, signature: str):
    parser.parse(signature, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    func = document.children[0]

    assert isinstance(func, Function)

    assert func.name == "glBlendFunc"
    assert not func.type

    assert len(func.arguments) == 2
    assert func.arguments[0].name == "sfactor"
    assert func.arguments[1].name == "dfactor"


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


@mark.parametrize("default", [
    "None",
    "'value'",
    "image.filepath",
    "list()",
    "tuple(3, 4)",
    "['a', 'b', 'c']"])
def test_arg_default_value(parser: Parser, document: document, default):
    source = f".. function:: init(name, arg1 = {default}, arg2=100)"

    parser.parse(source, document)
    document.transformer.apply_transforms()

    func = document.children[0]

    assert isinstance(func, Function)

    args = func.arguments

    assert len(args) == 3

    assert args[0].name == "name"
    assert not args[0].default

    assert args[1].name == "arg1"
    assert args[1].default == default

    assert args[2].name == "arg2"
    assert args[2].default == "100"


def test_parse_overloading(parser: Parser, document: document):
    source = cleandoc("""
       .. staticmethod:: chain(it, pred, modifier)
                         chain(it, pred)

          :arg it: The iterator on the ViewEdges of the ViewMap. It contains
             the chaining rule.
          :type it: :class:`ViewEdgeIterator`
          :arg pred: The predicate on the ViewEdge that expresses the
             stopping condition.
          :type pred: :class:`UnaryPredicate1D`
          :arg modifier: A function that takes a ViewEdge as argument and
             that is used to modify the processed ViewEdge state (the
             timestamp incrementation is a typical illustration of such a modifier).
             If this argument is not given, the time stamp is automatically managed.
          :type modifier: :class:`UnaryFunction1DVoid`
    """)

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 2

    (func1, func2) = document.children

    assert isinstance(func1, Function)
    assert isinstance(func2, Function)

    assert func1.name == "chain"
    assert func2.name == "chain"

    assert not func1.type
    assert not func2.type

    assert len(func1.arguments) == 3
    assert len(func2.arguments) == 2

    assert tuple(map(lambda a: a.name, func1.arguments)) == ("it", "pred", "modifier")
    assert tuple(map(lambda a: a.name, func2.arguments)) == ("it", "pred")


def test_parse_multiline(parser: Parser, document: document):
    source = """
       .. method:: __init__(num_iterations=100, factor_point=0.1, \
             factor_curvature=0.0, factor_curvature_difference=0.2, \
             aniso_point=0.0, aniso_normal=0.0, aniso_curvature=0.0, \
             carricature_factor=1.0)
       
          Builds a SmoothingShader object.
    """.strip()

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    func = document.children[0]

    assert isinstance(func, Function)

    assert func.name == "__init__"
    assert not func.type
    assert func.docstring and func.docstring.astext() == \
           "Builds a SmoothingShader object."

    assert len(func.arguments) == 8


@mark.parametrize("args", [
    ("isPlayingAction([layer])", "isPlayingAction", {}, {"layer"}),
    ("setAngularVelocity(velocity[, local])", "setAngularVelocity", {"velocity"}, {"local"}),
    ("applyImpulse(point, impulse[, local])", "applyImpulse", {"point", "impulse"}, {"local"}),
    ("Quaternion([seq, [angle]])", "Quaternion", {"seq"}, {"angle"})
])
def test_parse_optional_args(parser: Parser, document: document, args):
    (signature, name, required, optional) = args

    source = f".. function:: {signature}"

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    func = document.children[0]

    assert isinstance(func, Function)

    assert func.name == name
    assert len(func.arguments) == len(required) + len(optional)

    for arg in func.arguments:
        if arg.name in required:
            assert not arg.default
        else:
            assert arg.name in optional
            assert arg.default == "None"


def test_parse_bpy_prop_collection(parser: Parser, document: document):
    source = """
       .. function:: open(files=None)

           :arg files: A collection of files.
           :type files: :class:`bpy_prop_collection` of :class:`OperatorFileListElement`, (optional)
    """.strip()

    parser.parse(source, document)
    document.transformer.apply_transforms()

    assert len(document.children) == 1

    func = document.children[0]

    assert isinstance(func, Function)

    assert len(func.arguments) == 1
    assert func.arguments[0].type == "typing.Union[" \
                                     "typing.Sequence[OperatorFileListElement], " \
                                     "typing.Mapping[str, OperatorFileListElement], " \
                                     "bpy.types.bpy_prop_collection]"


def test_parse_alias(parser: Parser, document: document):
    source = """
       .. function:: glEvalCoord (u,v):

          B{glEvalCoord1d, glEvalCoord1f, glEvalCoord2d, glEvalCoord2f, glEvalCoord1dv, glEvalCoord1fv,
          glEvalCoord2dv, glEvalCoord2fv}

          Evaluate enabled one- and two-dimensional maps
    """.strip()

    parser.parse(source, document)
    document.transformer.apply_transforms()

    functions = set(map(lambda f: f.name, document.traverse(Function)))

    assert functions == {"glEvalCoord1d", "glEvalCoord", "glEvalCoord1dv", "glEvalCoord1f", "glEvalCoord1fv",
                         "glEvalCoord2d", "glEvalCoord2dv", "glEvalCoord2f", "glEvalCoord2fv"}


def test_parse_varargs(parser: Parser, document: document):
    source = """
       .. function:: app_template_paths(*, path=None)

          :type path: string
    """.strip()

    parser.parse(source, document)

    func = next(iter(document.traverse(Function)))
    args = func.arguments

    assert len(args) == 2

    assert args[0].name == "*args"
    assert not args[0].type

    assert args[1].name == "path"
    assert args[1].type == "str"

    assert func.signature == "def app_template_paths(*args, path: str = None) -> None:"


def test_parse_varargs_in_middle(parser: Parser, document: document):
    source = """
       .. method:: transform(matrix, *, scale=True, roll=True)

          :type matrix: :class:`mathutils.Matrix`
          :type scale: boolean
          :type roll: boolean
    """.strip()

    parser.parse(source, document)

    func = next(iter(document.traverse(Function)))
    args = func.arguments

    assert len(args) == 4

    assert args[0].name == "matrix"
    assert args[0].type == "mathutils.Matrix"

    assert args[1].name == "*args"
    assert not args[1].type

    assert args[2].name == "scale"
    assert args[2].type == "bool"
    assert args[2].default == "True"

    assert args[3].name == "roll"
    assert args[3].type == "bool"
    assert args[3].default == "True"

    assert func.signature == "def transform(self, matrix: mathutils.Matrix, " \
                             "*args, scale: bool = True, roll: bool = True) -> None:"


def test_parse_varargs_literal(parser: Parser, document: document):
    source = """
       .. method:: poll_message_set(message, *args)

          :type message: str
    """.strip()

    parser.parse(source, document)

    func = next(iter(document.traverse(Function)))
    args = func.arguments

    assert len(args) == 2

    assert args[0].name == "message"
    assert args[0].type == "str"

    assert args[1].name == "*args"
    assert not args[1].type

    assert func.signature == "def poll_message_set(self, message: str, *args) -> None:"


def test_parse_varargs_with_kwargs(parser: Parser, document: document):
    source = """
       .. function:: bake_action(obj, *, action, frames, **kwargs)

          :type obj: :class:`bpy.types.Object`
          :type action: :class:`bpy.types.Action`
          :type frames: iterable of int
    """.strip()

    parser.parse(source, document)

    func = next(iter(document.traverse(Function)))
    args = func.arguments

    assert len(args) == 5

    assert args[0].name == "obj"
    assert args[0].type == "bpy.types.Object"

    assert args[1].name == "*args"
    assert not args[1].type

    assert args[2].name == "action"
    assert args[2].type == "bpy.types.Action"

    assert args[3].name == "frames"
    assert args[3].type == "typing.Iterable[int]"

    assert args[4].name == "*kwargs"
    assert not args[4].type

    assert func.signature == "def bake_action(obj: bpy.types.Object, *args, action: bpy.types.Action, " \
                             "frames: typing.Iterable[int], *kwargs) -> None:"


def test_signature():
    func = Function(name="my_func")
    assert func.signature == "def my_func() -> None:"

    func.type = "str"
    assert func.signature == "def my_func() -> str:"

    func.scope = FunctionScope.Class
    assert func.signature == "@classmethod\ndef my_func(cls) -> str:"

    func.scope = FunctionScope.Instance
    assert func.signature == "def my_func(self) -> str:"

    func.scope = FunctionScope.Static
    assert func.signature == "@staticmethod\ndef my_func() -> str:"

    func.scope = FunctionScope.Module
    assert func.signature == "def my_func() -> str:"

    arg1 = Argument(name="arg1")
    func += arg1

    assert func.signature == "def my_func(arg1: typing.Any) -> str:"

    arg1.type = "int"

    arg2 = Argument(name="arg2", type="str", default="None")
    func += arg2

    assert func.signature == "def my_func(arg1: int, arg2: str = None) -> str:"


def test_referred_types():
    func = Function(name="my_func")
    func.type = "ClassA"

    func += Argument(name="arg1", type="ClassB")
    func += Argument(name="arg2", type="ClassC")

    assert func.referred_types == {"typing", "ClassA", "ClassB", "ClassC"}


def test_type_resolution():
    func = Function(name="my_func")
    func.type = "mymodule.LocalClass1"

    func += Argument(name="arg1", type="mymodule.LocalClass2")
    func += Argument(name="arg2", type="other.ExternalClass")

    module = Module(name="mymodule")

    module += Class(name="LocalClass1")
    module += Class(name="LocalClass2")

    module += func

    assert func.signature == \
           "def my_func(arg1: LocalClass2, arg2: other.ExternalClass) -> LocalClass1:"
