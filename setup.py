#!/usr/bin/env python3

from setuptools import setup

import pathlib
import re

_THIS_DIR = pathlib.Path(__file__).resolve().parent
_LONG_DESCRIPTION = (_THIS_DIR / "README.md").read_text()


def get_version() -> str:
    VERSION_REGEX = re.compile(r"""__version__\s+=\s+['"]([0-9.]+)['"]""")
    source_code = pathlib.Path(__file__).with_name("unimorph.py")
    match = VERSION_REGEX.search(source_code.read_text())
    if match is None:
        raise ValueError("Couldn't find version number.")
    return match.group(1)


setup(
    name="unimorph",
    version=get_version(),
    description="Annotated morphology in the world's languages",
    long_description=_LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://unimorph.github.io/",
    author="Arya D. McCarthy",
    author_email="arya@jhu.edu",
    maintainer_email="arya@jhu.edu",
    python_requires=">=3.6",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3 :: Only",
    ],
    # What does your project relate to?
    keywords=[
        "NLP",
        "natural language processing",
        "evaluation",
        "computational linguistics",
        "morphology",
    ],
    py_modules=["unimorph"],
    install_requires=["pandas"],
    extras_require={},
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={"console_scripts": ["unimorph = unimorph:main"]},
)
