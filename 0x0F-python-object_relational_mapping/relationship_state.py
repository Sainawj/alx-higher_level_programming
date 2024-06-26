#!/usr/bin/python3
"""
Module that defines the State class using SQLAlchemy ORM and establishes its relationship with the City class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    SQLAlchemy ORM class representing a state entity.

    Attributes:
        id (int): Primary key identifier for the state.
        name (str): Name of the state, maximum 128 characters.
        cities (relationship): One-to-many relationship with City objects.

    Table name: 'states'
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
