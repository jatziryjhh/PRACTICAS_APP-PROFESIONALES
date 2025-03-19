"""
Django settings for errorPages project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kc2sz!o9t80gef=&9s*dew5^52@-o@)u&r&#i5zuq*0#6ot7fa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'users',
    'productos',
    'categorias',
    'rest_framework',
    'alumnos',
    'rest_framework_simplejwt',
    'corsheaders',
]

#Configuracion de AUTH
#ESTAMOS DICIENDO YA NO USES COOKIES,USA JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

AUTH_USER_MODEL='users.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8001",
]

CORS_ALLOW_ALL_ORIGINS = True


ROOT_URLCONF = 'errorPages.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'errorPages.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

#que django sepa que vamos a usar mysql
import pymysql
#que django sepa que vamos a usar mysql
pymysql.install_as_MySQLdb()

#tienes que tener la base de datos creada en mysql y tambien iniciar sesion de mysql
DATABASES = {
    'default': {
        #cambiamos sqlite3 por mysql
        'ENGINE': 'django.db.backends.mysql',
        #en el name quitamos BASE_DIR / 'db.sqlite3', y pusimos en comillas el nombre de la base de datos con lo de usuario
        #'NAME': 'personas',
        'NAME':'mi_base_de_datos',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

HANDER404='app.views.error_404_view'
HANDER500='app.views.error_500_view'

#no me los roben,porfis:(
#SEARCH_ENGINE_ID='e4c89ecf1e32d448c'
#GOOGLE_API_KEY='AIzaSyAST2GdnTEt6cVcKC2jmzNVF7utaYVGkk8'

AUTH_USER_MODEL='users.CustomUser'


LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/home' # Dónde irán los usuarios tras iniciar sesión
LOGOUT_REDIRECT_URL = '/users/login/'