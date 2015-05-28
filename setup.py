#!/usr/bin/env python

from setuptools import setup

setup(
    name='pykarten',
    version='0.01',
    description='Flashcard generator web app',
    author='Willian Paixao',
    author_email='willian@ufpa.br',
    url='http://python-pykarten.rhcloud.com/',
    install_requires=['django==1.8', 'django-filter', 'django-zurb-foundation',
        'fabric', 'psycopg2'],
    license='GPLv3',
)
