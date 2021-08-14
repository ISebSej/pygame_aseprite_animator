#!/usr/bin/env python
# encoding: utf-8
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository pypi dist/*

from setuptools import setup

setup(
    name = "pygame_aseprite_animation",
    version="0.0.7",
    description="Package that allows you to import and use .ase and .aseprite files in pygame",
    author="Besmir Sejdijaj",
    author_email="b.sejdijaj@hotmail.com",
    py_modules = ["pygame_aseprite_animation"],
    long_description='https://github.com/ISebSej/pygame_aseprite_animator',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Games/Entertainment",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: pygame",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "src"},
    packages=['pygame_aseprite_animation', 'py_aseprite']
)