"""
Django settings for my_blog project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ora9^@@(9r_ejuc5oxu8(2$+w%fb=e)b@22la3p0n=6ul^3$r$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# 下面就是logging的配置
LOGGING = {
    'version': 1,  # 指明dictConnfig的版本，目前就只有一个版本，哈哈
    'disable_existing_loggers': False,  # 表示是否禁用所有的已经存在的日志配置
    'formatters': {  # 格式器
        'verbose': {  # 详细
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'standard': {  # 标准
            'format': '[%(asctime)s] [%(levelname)s] %(message)s'
        },
    },
    # handlers：用来定义具体处理日志的方式，可以定义多种，"default"就是默认方式，"console"就是打印到控制台方式。file是写入到文件的方式，注意使用的class不同
    'handlers': {                    # 处理器，在这里定义了两个个处理器
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',   # 文件重定向的配置，将打印到控制台的信息都重定向出去 python manage.py runserver >> /home/aea/log/test.log
            # 'stream': open('/log/test.log','a'),  #虽然成功了，但是并没有将所有内容全部写入文件，目前还不清楚为什么
            'formatter': 'standard'   # 制定输出的格式，注意 在上面的formatters配置里面选择一个，否则会报错
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/django_blog/my_blog/log/jwt_test.log',  # 这是将普通日志写入到日志文件中的方法，
            'formatter': 'standard'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/django_blog/my_blog/log/all.log',      # 日志输出文件
            'maxBytes': 1024*1024*5,                  # 文件大小
            'backupCount': 5,                         # 备份份数
            'formatter': 'standard',                  # 使用哪种formatters日志格式
        },
        # 上面两种写入日志的方法是有区别的，前者是将控制台下输出的内容全部写入到文件中，这样做的好处就是我们在views代码中的所有print也会写在对应的位置
        # 第二种方法就是将系统内定的内容写入到文件，具体就是请求的地址、错误信息等，小伙伴也可以都使用一下然后查看两个文件的异同。
    },
    'loggers': {  # log记录器，配置之后就会对应的输出日志
        # django 表示就是django本身默认的控制台输出，就是原本在控制台里面输出的内容，在这里的handlers里的file表示写入到上面配置的file-/home/aea/log/jwt_test.log文件里面
        # 在这里的handlers里的console表示写入到上面配置的console-/home/aea/log/test.log文件里面
        'django': {
            'handlers': ['console', 'file'],
            # 这里直接输出到控制台只是请求的路由等系统console，当使用重定向之后会把所有内容输出到log日志
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request ': {
            'handlers': ['console', 'file'],
            'level': 'WARNING',  # 配合上面的将警告log写入到另外一个文件
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['file'],  # 指定file handler处理器，表示只写入到文件
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
    'user',
    'show_time',
    'rest_framework',
    'django_seed',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'casbin_middleware.middleware.CasbinMiddleware'
]

ROOT_URLCONF = 'my_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'my_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# 静态文件配置
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# markdown的支持配置
MARKDOWN_EXTENSIONS = [
                        # 包含 缩写、表格等常用扩展
                        'markdown.extensions.extra',
                        # 语法高亮扩展
                        'markdown.extensions.codehilite',
                        ]
