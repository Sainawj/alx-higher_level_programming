#!/usr/bin/python3
"""
Script that adds the State object "California" along with
the City object "San Francisco"
to the database hbtn_0e_100_usa.
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

    # Ensure all tables are created based on the Base's metadata
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Create a new City object for San Francisco
    new_city = City(name='San Francisco')

    # Create a new State object for California and
    # associate it with the new city
    new_state = State(name='California')new_state.cities.append(
            new_city)

    # Add the new State and City objects to the session
    session.add_all([new_state, new_city])

    # Commit the transaction to save changes to the database
    session.commit()

    # Clean up: close the session
    session.close()
