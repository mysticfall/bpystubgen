from __future__ import annotations

from pathlib import Path
from typing import AbstractSet, Iterable, MutableMapping, Optional, Sequence, ValuesView, cast

from docutils.frontend import Values
from docutils.io import FileOutput
from docutils.nodes import document
from docutils.utils import new_document
from docutils.writers import Writer
from sphinx.environment import BuildEnvironment

import bpystubgen
from bpystubgen import nodes, patches
from bpystubgen.nodes import Class, DocString, Import, Module


class Task:

    @classmethod
    def create(cls, src_dir: Path, pattern: str = "*.rst") -> Task:
        root = Task()

        def resolve(path: Sequence[str], context: Task) -> Task:
            count = len(path)

            assert count > 0

            name = path[0]

            if name in context.keys():
                child = context[name]
            else:
                full_name = ".".join((context.full_name, name))

                if name[0].isupper() or full_name in bpystubgen.lowercase_class_names:
                    child = ClassTask(name, parent=context)
                else:
                    child = ModuleTask(name, parent=context)

            if count == 1:
                return child

            return resolve(path[1:], child)

        for file in sorted(src_dir.rglob(pattern)):
            segments = file.name.split(".")[:-1]

            if ".".join(segments) in patches.blacklist:
                continue

            task = resolve(segments, root)
            task.source = file

        return root

    def __init__(self, name: str = "", parent: Optional[Task] = None) -> None:
        self._name = name
        self._parent = parent
        self._children: MutableMapping[str, Task] = dict()

        if parent:
            parent._children[self.name] = self

            segments = list(filter(any, map(lambda a: a.name, self.ancestors)))
            segments.append(self.name)

            self._full_name = ".".join(segments)
        else:
            self._full_name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def full_name(self) -> str:
        return self._full_name

    @property
    def parent(self) -> Optional[Task]:
        return self._parent

    @property
    def ancestors(self) -> Iterable[Task]:
        if self.parent:
            yield from self.parent.ancestors
            yield self.parent

    def keys(self) -> AbstractSet[str]:
        return self._children.keys()

    def values(self) -> ValuesView[Task]:
        return self._children.values()

    def __getitem__(self, key: str) -> Task:
        return self._children[key]

    def __iter__(self) -> Iterable[Task]:
        for child in self.values():
            yield from child.__iter__()
            yield child

    def __len__(self) -> int:
        return len(self._children)

    def __repr__(self) -> str:
        return self.full_name

    def __bool__(self) -> bool:
        return True


class ParserTask(Task):

    def __init__(self, name: str = "", parent: Optional[Task] = None) -> None:
        super().__init__(name, parent)

        self.source: Optional[Path] = None
        self.doctree: Optional[document] = None

    def parse(self, settings: Values, env: BuildEnvironment) -> Optional[document]:
        if self.source:
            doc = nodes.from_path(self.source, settings, env)

            self.doctree = patches.apply(self.name, doc, settings, env)
        else:
            self.doctree = None

        return self.doctree


class ClassTask(ParserTask):
    pass


class ModuleTask(ParserTask):

    def parse(self, settings: Values, env: BuildEnvironment) -> Optional[document]:
        doctree = super().parse(settings, env)

        if not doctree:
            doctree = new_document("", settings=settings)
            doctree += patches.apply(self.full_name, Module(name=self.full_name), settings, env)

        self.doctree = doctree

        try:
            module = next(iter(doctree.traverse(Module)))
        except StopIteration:
            module = Module(name=self.full_name)

            docstring = DocString()

            for child in tuple(doctree.children):
                doctree.remove(child)
                docstring += child

            module += docstring

            doctree += patches.apply(self.full_name, module, settings, env)

            doctree.transformer.apply_transforms()

        for cls in module.traverse(Class):
            patches.apply(cls.full_name, cls, settings, env)

        classes = filter(lambda c: isinstance(c, ClassTask) and c.doctree, self.values())
        submodules = filter(lambda c: isinstance(c, ModuleTask) and c.doctree, self.values())

        for child in classes:
            for node in cast(ClassTask, child).doctree.traverse(Class):
                node.parent.remove(node)
                module += node

        module.import_types()
        module.sort_members()

        index = 1 if module.docstring else 0

        for child in submodules:
            for node in cast(ModuleTask, child).doctree.traverse(Module):
                module.insert(index, Import(module=".", types=module.localise_name(node.name)))

        return doctree

    def target_path(self, dest_dir: Path) -> Path:
        top_level = not any(self.ancestors)
        has_submodule = any(filter(lambda c: isinstance(c, ModuleTask), self.values()))

        if top_level or has_submodule:
            parent_dir = Path(dest_dir, "/".join(self.full_name.split("."))).resolve()
            return parent_dir / "__init__.pyi"
        else:
            parent_dir = Path(dest_dir, "/".join(self.full_name.split(".")[:-1])).resolve()
            return parent_dir / (self.name + ".pyi")

    def generate(self, dest_dir: Path, writer: Writer) -> Optional[Path]:
        target = self.target_path(dest_dir)

        target.parent.mkdir(parents=True, exist_ok=True)

        marker = target.parent / "py.typed"

        with open(marker, "w"):
            pass

        fout = FileOutput(destination_path=str(target))

        try:
            writer.write(self.doctree, fout)
            writer.assemble_parts()
        finally:
            fout.close()

        return target
