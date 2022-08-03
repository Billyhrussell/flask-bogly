"""Seed file to make sample data for users db"""

from models import db, User
from app import app

db.drop_all()
db.create_all()

aishwarya = User(first_name = 'Aishwarya', last_name = 'Majumdar',
                img_url = 'https://stanfordopticians.co.uk/wp-content/uploads/2016/04/default-profile.png')
billy = User(first_name = 'Billy', last_name='Russell',
                img_url ='https://stanfordopticians.co.uk/wp-content/uploads/2016/04/default-profile.png')
steve = User(first_name = 'Steve', last_name = 'Martin',
                img_url = 'https://stanfordopticians.co.uk/wp-content/uploads/2016/04/default-profile.png')


db.session.add(aishwarya)
db.session.add(billy)
db.session.add(steve)

db.session.commit()