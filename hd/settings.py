
"""
Django settings for hd project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+2y6rm!n_$(mcz54b)*%x3uiqu1!4*84s0_#fo=ff6x(#$qz1+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'contries',
    'states',
    'jobs',
    'gunicorn',
    'profiles',
    'areas',
    'sorl.thumbnail',
    #'home',

)

TEMPLATE_CONTEXT_PROCESSORS = (

    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hd.urls'

WSGI_APPLICATION = 'hd.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = '/login/'


STATICFILES_FINDER = (
'django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#'django.contrib.staticfiles.finders.DefaultStorageFinder',

)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
#para centralizar los staticos en la carpeta media que se crea por si misma cuando se sube un archivo
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]+['media']) 
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]+['content']) 
MEDIA_URL = '/media/'

# Python Social Auth

SOCIAL_AUTH_PIPELINE = (
        'social.pipeline.social_auth.social_details',
        'social.pipeline.social_auth.social_uid',
        'social.pipeline.social_auth.auth_allowed',
        'social.pipeline.social_auth.social_user',
        'social.pipeline.user.get_username',
        'social.pipeline.user.create_user',
        'social.pipeline.social_auth.associate_user',
        'social.pipeline.social_auth.load_extra_data',
        'social.pipeline.user.user_details',
        'hd.pipeline.update_user_social_data',
        # 'profiles.pipeline.user_details'
    )

## Twitter
SOCIAL_AUTH_TWITTER_KEY = 'ijiNdRJtAl7lEJOArMLiPiGqx'
SOCIAL_AUTH_TWITTER_SECRET = 'Q5hz2lnAo9bcEdi0hZvY92aSupJXsfS5CIkuAuCB0IDp4FYRiI'

## Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '1486716481572110'
SOCIAL_AUTH_FACEBOOK_SECRET = '266b7fdea38675e9885a2cfed6d67649'
# SOCIAL_AUTH_FACEBOOK_APP_NAMESPACE = 'zacklogin'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email','public_profile']
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

#SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'picture'}
# FACEBOOK_EXTENDED_PERMISSIONS = ['email']

# Backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.linkedin.LinkedinOAuth',
    'social.backends.twitter.TwitterOAuth',
    )

# URLs
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/login/'
