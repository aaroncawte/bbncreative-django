"""
Django settings for bbncreative project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from .base import *

from bbncreative import secrets


# bbncreative specific settings
NUM_TOP_PROJECTS = 3
NUM_TOP_FEEDS = 3

DEBUG = True

# Application definition

LOCKDOWN_ENABLED = False
LOCKDOWN_PASSWORDS = (secrets.LOCKDOWN_PASSWORD, '')


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Uploaded Content (Images, etc.)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = "/media/"
