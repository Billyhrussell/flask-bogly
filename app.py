"""Blogly application."""

from flask import Flask, render_template, redirect, request
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.get("/")
def homepage():
    """TODO: """

    return redirect("/users")

@app.get("/users")
def user_list():
    """TODO: """

    users = User.query.all()
    return render_template("userlisting.html", users = users)

@app.get("/users/new")
def add_new_user_form():
    """TODO: """

    return render_template("newuser.html")



