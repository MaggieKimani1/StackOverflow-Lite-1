from flask import Flask
from instance.config import app_config
"""Importing configurations from config file"""

def create_app(config_name):
    '''Creating app, setting up configurations to run the app'''
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    return app