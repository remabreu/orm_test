'''
Created on Aug 1, 2014

@author: rodrigoabreu
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base

engine = create_engine('sqlite:////Users/rodrigoabreu/Documents/Sakila.sqlite3')


Base = automap_base()

class Actor(Base):
    __tablename__='actor'

class Film(Base):
    __tablename__='film'

from sqlalchemy.orm import sessionmaker


session = sessionmaker()
session.configure(bind=engine)
Base.prepare(engine, reflect=True)

s = session()
actor_list =  s.query(Actor).filter(Actor.first_name == "PENELOPE").all()

for i in actor_list:
    print i.first_name, i.last_name