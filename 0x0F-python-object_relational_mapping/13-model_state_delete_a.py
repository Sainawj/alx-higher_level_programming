#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the
letter 'a' from a MySQL database using SQLAlchemy.
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

    # Query all State objects with names containing
    # the letter 'a' and delete them
    states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction to delete the states from the database
    session.commit()

    # Clean up: close the session
    session.close()
