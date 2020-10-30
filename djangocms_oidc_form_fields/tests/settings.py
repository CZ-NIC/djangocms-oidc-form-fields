SECRET_KEY = "secret"

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Django CMS
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'easy_thumbnails',
    # dependencies
    'mozilla_django_oidc',
    'django_countries',
    'filer',
    'aldryn_forms',
    # the project
    'djangocms_oidc',
    'djangocms_oidc_form_fields',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'djangocms_oidc.auth.DjangocmsOIDCAuthenticationBackend',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'djangocms_oidc.middleware.OIDCSessionRefresh',
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

CMS_TEMPLATES = (
    ('test_content_plugin.html', 'Test content'),
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "tests",
    }
}

TIME_ZONE = "UTC"
USE_TZ = True

LANGUAGE_CODE = "en"
LANGUAGES = [
    ('en', 'English'),
    ('cs', 'Czech'),
]

SITE_ID = 1
# ROOT_URLCONF = 'djangocms_oidc.tests.urls'

OIDC_AUTHENTICATE_CLASS = "djangocms_oidc.views.DjangocmsOIDCAuthenticationRequestView"
OIDC_CALLBACK_CLASS = "djangocms_oidc.views.DjangocmsOIDCAuthenticationCallbackView"
