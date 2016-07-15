# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    ptest_args = []

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run(self):
        import pytest
        pytest.main(self.pytest_args)

setup(
    name='hoge',
    version='0.1',
    description='test app',
    author='Magichan',
    author_email='nabe.dev@gmail.com',
    packages=find_packages(exclude=["*.tests"]),
    zip_safe=False,
    install_requires=['wheel'],
    extras_require={
        'test': ['pytest-cov',
                 'pytest-pep8',
                 'coverage',
                 'pep8',
                 'pytest'],
        'docs': ['sphinx'],
    },
    cmdclass={'test': PyTest},
)
