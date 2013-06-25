# coding=utf-8
from example.conf.dev import *

try:
    from settings_local import *
except ImportError:
    pass
