from setuptools import setup, find_packages

setup(
    name='selfhash',
    version='0.1',
    packages=find_packages(),
    author='Your Name',
    author_email='your.email@example.com',
    description='A package to hash the script and verify.',
    long_description=open('README.md').read(),
    url='https://github.com/yourusername/selfhash',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
)
