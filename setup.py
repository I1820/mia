from distutils.core import setup

setup(
    name='Kaa.py',
    version='0.5.dev1',
    packages=['kaa', 'kaa.cli', 'kaa.rest', 'kaa.domain'],
    url='https://github.com/AoLab/Kaa.py',
    license='LICENSE',
    author='Parham Alvani',
    author_email='parham.alvani@gmail.com',
    description='Kaa Administration REST Client',
    scripts=['scripts/kaa']
)
