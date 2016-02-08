#!/usr/bin/env python

from distutils.core import setup

setup(name='rsicalc',
      version='0.2',
      description='Relative Strength Index Calculator',
      author='Vivek Ayer',
      author_email='ayer@pobox.com',
      url='https://github.com/vsayer/rsicalc',
      license='BSD',
      install_requires=['yahoo_finance'],
      scripts=['bin/rsicalc'],
      )
