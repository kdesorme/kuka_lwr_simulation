#!/usr/bin/eny python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['lasa_to_iai_parser'],
    package_dir={'': 'scripts'}
)

setup(**d)
