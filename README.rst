.. image:: https://travis-ci.org/CZ-NIC/djangocms-oidc-form-fields.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/CZ-NIC/djangocms-oidc-form-fields

.. image:: https://codecov.io/gh/CZ-NIC/djangocms-oidc-form-fields/branch/master/graph/badge.svg
   :alt: Coverage
   :target: https://codecov.io/gh/CZ-NIC/djangocms-oidc-form-fields


==============================================================
DjangoCMS OIDC (OpenID Connect) plugins for Aldryn form fields
==============================================================

Plugins for post a data hangovered from OpenID provider, based on plugins `DjangoCMS OIDC <https://github.com/CZ-NIC/djangocms-oidc/>`_
and `Aldryn Forms version 5.0.1.2 <https://github.com/zbohm/aldryn-forms/tree/5.0.1.2>`_.


Installation
============

.. code-block:: shell

    $ pip install git+https://github.com/CZ-NIC/djangocms-oidc-form-fields



Add settings to settings.py
---------------------------

Start by making the following changes to your ``settings.py`` file.

.. code-block:: python

   # Add 'aldryn_forms' and 'djangocms_oidc_form_fields' to INSTALLED_APPS
   INSTALLED_APPS = (
       # ...
       'aldryn_forms',
       'djangocms_oidc_form_fields',
       # ...
   )



Example of installation
=======================

You can test in python virtual environment. This does not have any affest to your current python installation of packages.

Create python virtual environment and activate it:

.. code-block:: shell

    $ virtualenv --python=/usr/bin/python3 env
    $ source env/bin/activate

Install DjangoCMS and this projects:

.. code-block:: shell

    $ pip install djangocms-installer
    $ pip install git+https://github.com/CZ-NIC/djangocms-oidc-form-fields

Create CMS testing site and go to the main project folder:

.. code-block:: shell

    $ djangocms --django-version=2.2 --cms-version=3.7 mysite

Modify settings and urls with the `mysite-django-2.2.17.patch <accessoires/mysite-django-2.2.17.patch>`_:

.. code-block:: shell

    $ patch -p0 < accessoires/mysite-django-2.2.17.patch

Migrage new installed plugins:

.. code-block:: shell

    $ cd mysite
    $ python manage.py migrate


Run test server:

.. code-block:: shell

    $ python manage.py runserver


Usage in administration
=======================

These plugins are available to the editor in the administration:

  * OIDC Fields
  * OIDC Text
  * OIDC Textarea
  * OIDC Hidden
  * OIDC Email
  * OIDC EmailIntoFromField
  * OIDC Phone
  * OIDC Number
  * OIDC Boolean

License
-------

This software is licensed under the GNU GPL license. For more info check the LICENSE file.


More information
----------------

You can get the code from the `project site <https://github.com/CZ-NIC/djangocms-oidc-form-fields>`_.
