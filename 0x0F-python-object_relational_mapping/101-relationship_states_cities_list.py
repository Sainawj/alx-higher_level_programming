#!/usr/bin/python3
"""
Script that lists all State objects and their corresponding City objects
from a MySQL database named 'hbtn_0e_101_usa' using SQLAlchemy.
"""

if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # Ensure the table schema is created if not already present
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Query all State objects and print their IDs and names
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

        # Print all City objects belonging to the current State
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    # Clean up: close the session
    session.close()
