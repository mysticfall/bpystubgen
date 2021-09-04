from logging import Logger, getLogger
from typing import List

from docutils.nodes import Node, SkipNode, Text, literal_block, system_message
from docutils.utils import Reporter
from sphinx.writers.text import MAXWIDTH
from sphinxcontrib.writers.rst import RstTranslator, RstWriter

from bpystubgen.nodes import APIMember, Argument, AttributeRef, Class, ClassRef, Data, DataRef, DocString, Function, \
    FunctionRef, FunctionScope, Import, MethodRef, Module, ModuleRef, Property, PropertyRef, Reference


class StubWriter(RstWriter):

    def translate(self) -> None:
        visitor = StubTranslator(self.document, self.builder)

        self.document.walkabout(visitor)
        self.output = visitor.body


# noinspection PyPep8Naming, PyUnusedLocal
class StubTranslator(RstTranslator):
    logger: Logger = getLogger("StubTranslator")

    def wrap(self, text: str, width: int = MAXWIDTH) -> List[str]:
        # Disable wrapping.
        return [text]

    def visit_DocString(self, node: DocString) -> None:
        self.new_state(0)
        self.add_text("\"\"\"")

    def depart_DocString(self, node: DocString) -> None:
        self.add_text("\"\"\"")
        self.end_state()

    def visit_Module(self, node: Module) -> None:
        self.new_state(0)

    def depart_Module(self, node: Module) -> None:
        self.end_state()

    def visit_Import(self, node: Import) -> None:
        self.new_state(0)
        self.add_text(node.astext())
        self.end_state()

        raise SkipNode

    def depart_Import(self, node: Import) -> None:
        pass

    def visit_APIMember(self, node: APIMember) -> None:
        name = node.name

        if not name or not any(name):
            self.logger.warning("Ignoring a member node without a name: %s", node.astext())
            raise SkipNode

        self.new_state(0)

        for line in node.signature.split("\n"):
            self.new_state(0)
            self.add_text(line)
            self.end_state()

        if node.has_body:
            self.new_state(self.indent)

    def depart_APIMember(self, node: APIMember) -> None:
        if node.has_body:
            self.end_state()

        self.end_state()

    def visit_Data(self, node: Data) -> None:
        self.visit_APIMember(node)

    def depart_Data(self, node: Data) -> None:
        self.depart_APIMember(node)

    def visit_Property(self, node: Property) -> None:
        self.visit_APIMember(node)

    def depart_Property(self, node: Property) -> None:
        self.add_text("...")
        self.depart_APIMember(node)

    def visit_Function(self, node: Function) -> None:
        # Fix documentation errors.
        if isinstance(node.parent, Class) and node.scope == FunctionScope.Module:
            node.scope = FunctionScope.Instance

        self.visit_APIMember(node)

    def depart_Function(self, node: Function) -> None:
        self.add_text("...")
        self.depart_APIMember(node)

    def visit_Class(self, node: Class) -> None:
        self.visit_APIMember(node)

    def depart_Class(self, node: Class) -> None:
        if not any(node.members):
            self.add_text("...")

        self.depart_APIMember(node)

    def visit_Argument(self, node: Argument) -> None:
        raise SkipNode

    def depart_Argument(self, node: Argument) -> None:
        pass

    def visit_Reference(self, node: Reference) -> None:
        self.add_text(node.astext())

        raise SkipNode

    def visit_ModuleRef(self, node: ModuleRef) -> None:
        self.visit_Reference(node)

    def depart_ModuleRef(self, node: ModuleRef) -> None:
        pass

    def visit_DataRef(self, node: DataRef) -> None:
        self.visit_Reference(node)

    def depart_DataRef(self, node: DataRef) -> None:
        pass

    def visit_FunctionRef(self, node: FunctionRef) -> None:
        self.visit_Reference(node)

    def depart_FunctionRef(self, node: FunctionRef) -> None:
        pass

    def visit_ClassRef(self, node: ClassRef) -> None:
        self.visit_Reference(node)

    def depart_ClassRef(self, node: ClassRef) -> None:
        pass

    def visit_AttributeRef(self, node: AttributeRef) -> None:
        self.visit_Reference(node)

    def depart_AttributeRef(self, node: AttributeRef) -> None:
        pass

    def visit_PropertyRef(self, node: PropertyRef) -> None:
        self.visit_Reference(node)

    def depart_PropertyRef(self, node: PropertyRef) -> None:
        pass

    def visit_MethodRef(self, node: MethodRef) -> None:
        self.visit_Reference(node)

    def depart_MethodRef(self, node: MethodRef) -> None:
        pass

    def visit_system_message(self, node: system_message) -> None:
        level = node["level"]

        if level == Reporter.DEBUG_LEVEL:
            logger = self.logger.debug
        elif level == Reporter.INFO_LEVEL:
            logger = self.logger.info
        elif level == Reporter.WARNING_LEVEL:
            logger = self.logger.warning
        elif level == Reporter.ERROR_LEVEL:
            logger = self.logger.error
        elif level == Reporter.SEVERE_LEVEL:
            logger = self.logger.fatal
        else:
            logger = self.logger.log

        logger(node.astext())

        raise SkipNode

    def visit_literal_block(self, node: literal_block) -> None:
        for c in tuple(node.children):
            node.remove(c)

        node += Text(node.rawsource.replace('"""', '\\"\\"\\"'))

        super().visit_literal_block(node)

    def unknown_visit(self, node: Node) -> None:
        self.logger.warning("Unknown node type: %s", node)

    def unknown_departure(self, node: Node) -> None:
        pass
