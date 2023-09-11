from flask import Flask
from config import Config

app = Flask(__name__)

app.app_context().push()
app.config.from_object(Config)

from app import routes