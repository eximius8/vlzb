from .base import *

import os

DEBUG = eval(os.getenv('DEBUG', "True"))


ALLOWED_HOSTS = ['*']

