from .base import *
from pathlib import Path
from .secret import SECRET_KEY, RECAPTCHA_SECRET_KEY

DEBUG = False

# Show captchas on forms
CAPTCHA = True

# Autofill form entries
AUTOFILL = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'www-01.abtech.org', '128.2.24.195',
                 'www-staging.abtech.org']

ADMINS = [('Robert Maratos', 'rmaratos@andrew.cmu.edu')]

INSTALLED_APPS += ('website',
                   'django_markdown',
                   'bootstrap3',
                   'captcha')

PROJECT_DIR = (Path(__file__) / "../../..").resolve()

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'relay.andrew.cmu.edu'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

EVENT_EMAIL = 'abtech+chair@andrew.cmu.edu'
JOIN_EMAIL = 'abtech+chair@andrew.cmu.edu'

RECAPTCHA_SITE_KEY = '6LdvswQTAAAAAPhSuC25sVceWHEfpTIe3I0PuYnO'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows1.
    # Don't forget to use absolute paths, not relative paths.
    (PROJECT_DIR / "static/").resolve(),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            (PROJECT_DIR / "templates/").resolve(),
        ],
        'APP_DIRS': True,
    }
]
