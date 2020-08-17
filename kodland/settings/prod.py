from kodland.settings.common import *

import dj_database_url
import os

SECRET_KEY = os.environ['SECRET_KEY']
SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = ['kodland-task.herokuapp.com']

DATABASES['default']['NAME'] = 'kodland_prod'
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(ssl_require=True)
