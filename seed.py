"""Seed file to make sample data for users db"""

from models import db, User
from app import app

db.drop_all()
db.create_all()

aishwarya = User(first_name = 'Aishwarya', last_name = 'Majumdar',
                img_url = 'https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-jumbo.jpg?quality=75&auto=webp')
billy = User(first_name = 'Billy', last_name='Russell',
                img_url ='https://i.insider.com/5484d9d1eab8ea3017b17e29?width=600&format=jpeg&auto=webp')
steve = User(first_name = 'Steve', last_name = 'Martin',
                img_url = 'https://prdaficalmjediwestussa.blob.core.windows.net/images/2019/07/0003_COLOR_2015_LAA_SteveMartin_-557716299_KW_8679_AE182BAE8D02C2DDB953723A94E7A3FF.jpg')


db.session.add(aishwarya)
db.session.add(billy)
db.session.add(steve)

db.session.commit()