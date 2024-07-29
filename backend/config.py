import os

from environs import Env

DOTENV_PATH = os.path.join(os.path.dirname(__file__), os.pardir, '.env')


env = Env()
env.read_env(path=DOTENV_PATH)

# Django settings
DEBUG = env.bool('DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY', 'some_secret_key')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])
ALLOWED_ORIGINS = env('ALLOWED_ORIGINS', '*')
ALLOW_ALL_ORIGINS = env.bool('ALLOW_ALL_ORIGINS', False)


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('MYSQL_DATABASE'),
        'USER': env('MYSQL_USER'),
        'PASSWORD': env('MYSQL_PASSWORD'),
        'HOST': env('MYSQL_HOST'),
        'PORT': env('MYSQL_PORT'),
    }
}