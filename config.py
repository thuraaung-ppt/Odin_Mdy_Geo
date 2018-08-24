import os 

class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/mydb.db' % APPLICATION_DIR 
    SQLALCHEMY_TRACK_MODIFICATIONS = 'WhoisWhoInMyanmar Database'
    SECRET_KEY = 'WhoisWhoInMyanmar Project'
    STATIC_DIR = os.path.join(APPLICATION_DIR,'static')
    IMAGE_DIR = os.path.join(STATIC_DIR,'img')


