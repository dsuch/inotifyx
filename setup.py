#!/usr/bin/env python

# Author: Forest Bond
# This file is in the public domain.

import os, sys
from distutils.core import Extension


sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from setuptools import setup

setup(
  name = 'inotifyx',
  distinfo_module = 'inotifyx.distinfo',
  version = '0.2.2',
  description = 'Simple Linux inotify bindings',
  author = 'Forest Bond',
  author_email = 'forest@forestbond.com',
  url = 'https://launchpad.net/inotifyx/',
  packages = ['inotifyx'],
  ext_modules = [
    Extension(
      'inotifyx.binding',
      sources = [os.path.join('inotifyx', 'binding.c')],
    ),
  ],
)
