from docutils.parsers.rst.directives import register_directive
from docutils.parsers.rst.roles import GenericRole, register_local_role

from bpystubgen.directives import ClassDirective, CurrentModuleDirective, DataDirective, FunctionDirective, \
    ModuleDirective
from bpystubgen.generator import generate
from bpystubgen.nodes import AttributeRef, ClassRef, DataRef, DocString, Function, FunctionRef, MethodRef, Module, \
    ModuleRef

register_directive("module", ModuleDirective)
register_directive("data", DataDirective)
register_directive("attribute", DataDirective)
register_directive("function", FunctionDirective)
register_directive("method", FunctionDirective)
register_directive("classmethod", FunctionDirective)
register_directive("staticmethod", FunctionDirective)
register_directive("class", ClassDirective)
register_directive("currentmodule", CurrentModuleDirective)

register_local_role("class", GenericRole("class", ClassRef))
register_local_role("mod", GenericRole("mod", ModuleRef))
register_local_role("func", GenericRole("func", FunctionRef))
register_local_role("meth", GenericRole("meth", MethodRef))
register_local_role("data", GenericRole("data", DataRef))
register_local_role("attr", GenericRole("attr", AttributeRef))
