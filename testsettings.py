DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'hermes',
)

SECRET_KEY = 'abcde12345'

USE_TZ = True

ROOT_URLCONF = 'hermes.urls'
MIDDLEWARE_CLASSES = ()
