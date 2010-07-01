# Django settings for gospel_preaching project.

try:
    from local_settings import *
except ImportError:
    pass

#DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('David Nichols', 'dnichols@dn-webdesign.dnsalias.com'),
)

MANAGERS = ADMINS

#DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = ''             # Or path to database file if using sqlite3.
#DATABASE_USER = ''             # Not used with sqlite3.
#DATABASE_PASSWORD = ''         # Not used with sqlite3.
#DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = '/media/'

FILE_UPLOAD_PERMISSIONS = 0644

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
#SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "gospel_preaching.master.context_processors.apps",
    "gospel_preaching.master.context_processors.email",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'facebook.djangofb.FacebookMiddleware',
#    'socialregistration.middleware.FacebookMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'gospel_preaching.urls'

#TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#	'/home/bluevan/python/projects/gospel_preaching/templates'
#)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'gospel_preaching.articles',
    'gospel_preaching.nt_reading',
    'gospel_preaching.helpers',
    'gospel_preaching.questions',
#    'gospel_preaching.news',
    'gospel_preaching.master',
    'django.contrib.admin',
#    'gospel_preaching.simple_orders',
    'gospel_preaching.accounts',
#    'socialregistration',
    'django.contrib.sites',
    'django.contrib.flatpages',
)

#AUTH_PROFILE_MODULE = 'user_profiles.Profile'

ARTICLES_PER_PAGE = 20

QUESTIONS_PER_PAGE = 20

PRODUCTS_PER_PAGE = 10

AUTHOR_PARTIAL_NUM = 5

TAG_PARTIAL_NUM = 10

USERS_PER_PAGE = 20

#FACEBOOK_API_KEY = ''

#FACEBOOK_SECRET_KEY = ''

#AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', 'socialregistration.auth.FacebookAuth')
