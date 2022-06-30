"""
Django settings for surgery project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os


import hospital

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD='django.db.models.AutoField' 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j-erj2ub*bp^$e!7o7fd33#01n-z43bs-ttpwfs6)vn-hofba7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'xhtml2pdf',
    'rest_framework',
    'django_filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phonenumber_field',
    'bootstrap3',
    'jquery',
    'account.apps.AccountConfig',
    'user_profile.apps.UserProfileConfig',
    'appointment.apps.AppointmentConfig',
    'import_export',
    'icd10.apps.Icd10Config',
    'paymentMethod.apps.PaymentmethodConfig',
    'consultation_fee.apps.ConsultationFeeConfig',
    'edliz.apps.EdlizConfig',
    'medaid.apps.MedaidConfig',
    'widget_tweaks',
    'broadcast',
    'phonenumbers',
    'django_apscheduler',
   
  


   
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hospital.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'hospital.wsgi.application'
AUTH_USER_MODEL = 'account.User'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'surgery_management_system',
        'USER': 'postgres',
        'PASSWORD': 'endurancedame',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = "account:home"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]

#alternate code for verification : c1L5sCGOLjiZMZN1T9T_Ibnjt9SO_uhtWq5Znn-Ys
TWILIO_ACCOUNT_SID = os.getenv("AC4ca11b35c9c491bc720dfcced11beb64")
TWILIO_AUTH_TOKEN = os.getenv("9d56639677aab59c8a38d6eda8fe587e")
TWILIO_NUMBER = os.getenv("+18504937780")
# TWILIO_ACCOUNT_SID = os.getenv("AC785b62608f261eee4176460c5b96936d")
# TWILIO_AUTH_TOKEN = os.getenv("6a82fbec414b275713604a7c0e59c316")
# TWILIO_NUMBER = os.getenv("+13187053478")
# SMS_BROADCAST_TO_NUMBERS = [ 
#     "+263779145759",# use the format +19735551234

# ]

#verification code to be used when phone lost
#x-opBn-sINEc4FSdC2vKL_yUSQqXkMZMxMBOpX5-