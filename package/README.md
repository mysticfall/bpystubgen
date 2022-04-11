Blender / UPBGE API Stubs
=========================

This module provides type information for [Blender](https://www.blender.org) and 
[UPBGE](https://upbge.org)'s Python API, following the 
[PEP-561](https://www.python.org/dev/peps/pep-0561/) standard.

It was generated using [BPY Stub Generator](https://github.com/mysticfall/bpystubgen) which 
is also available on [PyPI](https://pypi.org/project/bpystubgen) as a separate module.

## Screenshots ##

Auto-completion at work in PyCharm:
![Screenshot in PyCharm](https://github.com/mysticfall/bpystubgen/raw/main/images/screenshot-pycharm.png?raw=true "Screenshot in PyCharm")

Pop-up documentation support in VSCode:
![Screenshot in VSCode](https://github.com/mysticfall/bpystubgen/raw/main/images/screenshot-vscode.png?raw=true "Screenshot in VSCode")

## Installation ##

There are two variants of the API stubs, one for Blender and the other for UPBGE. For Blender, 
you can install `blender-stubs` module with appropriate version qualifier as follows: 

```bash
$ pip install blender-stubs==3.1.27
```
This will install the latest module for Blender 2.93, and for now stubs are provided for Blender 
2.80 and onwards. You can also specify the next unreleased version as `3.1.*` to get the latest 
snapshot of the module:

```bash
$ pip install blender-stubs==3.2.*
```

A stub module for UPBGE 0.3, as well as pre-release versions for the master branch are also 
available on PyPI repository. For the stable version, you can install it as follows:  

```bash
$ pip install upbge-stubs==0.3.0.27
```

And for the latest snapshot, 

```bash
$ pip install upbge-stubs==0.3.1.*
```

You can also install the module using `Pipenv`. Note that it is required to set `allow_preleases` option 
in case you want to install a snapshot release (e.g. UPBGE 0.3.1.*).

You can use the following content as a template for your `Pipfile`:

```toml
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[packages]
"upbge-stubs" = "==0.3.1.*"

[requires]
python_version = "3.10"

[pipenv]
allow_prereleases = true
```
You may want to use `[dev-packages]` instead of `[packages]` as it's more appropriate to do so, 
in which case you can install or update the stubs using the `-d` flag like `pipenv update -d`.  

## License ##

This project is provided under the terms of 
[GNU General Public License v3 (GPL3)](https://github.com/mysticfall/bpystubgen/blob/main/LICENSE).
