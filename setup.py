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

import ast
import os
import re

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'archerysec_cli', '__init__.py'), 'rb') as f:
    version = str(ast.literal_eval(re.search(r'__version__\s*=\s*(.*)', f.read().decode('utf-8')).group(1)))

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='archerysec_cli',
    version=version,
    description='A commandline tool that wraps'
                ' the Archerysec REST API for'
                ' controlling Archery and executing '
                'quick, targeted scans.',
    long_description=long_description,
    url='https://github.com/archerysec/archerysec-cli.git',
    author='Anand Tiwari',
    author_email=' ',
    license=' ',
    packages=[
        'archerysec_cli',
    ],
    install_requires=[
        'certifi',
        'chardet',
        'Click',
        'idna',
        'pyArchery',
        'requests',
        'urllib3',
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
        ],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'archerysec-cli=archerysec_cli.cli:main',
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
