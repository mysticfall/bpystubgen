import logging
import sys
from argparse import ArgumentParser
from pathlib import Path

from bpystubgen.generator import generate

parser = ArgumentParser(
    prog="bpystubgen",
    description="Generate Python API stubs from Blender's documentation.")

parser.add_argument("input", type=str,
                    help="Source directory where *.rst files are located")
parser.add_argument("output", type=str, default=".",
                    help="Output directory where generated modules will be saved")
parser.add_argument("--format", default=False, action="store_true", help="Format generated source files")
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

generate(source, dest, args.format, log_level)
