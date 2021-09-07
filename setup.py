from setuptools import find_namespace_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bpystubgen",
    version="0.1.1",
    author="Xavier Cho",
    author_email="mysticfallband@gmail.com",
    description="A utility to generate Python API stubs from documentation files in reStructuredText format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mysticfall/bpystubgen",
    packages=["bpystubgen"],
    install_requires=["docutils==0.17.1", "sphinxcontrib-restbuilder==0.3", "black==21.8b0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ]
)
