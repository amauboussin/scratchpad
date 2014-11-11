__author__ = 'Andrew'



# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'scratchpad',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',   # Not used with sqlite3.
        'HOST': '127.0.0.1',                           # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                       # Set to empty string for default. Not used with sqlite3.
    }
}

Debug = True


try:
    from local_settings import *
except ImportError:
    pass