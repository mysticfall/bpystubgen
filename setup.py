from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bpystubgen",
    version="0.2.2",
    author="Xavier Cho",
    author_email="mysticfallband@gmail.com",
    description="A utility to generate Python API stubs from documentation files in reStructuredText format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mysticfall/bpystubgen",
    packages=["bpystubgen"],
    package_data={"bpystubgen": ["patches/*.txt", "patches/*.rst", "patches/__init__.py"]},
    install_requires=["docutils==0.17.1", "sphinxcontrib-restbuilder==0.3"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ]
)
