# coding=utf-8
import os
import platform

_ = lambda s: s


PROJECT_NAME = 'example'
BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        os.pardir,
        os.pardir,
    )
)

PROJECT_DIR = os.path.abspath(
    os.path.join(
        BASE_DIR, PROJECT_NAME
    )
)

ALLOWED_HOSTS = [
    '*',
]

# Workaround for bug in Pycharm when calling syncdb on mac
if platform.system() == 'Darwin':
    os.environ['LANG'] = 'de_DE.UTF-8'

TEMPLATE_DEBUG = True
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de'
SITE_ID = 1

LANGUAGES = (
    ('de', _('German')),
)

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

USE_I18N = True
USE_L10N = True
USE_TZ = True

EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_NAME

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%(^@=f1v%g)5h7du7a#$(m%&lw=y&(c7@rtc$@*kt65agyp02x'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

MIDDLEWARE_CLASSES = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'django_fancy_captcha',
    'example',
]

TEMPLATE_DIRS = (
    '%s/templates' % PROJECT_DIR,
)
STATICFILES_DIRS = (
    '%s/static' % BASE_DIR,
)
LOCALE_PATHS = (
    '%s/locale' % BASE_DIR,
)

COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/x-sass', 'sass {infile} {outfile}'),
)

COMPRESS_ENABLED = True

FANCY_CAPTCHA_IMAGES_DIR = os.path.abspath(
    os.path.join(
        BASE_DIR,
        'data',
        'fancy_captcha'
    )
)

FANCY_CAPTCHA_IMAGE_PATTERN = r'^ball-[\d+]\.jpg$'
FANCY_CAPTCHA_CORRECT_IMAGE = 'correct.jpg'
FANCY_CAPTCHA_IMAGE_SIZE = 100