"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_PROFILE_PIC = 'https://stanfordopticians.co.uk/wp-content/uploads/2016/04/default-profile.png'


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
                            nullable = False,
                            default = DEFAULT_PROFILE_PIC)

    posts = db.relationship('Post', backref = 'user')



class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement = True)
                    #primary key integers default to autoincrement
    title = db.Column(db.Text,
                        nullable = False)
    content = db.Column(db.Text,
                        nullable = False)
    created_at = db.Column(db.DateTime,
                        nullable = False,
                        default = db.func.now())
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable = False)


class Tag(db.Model):

    __tablename__ = "tags"

    id = db.Column(db.Integer,
                    primary_key = True)
    name = db.Column(db.Text,
                    unique = True,
                    nullable = False)

    tag_posts = db.relationship('Post',
                            secondary = 'post_tags',
                            backref = 'tags')

class PostTag(db.Model):

    __tablename__ = "post_tags"

    post_id = db.Column(db.Integer,
            db.ForeignKey("posts.id"),
            primary_key = True)
    tag_id = db.Column(db.Integer,
            db.ForeignKey("tags.id"),
            primary_key = True)




