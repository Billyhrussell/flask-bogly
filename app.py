"""Blogly application."""

from flask import Flask, render_template, redirect, request
from models import db, connect_db, User, Post
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
    """Redirects to a page displaying a list of current users."""

    return redirect("/users")

@app.get("/users")
def user_list():
    """Displays all current users"""

    users = User.query.all()
    return render_template("userlisting.html", users = users)

@app.get("/users/new")
def add_new_user_form():
    """Displays a form allowing a new user to be added."""

    return render_template("newuser.html")

@app.post("/users/new")
def add_new_user():
    """Once a new user is submitted, processes the form and addes the new user to
    the user list and redirects back to the user list."""

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

@app.get("/users/<int:user_id>")
def display_user(user_id):
    """Upon click on a specific name on user list, displays information about
    selected user, allowing editting and deletion of user."""

    user_information = User.query.get_or_404(user_id)

    return render_template("userdetail.html", user = user_information)

@app.get("/users/<int:user_id>/edit")
def edit_user(user_id):
    """Displays form allowing user to edit their information."""
    user_information = User.query.get_or_404(user_id)
    return render_template("edit.html", user = user_information)

@app.post("/users/<int:user_id>/edit")
def update_user(user_id):
    """Upon saving on edit form, proccess the edit form and returns editted user
    onto the user list, redirects to user list."""
    user = User.query.get(user_id)

    user.first_name = request.form['first-name']
    user.last_name =  request.form['last-name']
    user.img_url = request.form['image-url']
    #user.img_url = img_url if img_url else None

    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
    """Upon clicking Delete button, deletes the user and redirects to user list."""
    user = User.query.get(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

#PART 2

@app.get("/users/<int:user_id>/posts/new")
def show_add_post_form(user_id):
    """ Show form to add post for user """
    user = User.query.get_or_404(user_id)
    return render_template("addpost.html", user = user)

@app.post("/users/<int:user_id>/posts/new")
def add_post_to_page(user_id):
    """Handle add form and add post, redirect to user detail page """
    user = User.query.get_or_404(user_id)

    title = request.form['title']
    content = request.form['content']

    new_post = Post(title = title, content = content, user_id = user_id)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/users/{user_id}")

@app.get("/posts/<int:post_id>")
def show_post(post_id):
    """Show a post"""

    post = Post.query.get_or_404(post_id)

    return render_template("postdetail.html", post = post)

@app.get("/posts/<int:post_id>/edit")
def edit_post(post_id):
    """Show a form to edit post"""

    post = Post.query.get_or_404(post_id)
    # TODO: fix template

    return render_template("editpost.html", post = post)

@app.post("/posts/<int:post_id>/edit")
def get_post_edits(post_id):
    """Get edit post information and redirect to post view"""

    post = Post.query.get_or_404(post_id)

    post.title = request.form['title']
    post.content =  request.form['post-content']

    db.session.add(post)
    db.session.commit()
    # TODO: flash message

    return redirect(f"/posts/{post_id}")

@app.post("/posts/<int:post_id>/delete")
def delete_post(post_id):
    """Delete the post and redirect to user page"""

    post = Post.query.get_or_404(post_id)
    user_id = post.user_id

    db.session.delete(post)
    db.session.commit()


    return redirect(f"/users/{user_id}")