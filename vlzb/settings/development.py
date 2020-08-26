from .base import *

import os

DEBUG = eval(os.getenv('DEBUG', "False"))


ALLOWED_HOSTS = ['*']

