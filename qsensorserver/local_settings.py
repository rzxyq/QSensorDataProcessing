# Local PostGreSQL database on Joe Antonakakis's (jma353) commercial 


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'qsensorserver_db', 
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}




# For local debugging 
DEBUG = True 