from .settings import *


DATABASES['fias'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(PROJECT_PATH, 'fias.sqlite'),
}

FIAS_DATABASE_ALIAS = 'fias'
DATABASE_ROUTERS = ['fias.routers.FIASRouter']