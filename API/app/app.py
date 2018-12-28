import os
import datetime
from flask import Flask
from flask import Session

from .api.v1.views.UserView import auth
from .api.v1.views.QuestionView import ques
from .api.v1.views.AnswerView import ans

from instance.config import app_config

"""This is the main app set up"""

def create_app(config_name):
    '''Creating app, setting up configurations to run the app'''

    app = Flask(__name__, instance_relative_config=True)

    app.config['JSON_SORT_KEYS'] = False #Not sort return data
    if not config_name:
        app.config.from_object(app_config['development'])
    else:
        app.config.from_object(app_config[config_name])

    app.config['SESSION_TYPE'] = 'memcached'

    app.secret_key = 'I\xb4\x14\xa6\xb2b\xc41SP\xe7\xd5\xd9\x89\xd0\xd7'
    app.config.from_pyfile('config.py',silent=True)

    app.register_blueprint(auth)
    app.register_blueprint(ques)
    app.register_blueprint(ans)
    
    app.permanent_session_lifetime = datetime.timedelta(minutes=1)
    return app