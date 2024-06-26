#!/usr/bin/python3
"""
Script that retrieves and prints all City objects from a MySQL database using SQLAlchemy.
"""
from model_city import City
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

    # Query all City objects joined with their respective State objects and print their details
    cities = session.query(State, City).join(City).order_by(City.id)
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Clean up: close the session
    session.close()
