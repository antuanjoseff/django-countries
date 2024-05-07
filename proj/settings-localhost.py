DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mobility_udg',
        'USER': 'postgres',
        'PASSWORD': 'p1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
} 

GDAL_LIBRARY_PATH = 'C:/OSGeo4W/bin/gdal303.dll'
GEOS_LIBRARY_PATH = 'C:/OSGeo4W/bin/geos_c.dll'

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    BASE_DIR / "static",
]