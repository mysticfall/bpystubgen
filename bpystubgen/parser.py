import re
from typing import Final, Optional

_container_pattern1: Final = re.compile("^\\s*([a-z0-9-:`\\s]+)\\s+of\\s+([^$]+)$")

_container_pattern2: Final = re.compile("^\\s*([a-z0-9-:`]+)\\s*\\[\\s*([^]\\s]+)\\s*]\\s*$")

_simple_type_pattern: Final = re.compile("^\\s*([a-z]+)([,\\s][^a-zA-Z0-9_]+)?")

_reference_type_pattern: Final = re.compile("\\s*class:`[~!]?([a-zA-Z_0-9.]+)`")

_primitive_type_pattern: Final = re.compile("^\\s*([a-z]+)[,.]?\\s*$")

known_data_types: Final = {
    "str": "str",
    "strs": "str",
    "string": "str",
    "strings": "str",
    "int": "int",
    "ints": "int",
    "integer": "int",
    "integers": "int",
    "float": "float",
    "floats": "float",
    "double": "float",
    "doubles": "float",
    "bool": "bool",
    "bools": "bool",
    "boolean": "bool",
    "booleans": "bool",
    "list": "typing.List[typing.Any]",
    "tuple": "typing.Tuple[typing.Any, ...]"
}

known_container_types: Final = {
    "list": "typing.List",
    "vector": "typing.List",
    "array": "typing.Tuple",
    "tuple": "typing.Tuple",
    "sequence": "typing.Sequence"
}

numbers: Final = {
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}


def parse_primitive(text: str) -> Optional[str]:
    result = _primitive_type_pattern.search(text)

    if result:
        group = result.group(1)

        if group in known_data_types:
            return known_data_types[group]

    return None


def parse_type(text: str) -> Optional[str]:
    result = _container_pattern1.search(text)

    if not result:
        result = _container_pattern2.search(text)

    if result:  # e.g. "(some container) of (some values)"
        container_type: Optional[str] = None
        data_type: Optional[str] = None

        group = result.group(1)
        values = group.split(" ")

        if len(values) == 2:  # e.g. "float array"
            data_type = parse_primitive(values[0])

            if values[1] in known_container_types:
                container_type = known_container_types[values[1]]
        elif len(values) == 1:  # e.g. "tuple"
            if values[0] in known_container_types:
                container_type = known_container_types[values[0]]

            group = result.group(2)
            values = group.split(" ")

            if len(values) == 1:  # e.g. "bool"
                data_type = parse_primitive(values[0])
            elif len(values) == 2:  # e.g. "3 floats"
                pass

        if container_type:
            data_type = data_type if data_type else "typing.Any"

            return f"{container_type}[{data_type}]"

    result = _reference_type_pattern.search(text)

    if result:
        return "".join(['"', result.group(1), '"'])

    result = _simple_type_pattern.search(text)

    if result:
        return parse_primitive(result.group(1))

    return None
