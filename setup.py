#!/usr/bin/env python

import os
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


README = read('README.rst')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests', '-s']
        self.test_suite = True

    def run_tests(self):
        import pytest
        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='skip-django-choice-enumfields',
    version='1.1.3.2',
    author='HZDG, Lubos Matl',
    author_email='matllubos@gmail.com',
    description='Real Python Enums for Django.',
    license='MIT',
    url='https://github.com/skip-pay/django-choice-enumfields',
    long_description=README,
    packages=find_packages(exclude=['tests*']),
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
    ],
    tests_require=[
        'pytest-django',
        'Django',
        'djangorestframework',
        'pytz',
    ],
    cmdclass={'test': PyTest},
)
