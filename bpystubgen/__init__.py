from typing import Final

from docutils.parsers.rst.directives import register_directive
from docutils.parsers.rst.roles import GenericRole, register_local_role

from bpystubgen.directives import ClassDirective, CurrentModuleDirective, DataDirective, FunctionDirective, \
    ModuleDirective, PropertyDirective
from bpystubgen.nodes import AttributeRef, ClassRef, DataRef, DocString, Function, FunctionRef, MethodRef, Module, \
    ModuleRef, PropertyRef, PythonRef, Reference

lowercase_class_names: Final = {
    "bpy.types.bpy_prop_collection",
    "bpy.types.bpy_struct",
    "bpy.types.wmOwnerID",
    "bpy.types.wmOwnerIDs",
    "bpy.types.wmTools"
}

register_directive("module", ModuleDirective)
register_directive("data", DataDirective)
register_directive("attribute", DataDirective)
register_directive("property", PropertyDirective)
register_directive("function", FunctionDirective)
register_directive("method", FunctionDirective)
register_directive("classmethod", FunctionDirective)
register_directive("staticmethod", FunctionDirective)
register_directive("class", ClassDirective)
register_directive("currentmodule", CurrentModuleDirective)

_known_roles = (
    ("ref", Reference),
    ("mod", ModuleRef),
    ("class", ClassRef),
    ("func", FunctionRef),
    ("meth", MethodRef),
    ("data", DataRef),
    ("attr", AttributeRef),
    ("property", PropertyRef)
)

for (name, cls) in _known_roles:
    register_local_role(name, GenericRole(name, cls))

    if issubclass(cls, PythonRef):
        register_local_role("py:" + name, GenericRole("py:" + name, cls))
