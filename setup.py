#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='graphite-dashboard',
      version = '0.1',
      description = 'CLI for export\import graphite dashboards',
      author = 'Alexey Dubkov',
      author_email = 'alexey.dubkov@gmail.com',
      url = 'https://github.com/blacked/graphite-dashboard',
      install_requires = ["argparse"],
      scripts = ['graphite-dashboard'],
      packages = find_packages(),
     )
