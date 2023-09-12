import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or '52770cc66594d5923cb2807582ea9277'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')\
  or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False