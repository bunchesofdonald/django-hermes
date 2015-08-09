from setuptools import setup, find_packages

setup(
    author='Chris Pickett',
    author_email='chris.pickett@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
    ],
    description='A light-weight blogging app for Django.',
    license='MIT',
    long_description=open('README.rst').read(),
    name='django-hermes',
    packages=find_packages(),
    url='https://github.com/bunchesofdonald/django-hermes',
    version='1.4.0',
)
