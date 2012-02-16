DEBUG = True # Set to False for a production environment

ADMINS = (
    ('Admin', 'user@example.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

SITE_ID = 1

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    '/home/user/gospel-preaching/media',
)

# Turns the static media server on for the development environment.
# Set to False for the production environment.
STATIC_MEDIA_SERVER = False

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	''
)

#INSTALLED_APPS = (
#    'django.contrib.staticfiles',
#)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# Settings for the e-mail form on the admin pages.
ADMIN_EMAIL_FORM_URL = ''
ADMIN_EMAIL_REDIR_URL = ''
ADMIN_EMAIL_USER = ''
ADMIN_EMAIL_PASSWD = ''

# Settings for sending mail.
EMAIL_HOST = ""
EMAIL_PORT = 25
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
DEFAULT_FROM_EMAIL = ""
SERVER_EMAIL = "root@localhost"
EMAIL_SUBJECT_PREFIX = "[Django] "

# Cumulus cloud files settings
CUMULUS_USERNAME = ''
CUMULUS_API_KEY = ''
CUMULUS_CONTAINER = ''
CUMULUS_CNAMES = { 'http://c000000.r00.cf0.rackcdn.com': 'http://media.domain.tld' }
DEFAULT_FILE_STORAGE = 'cumulus.storage.CloudFilesStorage'

BOOKCLUB_ADMIN_EMAILS = ["user@example.com"]
BOOKCLUB_SUBJECT = ""
BOOKCLUB_REDIRECT = "/"
BOOKCLUB_STATUS_PAGE = ""
