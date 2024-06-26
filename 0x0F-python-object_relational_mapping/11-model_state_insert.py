#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to a
MySQL database using SQLAlchemy.
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

    # Create a new State object for "Louisiana" and add it to the session
    add_state = State(name="Louisiana")
    session.add(add_state)

    # Commit the transaction to add the new state to the database
    session.commit()

    # Print the ID of the newly added State object
    print(add_state.id)

    # Clean up: close the session
    session.close()
