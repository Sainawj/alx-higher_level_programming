#!/usr/bin/python3
"""
Module that defines the City class using SQLAlchemy ORM and establishes its relationship with the State class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    """
    SQLAlchemy ORM class representing a city entity.

    Attributes:
        id (int): Primary key identifier for the city.
        name (str): Name of the city, maximum 128 characters.
        state_id (int): Foreign key referencing the ID of the state to which the city belongs.

    Table name: 'cities'
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
