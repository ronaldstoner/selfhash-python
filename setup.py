#!/usr/bin/python
# Hash: 8b74bf84000993da1f0fbb10e97197c7443b978b43edd1fa5f3957e729e49718
# Author: Ron Stoner
# Github: ronaldstoner
# Website: stoner.com

"""SelfHash setup.py file package metadata"""

from setuptools import setup, find_packages

setup(
    name='selfhash',
    version='0.1.2',
    packages=find_packages(),
    author='Ron Stoner',
    author_email='ron@stoner.com',
    description='A package to self hash and verify a python script',
    long_description_content_type='text/markdown; charset=UTF-8',
    long_description=open('README.md').read(),
    url='https://github.com/ronaldstoner/selfhash-python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='self hash verify python script integrity checksum ',
)
