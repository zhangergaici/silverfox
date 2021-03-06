"""
Django settings for SilverFox project.

Generated by 'django-admin startproject' using Django 2.0b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 把Plugins,Common目录添加到系统目录里面
sys.path.append(os.path.join(BASE_DIR, 'Plugins'))
sys.path.append(os.path.join(BASE_DIR, 'Common'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i7zyl$e6l47@c^7rp_7lexik+8^7f#bndx4byd88fkb^j)w11='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = 'WebConsole.AuthUser'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'WebConsole',
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

ROOT_URLCONF = 'SilverFox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'WebConsole', 'templates')],
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
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'WebConsole/templates'),)

WSGI_APPLICATION = 'SilverFox.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
# BOOL
# 是否使用Machines的缓冲机制；
# 使用些机制可以减缓页面打开时的卡顿现象，
# 但对于实时性来说，会有些偏差
# 注意：此机制只能在独立运行时设置成true，
#       如果部署到apache等http服务器上以后此参数仍然为True，
#       有可能会造成大量的udp广播包
USE_MACHINES_BUFFER = False

# FLOAT；单位：秒
# 当多长时间没有查询Machines相关数据时停止缓冲机制，
# 以避免长时间没有人操作还不停的广播查询包
STOP_BUFFER_TIME = 300

# FLOAT；单位：秒
# Machines缓冲机制的刷新间隔
# 间隔时间越短，越精确，发送的数据也越频繁
# 此参数仅在 USE_MACHINES_BUFFER = True 时起作用
MACHINES_BUFFER_FLUSH_TIME = 1.0

# FLOAT；单位：秒
# 每次查询Machine时等待响应的最长时间
MACHINES_QUERY_WAIT_TIME = 1.0

# MACHINES地址配置
# 当此参数不为空时，则由原来的广播探测改为固定地址探测，
# WebConsole仅会以此配置的地址进行探测，
# 当服务器存在跨网段的情况时，此方案犹为有用。
# 例子：
# MACHINES_ADDRESS = ["192.168.0.1", "10.0.0.1", "172.16.0.1"]
MACHINES_ADDRESS = ["127.0.0.1"]
