from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description_text = f.read()

# Get the long description from the README file
with open(path.join(here, 'LICENSE'), encoding='utf-8') as f:
    license_text = f.read()

setup(
    name='pykaa',
    version='0.5.dev2',
    packages=find_packages(),
    package_dir={'pykaa': 'pykaa'},
    url='https://github.com/AoLab/Kaa.py',
    license=license_text,
    long_description=long_description_text,
    author='Parham Alvani',
    author_email='parham.alvani@gmail.com',
    description='Kaa Administration REST Client',
    entry_points={
        'console_scripts': [
            'kaa.py = pykaa.cli:main'
        ]
    },
    package_data={
        'pykaa': ['server.data'],
    }, requires=['requests']
)
