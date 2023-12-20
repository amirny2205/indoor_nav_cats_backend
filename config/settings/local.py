from .base import *
import environ

env.read_env(env.str('ENV_PATH', '.env_local'), overwrite=True)

SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'incdb',
        'USER': 'catsuser',
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
