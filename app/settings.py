import environ


root = environ.Path(__file__) - 2
env = environ.Env()


BASE_DIR = root()

SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'app.urls'

DATABASES = {
    'default': env.db_url('DATABASE_URL'),
}

ELASTICSEARCH_HOSTS = [
    env.str('ELASTICSEARCH_HOST'),
]

INSTALLED_APPS = [
    'app',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'UNAUTHENTICATED_USER': None,
}
