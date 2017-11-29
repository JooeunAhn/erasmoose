from .common import *


DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('DJANGO_DATABASE_NAME', 'erasmoose'),
        'USER': os.environ.get('DJANGO_DATABASE_USER', 'erasmoose'),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD', 'google'),
        'HOST': os.environ.get('DJANGO_DATABASE_HOST', '127.0.0.1'),
    }
}
