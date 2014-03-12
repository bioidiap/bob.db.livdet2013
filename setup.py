#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Sex 10 Ago 2012 14:22:33 CEST

from setuptools import setup, find_packages

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    name='xbob.db.livdet2013',
    version='1.0',
    description='LivDet 2013 Fingerprint database access',
    url='https://github.com/dyambay/xbob.db.livdet2013',
    license='GPLv3',
    author='David Yambay',
    author_email='yambayda@gmail.com',
    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
      'setuptools',
      'six',  # py2/3 compatibility library
      'bob',  # base signal proc./machine learning library
    ],

    namespace_packages = [
      'xbob',
      'xbob.db',
      ],

    entry_points={

      # declare database to bob
      'bob.db': [
        'livdet2013 = xbob.db.livdet2013.driver:Interface',
        ],

      # declare tests to bob
      'bob.test': [
        'livdet2013 = xbob.db.livdet2013.test:livdet2013DatabaseTest',
        ],

      },

    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering',
      'Topic :: Database :: Front-Ends',
      ],
)
