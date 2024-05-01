import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20))
    email = Column(String(250))
    password = Column(String(20))
    subscription_date = Column(Integer)
    first_name = Column(String(50))
    last_name = Column(String(50))

    
class Faccion(Base):
    __tablename__ = 'faction'
    id = Column(Integer, primary_key=True)
    planets_under_control = Column(Integer)
    army = Column(Integer)
    starships = Column(Integer)
    leader = Column(String(50))


class Planetas(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    population = Column(Integer)
    faction_id = Column(Integer, ForeignKey('faction.id'))
    user = relationship(Faccion)

class Personajes(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    gender = character_faction = Column(String(250))
    age = Column(Integer)
    native_planet = Column(Integer)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship(Planetas)
    character_faction = Column(String(250))
    faction_id = Column(Integer, ForeignKey('faction.id'))
    user = relationship(Faccion)

class PlanetasFavoritos(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planetas)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(Usuario)

class PersonajesFavoritos(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Personajes)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(Usuario)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
