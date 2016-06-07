import os
ALLOWED_HOSTS = []
BASE_DIR = 'D:\myp_projectp528_funcodeuncode'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'D:\\myp\\02_project\\160528_funcode\\funcode\\db.sqlite3'}}
DEBUG = True
INSTALLED_APPS = ('django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'app_django', 'app_rzrk', 'app_cplusplus', 'app_vs2008', 'app_qt4', 'app_vim')
LANGUAGE_CODE = 'en-us'
MIDDLEWARE_CLASSES = ('django.contrib.sessions.middleware.SessionMiddleware', 'django.middleware.common.CommonMiddleware', 'django.middleware.csrf.CsrfViewMiddleware', 'django.contrib.auth.middleware.AuthenticationMiddleware', 'django.contrib.auth.middleware.SessionAuthenticationMiddleware', 'django.contrib.messages.middleware.MessageMiddleware', 'django.middleware.clickjacking.XFrameOptionsMiddleware')
ROOT_URLCONF = 'funcode.urls'
SECRET_KEY = '0(o^bp2x*ct3tln+*dsxm#&*j@#^p*oe&5u+t_br&dtowm1f)d'
STATIC_URL = '/static/'
TEMPLATE_DEBUG = True
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
WSGI_APPLICATION = 'funcode.wsgi.application'