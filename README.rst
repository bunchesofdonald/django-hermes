.. image:: https://travis-ci.org/bunchesofdonald/django-hermes.svg?branch=master
    :target: https://travis-ci.org/bunchesofdonald/django-hermes

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

If you want to create your blog templates in a specific app directory (other than hermes), make sure that that app comes before hermes in your INSTALLED_APPS. Otherwise, Django will render the templates that are in the hermes app itself and not yours.


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
2. Support tagging
3. Annotations ala Medium?

