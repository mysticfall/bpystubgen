![pytest](https://github.com/mysticfall/bpystubgen/workflows/pytest/badge.svg)
[![PyPI version](https://badge.fury.io/py/bpystubgen.svg)](https://badge.fury.io/py/bpystubgen)

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
   for Blender. But _bpystubgen_ can do it under a minute (1,593 source documents).
 * The generated stub modules preserve most of the source documentation, so you can use them 
   as a manual as well.
 * It generates _PEP-561_ compliant stub modules, so it's safe to include them in your runtime 
   module path.
 * Along with its fast execution speed, the project also provides well-organised API and test 
   suites to make it easier to fix bugs or improve the output quality. 

## Screenshots ##

Auto-completion at work in PyCharm:
![Screenshot in PyCharm](images/screenshot-pycharm.png?raw=true "Screenshot in PyCharm")

Pop-up documentation support in VSCode:
![Screenshot in VSCode](images/screenshot-vscode.png?raw=true "Screenshot in VSCode")

## Installation ##

The library can be installed using `pip` as follows:
```bash
$ pip install bpystubgen
```

## Usage ##

### Generating Stubs ###

If you want to generate the API stubs yourself, you can use `bpystubgen` module which 
can be invoked with the following options:

```bash
$ python -m bpystubgen -h

usage: bpystubgen [-h] [--verbose] [--quiet] input output

Generate Python API stubs from Blender documentation.

positional arguments:
  input       Source directory where *.rst files are located
  output      Output directory where generated modules will be saved

optional arguments:
  -h, --help  show this help message and exit
  --verbose   Print debug messages
  --quiet     Print only error messages
```

### Using Stubs ###

If you just want to use the API stubs, you can install them from PyPI without having to generate 
them yourself.

There are two variants of the API stubs, one for Blender and the other for UPBGE. For Blender, 
you can install `blender-stubs` module with appropriate version qualifier as follows: 

```bash
$ pip install blender-stubs==2.93.*
```
This will install the latest module for Blender 2.93, and for now stubs are provided for Blender 
2.80 and onwards. You can also specify the next unreleased version as `3.0.*` to get the latest 
snapshot of the module.

As for UPBGE, stubs are available for the upcoming 0.3 release, which you can install as follows:

```bash
$ pip install upbge-stubs==0.3.*
```

You can also install it using `Pipenv`. Note that it is required to set `allow_preleases` option 
in case the target application has no stable release (i.e. UPBGE 0.3 branch). You can use the 
following content as a template for your `Pipfile`:

```toml
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[packages]
"upbge-stubs" = "==0.3.*"

[requires]
python_version = "3.9"

[pipenv]
allow_prereleases = true
```
Also, it would be more correct to use `[dev-packages]` instead of `[packages]`, in which 
case you can install or update the stubs using the `-d` flag like `pipenv update -d`.  

## License ##

This project is provided under the terms of _[GNU General Public License v3 (GPL3)](LICENSE)_.
