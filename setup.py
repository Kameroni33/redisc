# -*- coding: utf-8 -*-
from Cython.Build import cythonize
from setuptools import setup
from setuptools.extension import Extension

short_description = 'A high performance Redis client implemented in Cython for realtime linux applications.'

with open('README.rst', 'r') as file:
    long_description = file.read()

ext_modules = [
    Extension('redisc.base', ['src/redisc/base.pyx']),
    Extension('redisc.pool', ['src/redisc/pool.pyx']),
]

setup(
    name='redisc',
    version='1.0.0',
    description=short_description,
    long_description=long_description,
    url='https://github.com/Kameroni33/redisc',
    ext_modules=cythonize(ext_modules),
    zip_safe=False,
)
