#!/usr/bin/env python
from setuptools import setup, find_packages, Command
from setuptools.command.install import install
from setuptools.command.develop import develop
import sys

packages = find_packages()
version_str = '0.9.0'

if sys.version_info.major < 3:
    print("The wiki_zh_vec code can only run in Python 3.")
    sys.exit(1)


setup(
    name = 'wiki_zh_vec',
    version = version_str,
    description = 'word2vec and glove to train Chinese wiki data',
    author = "June Shen",
    author_email = 'longsonofgod@gmail.com',
    packages=packages,
    include_package_data=True,
    exclude_package_data={'wiki_zh_vec': ['tmp', 'data']},
    install_requires=[
        'snakemake', 'click','jieba','gensim'
    ],
    license = 'Apache License 2.0',
    keywords=['wiki', 'Chinese','word2vec','glove'],
    entry_points = {
        'console_scripts': [
            'wiki_zh_vec = cli:cli'
        ]
    }
)
