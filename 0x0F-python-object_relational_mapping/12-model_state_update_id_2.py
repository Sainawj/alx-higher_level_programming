#!/usr/bin/python3
"""
Script that updates the name of a State object in a
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

    # Query the State object with ID '2' and update its name to "New Mexico"
    state_to_update = session.query(State).filter_by(id='2').first()
    state_to_update.name = "New Mexico"

    # Commit the transaction to update the state's name in the database
    session.commit()

    # Clean up: close the session
    session.close()
