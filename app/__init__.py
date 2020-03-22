from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app_flsk = Flask(__name__)
app_flsk.config.from_object(Config)
db = SQLAlchemy(app_flsk)
migrate = Migrate(app_flsk, db)
login = LoginManager(app_flsk)
login.login_view = 'login'

from app import routes, models