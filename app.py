"""Blogly application."""

from flask import Flask, render_template, redirect, request
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

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

app.post("/users/new")
def add_new_user():
    #process add form
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    img_url = request.form['image-url']

    new_user = User(first_name = first_name, last_name = last_name, img_url = img_url)

    #add a new user
    db.session.add(new_user)
    db.session.commit()

    #go back to users
    return redirect("/users")





