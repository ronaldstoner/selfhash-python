#!/usr/bin/python
# Hash: 193dfdda9e08fb513338a76bd17dacf8eb80e6a0fb8cef90bb838466e073f78f

"""SelfHash setup.py file package metadata"""

from setuptools import setup, find_packages

setup(
    name='selfhash',
    version='0.1.1',
    packages=find_packages(),
    author='Ron Stoner',
    author_email='ron@stoner.com',
    description='A package to self hash and verify a python script',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    url='https://github.com/ronaldstoner/selfhash-python',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
)
