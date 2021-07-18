import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    

'''
Person
Have vname and release year
'''


trips = db.Table(
    'trips',
    Column('traveller_id', Integer, ForeignKey('travellers.id'), primary_key=True),
    Column('venue_id', Integer, ForeignKey('venues.id'), primary_key=True)
)


class Venue(db.Model):
    __tablename__ = "venues"

    id = Column(Integer, primary_key=True)
    vname = Column(String, nullable=False)
    visit_year = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    start = Column(DateTime, default=datetime.datetime.utcnow)

    cast = db.relationship(
        'Traveller',
        secondary=trips,
        backref=db.backref(
            'venues',
            lazy=True))

    def __init__(self, vname, visit_year, duration):
        self.vname = vname
        self.visit_year = visit_year
        self.duration = duration

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return f'<{self.id} - {self.vname} - {self.visit_year}>'

    def format(self):
        return {
            'id': self.id,
            'vname': self.vname,
            'visit_year': self.visit_year,
            'duration': self.duration
        }


class Traveller(db.Model):
    __tablename__ = 'travellers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    start = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return f'<{self.id} - {self.name}>'

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'start': self.start
        }
