from flask import Flask
from .api.v1.views.UserView import auth
from instance.config import app_config

"""This is the main app set up"""

def create_app(config_name):
    '''Creating app, setting up configurations to run the app'''
    app = Flask(__name__,instance_relative_config=True)
    app.config['JSON_SORT_KEYS'] = False #Not sort return data
    if not config_name:
        app.config.from_object(app_config['development'])
    else:
        app.config.from_object(app_config[config_name])

    app.config.from_pyfile('config.py',silent=True)

    app.register_blueprint(auth)

    return app