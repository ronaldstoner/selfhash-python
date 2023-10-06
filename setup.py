from setuptools import setup, find_packages

setup(
    name='selfhash',
    version='0.1',
    packages=find_packages(),
    author='Ron Stoner',
    author_email='stoner.com',
    description='A package to self hash and verify a python script.',
    long_description=open('README.md').read(),
    url='https://github.com/ronaldstoner/selfhash-python',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
)
