#!/usr/bin/env python
from importlib.metadata import entry_points
from setuptools import find_packages
from setuptools import setup

setup(name='obesity',
      version='1.0',
      description='Python',
      author='Thejas Devadiga',
      author_email='mrdevaidgatj@gmail.com',
      url='https://github.com/ThejasDevadiga',
      packages=find_packages(),
      entry_points={
          'console_scripts':
['model-cli = model.main:main',]  ,    },
     )
