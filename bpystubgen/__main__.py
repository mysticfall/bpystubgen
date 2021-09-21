import logging
import sys
import time
from argparse import ArgumentParser
from pathlib import Path

from docutils.frontend import OptionParser
from docutils.parsers.rst import Parser
from sphinx.application import Sphinx
from sphinxcontrib.builders.rst import RstBuilder

from bpystubgen.patches import blacklist
from bpystubgen.tasks import ModuleTask, ParserTask, Task
from bpystubgen.writer import StubWriter

parser = ArgumentParser(
    prog="bpystubgen",
    description="Generate Python API stubs from Blender's documentation.")

parser.add_argument("input", type=str,
                    help="Source directory where *.rst files are located")
parser.add_argument("output", type=str, default=".",
                    help="Output directory where generated modules will be saved")
parser.add_argument("--verbose", default=False, action="store_true", help="Print debug messages")
parser.add_argument("--quiet", default=False, action="store_true", help="Print only error messages")

args = parser.parse_args()

source = Path(args.input).expanduser()
dest = Path(args.output).expanduser()

if not source.is_dir():
    sys.exit(f"The specified input is not a valid directory: {source}")

if dest.exists():
    if dest.is_file():
        sys.exit(f"The specified output already exists but it's not a valid directory: {dest}")
else:
    dest.mkdir(parents=True)

if args.quiet:
    log_level = logging.WARNING
elif args.verbose:
    log_level = logging.DEBUG
else:
    log_level = logging.INFO

logging.basicConfig(level=log_level, format="[%(levelname)s] %(name)s - %(message)s")
logger = logging.getLogger("bpystubgen")

logger.info("Reading *.rst files from the source location: %s", source)

started = time.perf_counter()

root = Task.create(source)

# noinspection DuplicatedCode
components = (Parser,)

app = Sphinx(srcdir=".", confdir=None, outdir=str(dest), doctreedir=".", buildername="text")

settings = OptionParser(components=components).get_default_values()

settings.line_length_limit = 15000
settings.report_level = 5
settings.traceback = True
settings.env = app.env

builder = RstBuilder(app)
builder.config.rst_indent = 2

writer = StubWriter(builder)

total = len(tuple(root))
done = 0

for task in root:
    done += 1

    logger.info("Processing %s (%d of %d)", task.full_name, done, total)

    if task.full_name in blacklist:
        logger.info("Skipping blacklisted file: %s.", task)
        continue

    try:
        if isinstance(task, ParserTask):
            task.parse(settings, app.env)

        if isinstance(task, ModuleTask):
            task.generate(dest, writer)
    except BaseException as e:
        logger.error("Failed to process task: %s", task, exc_info=e)

elapsed = time.perf_counter() - started

logger.info("Finished processing %d entries in %d seconds.", total, elapsed)
