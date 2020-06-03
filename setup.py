from setuptools import setup
from os import path

version='0.0.1'
current = path.abspath(path.dirname(__file__))
# Getting long description
with open(path.join(current, 'README.md'), 'r') as f:
    readme = f.read()

setup(
    name='fulk',
    version=version,
    author='Boris Kayi',
    author_email='boriskayienzo@gmail.com',
    description='A bulk file renaming tool',
    long_description=readme,
    python_requires= '>=3.6',
    install_requires=[
        'Click',
        'colorama'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points='''
    [console_scripts]
    fulk=fulk:main
    ''',
)