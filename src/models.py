import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_User = Column(Integer, primary_key=True)
    Nombre_usuario = Column(String(250), nullable=False)
    Password=Column(String(255), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_Fa = Column(Integer, primary_key=True)
    id_User = Column(Integer, ForeignKey("user.id_User"))
    id_Pe= Column(Integer, ForeignKey("people.id_Pe"))
    id_Pl = Column(Integer, ForeignKey("planet.id_Pl"))
    
class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_Pe = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    id_Pl = Column(Integer, ForeignKey("planet.id_Pl"))
    id_Fi = Column(Integer, ForeignKey("film.id_Fi"))
    
class Planet(Base):
    __tablename__ = 'planet'
    id_Pl =Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
   

class Film(Base):
    __tablename__ = 'film'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_Fi = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    director = Column(String(250), nullable=False)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
