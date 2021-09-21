from typing import Final, Mapping, Union

from docutils.frontend import Values
from docutils.nodes import Element
from pkg_resources import resource_listdir, resource_stream, resource_string
from sphinx.environment import BuildEnvironment

from bpystubgen import Module, nodes
from bpystubgen.nodes import APIMember, Class

blacklist: Final = set(map(lambda b: b.decode("UTF-8"),
                           resource_string(__name__, "blacklist.txt").splitlines()))

patches: Final = set(map(lambda n: n[:-4],
                         filter(lambda f: f.endswith(".rst"), resource_listdir(__name__, "."))))

Patchable = Union[Module, Class]


def apply(name: str, target: Element, settings: Values, env: BuildEnvironment) -> Element:
    if name not in patches:
        return target

    source_path = name + ".rst"
    source = resource_stream(__name__, source_path)

    def members_of(elem: Element) -> Mapping[str, APIMember]:
        return dict(map(lambda m: (m.name, m), elem.traverse(APIMember)))

    patch = members_of(nodes.from_io(source, source_path, settings, env))
    members = members_of(target)

    for member in members.values():
        if member.name not in patch:
            continue

        index = target.index(member)
        target.insert(index, patch[member.name].deepcopy())

        member.parent.remove(member)

    names_to_add = set(patch.keys()).difference(members.keys())

    for key in filter(lambda k: k in names_to_add, patch.keys()):
        target += patch[key].deepcopy()

    return target
