import os

class Config(object):
    VERSION = '0.1.0'
    ISDEBUG = (os.environ.get('ISDEBUG', 'True') == 'True')
