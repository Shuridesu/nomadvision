import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'django-insecure-6k8_j+geg42g-n^lr5^)=#d70@(nj)an=&tcv#ji*$998&!8m#' 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True