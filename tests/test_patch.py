import shutil
import tempfile
from pathlib import Path

from docutils.frontend import OptionParser, Values
from docutils.parsers import Parser
from pytest import fixture
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment

from bpystubgen import Module, patches
# noinspection DuplicatedCode
from bpystubgen.nodes import Data


# noinspection DuplicatedCode
@fixture
def env() -> BuildEnvironment:
    dest_path = Path(tempfile.tempdir) / "bpystubgen-test"
    app = Sphinx(srcdir=".", confdir=None, outdir=str(dest_path), doctreedir=".", buildername="text")

    yield app.env

    shutil.rmtree(dest_path)


@fixture
def settings(env: BuildEnvironment) -> Values:
    components = (Parser,)
    settings = OptionParser(components=components).get_default_values()

    settings.line_length_limit = 15000
    settings.report_level = 5
    settings.traceback = True
    settings.env = env
    settings.pep_references = None
    settings.rfc_references = None

    return settings


def test_patch(settings: Values, env: BuildEnvironment):
    module = Module(name="bgl")

    module += Data(name="existing1", type="bool")
    module += Data(name="GL_ACTIVE_TEXTURE", type="str")
    module += Data(name="existing2", type="int")

    patches.apply(module.name, module, settings, env)

    members = module.members

    assert len(members) == 799

    assert members[0].name == "existing1"
    assert members[0].type == "bool"

    assert members[1].name == "GL_ACTIVE_TEXTURE"
    assert members[1].type == "int"

    assert members[2].name == "existing2"
    assert members[2].type == "int"

    assert members[3].name == "GL_ACTIVE_ATTRIBUTES"
    assert members[3].type == "int"

    assert members[4].name == "GL_ACTIVE_ATTRIBUTE_MAX_LENGTH"
    assert members[4].type == "int"

    assert members[5].name == "GL_ACTIVE_UNIFORMS"
    assert members[5].type == "int"


def test_patch_noop(settings: Values, env: BuildEnvironment):
    module = Module(name="dummy")

    module += Data(name="existing1", type="bool")
    module += Data(name="existing2", type="int")

    patches.apply(module.name, module, settings, env)

    assert len(module.members) == 2
