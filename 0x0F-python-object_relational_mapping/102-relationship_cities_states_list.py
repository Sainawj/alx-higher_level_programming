#!/usr/bin/python3
"""
Module that performs MySQL query through SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    # Construct the database URI from command-line arguments
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine(db_uri, pool_pre_ping=True)

    # Ensure all tables are created based on the Base's metadata
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and print their details,
    # including the associated state
    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session to clean up resources
    session.close()
