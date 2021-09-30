#!/usr/bin/env python
# -*- coding: utf-8 -*-

__license__ = """
C#                   _
#    /\            | |
#   /  \   _ __ ___| |__   ___ _ __ _   _
#  / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
# / ____ \| | | (__| | | |  __/ |  | |_| |
# /_/    \_\_|  \___|_| |_|\___|_|   \__, |
#                                    __/ |
#                                   |___/
# Copyright (C) 2017-2018 ArcherySec
# This file is part of ArcherySec Project.
"""

from setuptools import (
    find_packages,
    setup,
)

import ast
import os
import re


from pathlib import Path

def read(rel_path):
    init = Path(__file__).resolve().parent / rel_path
    return init.read_text('utf-8', 'ignore')

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            return line.split('\'')[1]
    raise RuntimeError('Unable to find version string.')


with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='archerysec_cli',
    version=get_version('archerysec_cli/__init__.py'),
    description='A commandline tool that wraps'
                ' the Archerysec REST API for'
                ' controlling Archery and executing '
                'quick, targeted scans.',
    long_description=long_description,
    url='https://github.com/archerysec/archerysec-cli.git',
    author='Anand Tiwari',
    author_email=' ',
    license=' ',
    packages=find_packages(include=[
        'archerysec_cli', 'archerysec_cli.*',
    ]),
    install_requires=[
        'click==7.1.2',
        'docker==5.0.0',
        'idna==2.10',
        'jmespath==0.10.0',
        'python-dateutil==2.8.1',
        'PyYAML==5.4.1',
        'websocket-client==0.58.0',
        'wget==3.2',
    ],
    extras_require={
        'dev': [
            'coverage',
            'ddt',
            'mock',
            'pep8',
            'pylint',
            'pytest',
            'responses',
        ]
    },

    include_package_data=True,
    entry_points={
        'console_scripts': [
            'archerysec-cli=archerysec_cli.cli.cli:main',
        ],
    },
    test_suite='tests',
    classifiers=[
        'Topic :: Security',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
    ],
)
