==============================================================
DjangoCMS OIDC (OpenID Connect) plugins for Aldryn form fields
==============================================================

Plugins for post a data hangovered from OpenID provider, based on plugins `DjangoCMS OIDC <https://github.com/CZ-NIC/djangocms-oidc/>`_.


Installation
============

.. code-block:: shell

    $ pip install djangocms-oidc-form-fields



Add settings to settings.py
---------------------------

Start by making the following changes to your ``settings.py`` file.

.. code-block:: python

   # Add 'mozilla_django_oidc' and 'djangocms_oidc' to INSTALLED_APPS
   INSTALLED_APPS = (
       # ...
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
    $ pip install git+https://github.com/CZ-NIC/djangocms-oidc-form-fields@28406-create-plugins

Create CMS testing site and go to the main project folder:

.. code-block:: shell

    $ djangocms mysite
    $ cd mysite

Modify settings and urls:

.. code-block:: diff

    --- mysite/mysite/settings.py
    +++ mysite/mysite/settings.py
    @@ -68,6 +68,15 @@
        },
    ]

    +AUTHENTICATION_BACKENDS = [
    +    'django.contrib.auth.backends.ModelBackend',
    +    'djangocms_oidc.auth.DjangocmsOIDCAuthenticationBackend',
    +]
    +
    +# Define OIDC classes
    +OIDC_AUTHENTICATE_CLASS = "djangocms_oidc.views.DjangocmsOIDCAuthenticationRequestView"
    +OIDC_CALLBACK_CLASS = "djangocms_oidc.views.DjangocmsOIDCAuthenticationCallbackView"
    +
    # Internationalization
    # https://docs.djangoproject.com/en/2.2/topics/i18n/

    @@ -136,6 +145,8 @@
        'cms.middleware.page.CurrentPageMiddleware',
        'cms.middleware.toolbar.ToolbarMiddleware',
        'cms.middleware.language.LanguageCookieMiddleware',
    +    'djangocms_oidc.middleware.OIDCSessionRefresh',
    ]

    INSTALLED_APPS = [
    @@ -178,6 +189,9 @@
        'djangocms_snippet',
        'djangocms_googlemap',
        'djangocms_video',
    +    'mozilla_django_oidc',  # place after auth (django.contrib.auth)
    +    'djangocms_oidc',
    +    'aldryn_forms',
    +    'djangocms_oidc_form_fields',
        'mysite'
    ]

    --- mysite/mysite/urls.py
    +++ mysite/mysite/urls.py
    @@ -15,6 +15,8 @@
    urlpatterns = [
        url(r'^sitemap\.xml$', sitemap,
            {'sitemaps': {'cmspages': CMSSitemap}}),
    +    url(r'^oidc/', include('mozilla_django_oidc.urls')),
    +    url(r'^djangocms-oidc/', include('djangocms_oidc.urls')),
    ]


Migrage new installed plugins:

.. code-block:: shell

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
