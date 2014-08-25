from os.path import abspath, basename, dirname, join, normpath
from sys import path

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DBPATH = join(DBDIR,"membamanpg")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'membaman', 
        'USER': 'membaman_dba',
        'PASSWORD': 'membaman_dba!2014',
        'HOST': 'localhost',   
        'PORT': '',  
    }
}
