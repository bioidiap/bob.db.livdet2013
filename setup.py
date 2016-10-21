#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

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
    description='LivDet 2013 Fingerprint database access for Bob',
    url='https://gitlab.idiap.ch/bob/bob.db.livdet2013',
    license='BSD',
    author='David Yambay',
    author_email='yambayda@gmail.com',
    maintainer='Andre Anjos',
    maintainer_email='andre.anjos@idiap.ch',
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
      'Framework :: Bob',
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering',
      'Topic :: Database :: Front-Ends',
      ],
)
