from flask import Flask, g
from flask_session import Session
from flask_login import current_user
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
# from authomatic import Authomatic
from app.config import get_config

app = Flask(__name__)

# Configs for MongoDB
app.config = get_config(app.config)
Session(app)
# Flask-login Config
login = LoginManager(app)
login.login_view = 'api/login'

db = MongoEngine(app)

# authomatic = Authomatic( CONFIG, os.environ.get('SECRET'))


@app.before_request
def global_user():
    g.user = current_user
    
# Make current user available on templates
@app.context_processor
def inject_user():
    try:
        return {'user': g.user}
    except AttributeError:
        return {'user': None}
    