"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from app import app
db = SQLAlchemy()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement=True)
    first_name = db.Column(db.Text,
                            nullable = False)
    last_name = db.Column(db.Text,
                            nullable = False)
    img_url = db.Column(db.Text,
                            nullable = True)

