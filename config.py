import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or '52770cc66594d5923cb2807582ea9277'