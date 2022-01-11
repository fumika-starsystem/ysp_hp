from .settings_common import *


#SECRITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []

#ロギング設定
LOGGING = {
    'version': 1, #1固定
    'disable_existing_loggers': False,

    #ロガーの設定
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'ysp': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    #ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    #フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ysp.southaichi1006@gmail.com'
EMAIL_HOST_PASSWORD = 'bsqikcbnwhovoxcb'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
