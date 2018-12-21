import os
'''Configurations for the app this will allow the set up
    of env variables'''

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


app_config = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)