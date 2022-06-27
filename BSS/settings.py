import os
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # connection projects
    'BSS',
    'Tender',
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

ROOT_URLCONF = 'BSS.urls'

TEMPLATES = [
    {
        'BACKEND'  : 'django.template.backends.django.DjangoTemplates',
        'DIRS'     : [ os.path.join(BASE_DIR, 'templates') ],
        'APP_DIRS' : True,
        'OPTIONS'  : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'BSS.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.sqlite3',
	    # Подключение БД
        'NAME'   : os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL  = '/static/'

MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
MEDIA_URL   = '/media/'

# TEMPLATE_DIRS = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates')

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'testdjangos@gmail.com'
# EMAIL_HOST_PASSWORD = 'testdjango123'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# # send_mail('Django mail', 'This e-mail was sent with Django.',
# # 'your_account@gmail.com', ['your_account@gmail.com'], fail_silently=False)

# LOGIN_REDIRECT_URL = reverse_lazy('profile')
# LOGIN_URL = reverse_lazy('login')
# LOGOUT_URL = reverse_lazy('logout')