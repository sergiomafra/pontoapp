from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


## App
app = Flask(__name__)
app.config.from_object(Config)

## Database
db = SQLAlchemy(app)

## Migration
migrate = Migrate(app,db)

from app import routes, models
