#!/usr/bin/env python

from setuptools import setup, find_packages
from entry_points import entry_points

setup(
    name='pymdown-styles',
    version='1.0',
    packages=find_packages(exclude=["file_strip"]),
    entry_points=entry_points,
    zip_safe=True
)
