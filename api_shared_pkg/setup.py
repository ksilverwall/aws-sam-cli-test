#!/usr/bin/env python
# Learn more: https://github.com/kennethreitz/setup.py
from setuptools import setup, find_packages

PACKAGE_NAME = 'api_shared'

packages = [
    PACKAGE_NAME,
]

setup(
    name=PACKAGE_NAME,
    version="1.0.0",
    description="api shared package",
    packages=packages,
    package_data={
        PACKAGE_NAME: ['py.typed'],
    },
    python_requires=">=3.8",
    install_requires=[
    ],
    zip_safe=False,
)
