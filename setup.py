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
    name='I18.20',
    version='1.0.dev1',
    packages=find_packages(),
    url='https://github.com/AoLab/I1820',
    description="The IoT Middleware",
    license=license_text,
    long_description=long_description_text,
    author='Parham Alvani',
    author_email='parham.alvani@gmail.com',
)
