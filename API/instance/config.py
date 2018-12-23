import os
'''Configurations for the app this will allow the set up
    of env variables'''

class Config:
    SECRET_KEY = os.getenv('SECRET')
    DEBUG = False
    ENV="production"


class DevelopmentConfig(Config):
    DEBUG = True
    ENV="development"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    ENV="testing"


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    ENV="production"


app_config = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)