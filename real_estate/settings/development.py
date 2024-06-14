
from .base import *

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

