from setuptools import setup, find_packages

setup(
    name='django-hermes',
    version='1.2.2',
    author='Chris Pickett',
    author_email='chris.pickett@gmail.com',
    packages=find_packages(),
    url='https://github.com/bunchesofdonald/django-hermes',
    license='MIT',
    long_description=open('README.rst').read(),
    description='A light-weight blogging app for Django.',
)
