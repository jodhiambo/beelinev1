import os
# from decouple import config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from django.contrib.messages import constants as messages

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY')
# SECRET_KEY= config('SECRET_KEY')
SECRET_KEY = '_m&h*ghq^_8&#0#0n=pnyrf9%^z&fv$k=**v9(96bfrw7nv*+@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# APPEND_SLASH = False
# CSRF_COOKIE_SECURE = True

# SESSION_COOKIE_SECURE = True
# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'userprofiles.apps.UserprofilesConfig',
    'mainapp.apps.MainappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news.apps.NewsConfig',
    'crispy_forms',
    'multiselectfield',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'ckeditor',
    'ckeditor_uploader',
    'imagekit',
    'tinymce',
    'corsheaders',
    'sorl.thumbnail',
    'newsletter',
    'graphene_django'
]

GRAPHENE = {
    'SCHEMA': 'mainapp.schema.schema'
}


AUTH_USER_MODEL = 'users.CustomUser'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:8080",
# ]
# CORS_ALLOW_METHODS = [
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# ]
# CORS_ALLOW_HEADERS = [
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# ]
APPEND_SLASH = False
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'challengegov.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'users/templates'),
            os.path.join(BASE_DIR, 'templates/account'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request'
            ],
        },
    },
]

WSGI_APPLICATION = 'challengegov.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': 'challengegov',
        # 'USER': 'freddy',
        # 'PASSWORD': 'voldermort',
        # 'HOST': 'localhost',
        # 'PORT':5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



# # Amount of seconds to wait between each email. Here 100ms is used.
# NEWSLETTER_EMAIL_DELAY = 0.3
#
# # Amount of seconds to wait between each batch. Here one minute is used.
# NEWSLETTER_BATCH_DELAY = 60
#
# # Number of emails in one batch
# NEWSLETTER_BATCH_SIZE = 100
#
#
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )
#
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#
# #SMTP Configuration
#
# # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = config('EMAIL_PORT', cast=int)
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL= False
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
#
#
# NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"
# NEWSLETTER_CONFIRM_EMAIL = False


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
SITE_ID = 1

STATIC_URL = '/static/'
# STATIC_ROOT = '/home/beeline/myproject/challengegov/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CKEditor SETTINGS
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
        'extraPlugins': ','.join(
            ['codesnippet',
             'uploadimage',
             'uploadwidget',
             'widget',
             'dialog', ]),
        'allowedContent': True,
        'height': '250px',
        'width': '66%',
        'styles': {'font-family':'#(family)'},
        'overides': [{ 'element': 'font', 'attributes': {'face': 'null'}}]


    },
}

CKEDITOR_IMAGE_BACKEND = 'pillow'
# ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.CustomUserCreationForm'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_LOGOUT_ON_GET = True
LOGIN_REDIRECT_URL = 'mainapp:homepage'

TINYMCE_FILEBROWSER = True
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace,image,link,lists",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
