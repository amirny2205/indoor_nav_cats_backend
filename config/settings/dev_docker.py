from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'incdb',
        'USER': 'catsuser',
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': 'indoor_nav_cats_backend-db-1',
        'PORT': '5432',
    }
}

