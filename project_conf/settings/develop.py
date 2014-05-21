# -*- coding: utf-8 -*-
__author__ = 'gzbender'

from common import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project_db',
        'USER': 'user',
        'PASSWORD': '123',
    }
}

SOCIAL_AUTH_VK_OAUTH2_KEY = 4368642
SOCIAL_AUTH_VK_OAUTH2_SECRET = '9JiiCughH1LBRNhQKh7v'

SOCIAL_AUTH_FACEBOOK_KEY = 491440387624202
SOCIAL_AUTH_FACEBOOK_SECRET = '3d342d952d8f31b076f6549806106fee'