BPY Stub Generator
==================

A utility to generate Python [API stubs](https://www.python.org/dev/peps/pep-0561/) from 
documentation files in [_reStructuredText_](https://docutils.sourceforge.io/rst.html) format.  

## Introduction ##

The main usage of the program is to create Python API stubs from the documentation generated 
during the build process of [Blender](https://www.blender.org) or [UPBGE](https://upbge.org) 
so that an IDE can provide autocompletion support and type hints for relevant modules like 
`bpy` or `bge`.

There are already a number of tools created with a similar goal in mind, notably 
[fake-bpy-module](https://github.com/nutti/fake-bpy-module) which can be a good alternative 
to this project.

However, _bpystubgen_ has a few advantages over the others:

 * It's very fast - Some of those tools may take over an hour to generate the entire stubs 
   for Blender. But _bpystubgen_ can do it under 30 seconds (1,593 source documents).
 * The generated stub modules preserve most of the source documentation, so you can use them 
   as a manual as well.
 * It generates _PEP-561_ compliant stub modules, so it's safe to include them in your runtime 
   module path.
 * Along with its fast execution speed, the project also provides well-organised API and test 
   suites to make it easier to fix bugs or improve the output quality. 

## Usage ##

```bash
$ python -m bpystubgen -h

usage: bpystubgen [-h] [--debug] input output

Generate Python API stubs from Blender's documentation.

positional arguments:
  input       Source directory where *.rst files are located
  output      Output directory where generated modules will be saved

optional arguments:
  -h, --help  show this help message and exit
  --debug     Print debug messages
```

## Status ##

While mostly working as intended, it still has a few missing features which better be implemented 
before the official release. It will soon be published to the PyPi repository along with prebuilt 
stub modules for Blender and UPBGE.

## License ##

This project is provided under the terms of _[GNU General Public License v3 (GPL3)](LICENSE)_.
