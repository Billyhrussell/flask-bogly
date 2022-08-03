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

@app.post("/users/new")
def add_new_user():
    #process add form
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    img_url = request.form['image-url']

    img_url = img_url if img_url else None

    new_user = User(first_name = first_name, last_name = last_name, img_url = img_url)

    #add a new user
    db.session.add(new_user)
    db.session.commit()

    #go back to users
    return redirect("/users")

@app.get("/users/<user_id>")
def display_user(user_id):
    #show information about user
    user_information = User.query.get(user_id)

    return render_template("userdetail.html", user = user_information)

@app.get("/users/<user_id>/edit")
def edit_user(user_id):
    #show the edit page for a user
    user_information = User.query.get(user_id)
    return render_template("edit.html", user = user_information)

@app.post("/users/<user_id>/edit")
def update_user(user_id):
    #process edit form
    user = User.query.get(user_id)

    user.first_name = request.form['first-name']
    user.last_name = request.form['last-name']
    user.img_url = request.form['image-url']
    #user.img_url = img_url if img_url else None

    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.post("/users/<user_id>/delete")
def delete_user(user_id):
    #delete a users information
    user = User.query.get(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect("/users")