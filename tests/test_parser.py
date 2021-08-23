from bpystubgen.types import parse_type


def test_parse_empty():
    assert not parse_type("")
    assert not parse_type("  ")
    assert not parse_type("\n")


def test_parse_str():
    assert parse_type("str") == "str"
    assert parse_type("string") == "str"
    assert parse_type("string, default \"\", (never None)") == "str"
    assert parse_type("\n str,default \"\", (readonly)") == "str"
    assert parse_type(":class:`Substring`") != "str"


def test_parse_bool():
    assert parse_type("bool") == "bool"
    assert parse_type("boolean") == "bool"
    assert parse_type("boolean, default True") == "bool"
    assert parse_type("\n bool,default False") == "bool"
    assert parse_type(":class:`Cbool`") != "bool"


def test_parse_int():
    assert parse_type("int") == "int"
    assert parse_type("integer") == "int"
    assert parse_type("int in [0, 10000], default 0") == "int"
    assert parse_type("\n integer (0-100) ") == "int"
    assert parse_type("list of integer") != "int"


def test_parse_float():
    assert parse_type("float") == "float"
    assert parse_type("float in [0, 1], default 1.0") == "float"
    assert parse_type("\n float (0-100) ") == "float"
    assert parse_type("float array of 2 items in [-inf, inf], default (0.0, 0.0)") != "float"
    assert parse_type("double") == "float"


def test_parse_list():
    assert parse_type("list of float") == "typing.List[float]"
    assert parse_type("list of strings") == "typing.List[str]"
    assert parse_type("list of float.") == "typing.List[float]"
    assert parse_type("list[str]") == "typing.List[str]"
    assert parse_type("list [ float ] ") == "typing.List[float]"
    assert parse_type("list") == "typing.List[typing.Any]"


def test_parse_class():
    assert parse_type("class:`bge.types.KX_GameObject`") == "bge.types.KX_GameObject"
    assert parse_type("class:`~bge.types.KX_GameObject`") == "bge.types.KX_GameObject"
    assert parse_type("class:`!bge.types.KX_GameObject`") == "bge.types.KX_GameObject"
