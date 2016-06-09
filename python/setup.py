#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# with open(path.join(here, 'VERSION')) as version_file:
#   version = version_file.read().strip()
long_description = "Datajoint schema for EM anatomical data. "


setup(
    name='EM',
    version='0.1.0.dev1',
    description="Datajoint schema for EM anatomical data.",
    long_description=long_description,
    author='Fabian Sinz',
    author_email='sinz@bcm.edu',
    license="MIT",
    url='https://github.com/cajal/EM',
    keywords='data organization',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['datajoint'],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
    ],
)
