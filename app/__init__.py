from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

# from app.auth import bp as auth_bp
# app.register_blueprint(auth_bp, url_prefix='/auth')
app.config.from_object(Config)
app.app_context().push()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)



from app import routes
from app.models import *
