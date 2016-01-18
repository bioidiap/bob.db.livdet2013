#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# David Yambay <yambayda@gmail.com>
# Mar 14 2014 14:32

from setuptools import setup, find_packages, dist
dist.Distribution(dict(setup_requires=['bob.extension']))

from bob.extension.utils import load_requirements
install_requires = load_requirements()

# Define package version
version = open("version.txt").read().rstrip()

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    name='bob.db.livdet2013',
    version=version,
    description='LivDet 2013 Fingerprint database access',
    url='https://github.com/bioidiap/bob.db.livdet2013',
    license='GPLv3',
    author='David Yambay',
    author_email='yambayda@gmail.com',
    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires=install_requires,

    entry_points={
      'bob.db': [
        'livdet2013 = bob.db.livdet2013.driver:Interface',
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
