#!/usr/bin/python3
"""
Defines a Python class representing a State, using SQLAlchemy for database ORM.

The State class maps to a database table 'states' with attributes:
- id: Unique identifier for the state.
- name: Name of the state.

Requires SQLAlchemy library for ORM functionality.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    SQLAlchemy ORM class representing a state entity.

    Attributes:
        id (int): Primary key and auto-incremented identifier for the state.
        name (str): Name of the state, maximum 128 characters.

    Table name: 'states'
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
