from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

db.create_all()
db.session.commit()

from flaskr.models import Note
import flaskr.views

