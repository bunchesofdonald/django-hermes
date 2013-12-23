=============
django-hermes
=============

A light-weight blogging app for Django.

Installation
============

Download
--------
::

    pip install django-hermes

Add To Installed Apps
---------------------
In your django settings file, add hermes to your INSTALLED_APPS::

    INSTALLED_APPS = (
        ...
        'hermes',
        ...
    )

Setup URLs
----------
Include hermes.urls in your ROOT_URLCONF::

    url(r'^blog/', include('hermes.urls')),


Create Templates
----------------
Hermes expects three templates:

1. hermes/post_list.html
2. hermes/post_detail.html
3. hermes/random_post_list.html


TODO
====
1. Create Sphinx Documentation

