#!/usr/bin/python3
"""
Script that retrieves and lists all State objects from a MySQL database using SQLAlchemy.
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Configure and create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Ensure the table schema is created if not already present
    Base.metadata.create_all(engine)

    # Query all State objects and print their IDs and names
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Clean up: close the session
    session.close()
