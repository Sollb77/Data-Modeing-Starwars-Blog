import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_User = Column(Integer, primary_key=True)
    Nombre_usuario = Column(String(250), nullable=False)
    Password=Column(String(255), nullable=False)

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_Fa = Column(Integer, primary_key=True)
    id_User = Column(String(250), nullable=False)
    id_Pe= Column(String(250), nullable=False)
    od_Pl = Column(String(250), nullable=False)
    
class People(Base):
    __tablename__ = 'People'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_Pe = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    id_pl = Column(String(250), nullable=False)
    id_Fi = Column(String(250), nullable=False)
    
    class Planet(Base):
     __tablename__ = 'Planet'
    id_Pl =Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    id_Fi = Column(String(250), nullable=False)

    class Film(Base):
     __tablename__ = 'Film'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_Fi = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    id_Pe = Column(String(250), nullable=False)
    director = Column(String(250), nullable=False)
    id_Pl = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
