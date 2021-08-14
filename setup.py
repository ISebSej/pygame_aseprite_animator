#!/usr/bin/env python
# encoding: utf-8
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository pypi dist/*

from setuptools import setup

setup(
    name = "pygame_aseprite_animation",
    version="0.0.1",
    description="Package that allows you to import and use .ase and .aseprite files in pygame",
    author="Besmir Sejdijaj",
    author_email="b.sejdijaj@hotmail.com",
    py_modules = ["pygame_aseprite_animation"]
)