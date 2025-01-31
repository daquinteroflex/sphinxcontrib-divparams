#!/usr/bin/env python
import os
from setuptools import setup


def slurp(filename):
    """
    Return whole file contents as string. File is searched relative to
    directory where this `setup.py` is located.
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name                 = "divparams",
    version              = "0.0.7",
    packages             = ["sphinxcontrib", "sphinxcontrib.divparams"],
    namespace_packages   = ["sphinxcontrib"],
    package_dir          = {'': "src"},
    package_data         = {'sphinxcontrib.divparams': [
                                '_static/divparams.css',
                                '_templates/layout.html']},
    author               = "Pavel Kretov",
    author_email         = "firegurafiku@gmail.com",
    license              = "MIT",
    url                  = "https://github.com/sphinxcontrib-divparams",
    keywords             = ["helpers"],
    requires             = ["six"],
    description          = ("Converts parameter tables in HTML documentation "
                            "generated by Sphinx into <div>'s."),
    long_description     = slurp("README.rst"),
    classifiers          = ["Programming Language :: Python",
                            "Programming Language :: Python :: 2.6",
                            "Programming Language :: Python :: 2.7",
                            "Programming Language :: Python :: 3.3",
                            "Programming Language :: Python :: 3.4",
                            "Programming Language :: Python :: 3.5",
                            "Development Status :: 2 - Pre-Alpha",
                            "Topic :: Documentation",
                            "Intended Audience :: Developers",
                            "License :: OSI Approved :: MIT License",
                            "Operating System :: POSIX"])
