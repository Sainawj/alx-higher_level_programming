#!/usr/bin/python3
"""
Script that retrieves and lists all State objects containing
the letter 'a' from a MySQL database using SQLAlchemy.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Ensure the table schema is created if not already present
    Base.metadata.create_all(engine)

    # Query all State objects containing the letter 'a' in their
    # name and print their IDs and names
    states = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Clean up: close the session
    session.close()
