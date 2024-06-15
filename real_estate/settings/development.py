
from .base import *



EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "info@real-estate.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Rentify Estate"



DATABASES = {
    'default': {
        'ENGINE': env('DATABASE_ENGINE'),
        'NAME': os.path.join(BASE_DIR, env('DATABASE_NAME')),
    }
}


# Uncomment this section if using PostgreSQL
# DATABASES = {
#     'default': {
#         'ENGINE': env('DATABASE_ENGINE'),
#         'NAME': env('DATABASE_NAME'),
#         'USER': env('DATABASE_USER'),
#         'PASSWORD': env('DATABASE_PASSWORD'),
#         'HOST': env('DATABASE_HOST'),
#         'PORT': env('DATABASE_PORT', default='5432'),
#     }
# }

