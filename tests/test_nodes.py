from typing import Type

from pytest import mark

from bpystubgen.nodes import Argument, Data, DocString, Documentable, Function, Module, Named, Typed


@mark.parametrize("node_type", (Module, Data, Function, Argument))
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


@mark.parametrize("node_type", (Data, Function, Argument))
def test_typed(node_type: Type[Typed]):
    node = node_type()

    assert isinstance(node, Typed)
    assert not node.type

    node.type = "type"
    assert node.type == "type"

    node.type = None
    assert not node.type


@mark.parametrize("node_type", (Module, Data, Function, Argument))
def test_docstring(node_type: Type[Documentable]):
    node = node_type()

    assert isinstance(node, Documentable)
    assert not node.docstring

    docstring = DocString("comment")

    node += docstring

    assert node.docstring == docstring
