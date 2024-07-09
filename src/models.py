import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorites = relationship("Favorite", backref="user", lazy=True)

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(Enum("arid", "temperate", "tropical", "frozen", "murky"), nullable=False)
    terrain = Column(Enum("desert", "grasslands", "mountains", "forests", "rainforest", "jungle", "ocean", "tundra", "ice caves", "ranges", "swaps", "gas gigant", "lakes", "grassy hills", "cityscape"), nullable=False)
    population = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    characters = relationship("Character", backref='planet', lazy=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(Enum("female", "male", "other", "n/a"), nullable=False)
    birth_year = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    hair_color = Column(Enum("brown", "blond", "red", "black", "n/a"), nullable=False)
    eye_color = Column(Enum("brown", "green", "blue", "gold", "n/a"), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id')) #planet_id = planet.id creado con backref planet de la tabla Planet
    vehicle = relationship("Vehicle", backref='character', lazy=True)

class Vehicles(Base):
    __tablename__ ='vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    vehicle_class = Column(Enum("repulsorcraft", "wheeled", "starfighter"), nullable=False)
    manufacturer = Column(Enum("Incom Corporation", "Corelia Mining Corporation"), nullable=False)
    length = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    pilot_id= Column(Integer, ForeignKey('character.id')) #pilot = character.id creado con backref character tabla  Character

class Favorites(Base):
    __tablename__ ='favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) #user_id de la tabla de User creado con backref
    favorite_type = Column(Enum("Planet", "Vehicle", "Character"), nullable=False)
    favorite_id = Column(Integer, nullable=False)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
