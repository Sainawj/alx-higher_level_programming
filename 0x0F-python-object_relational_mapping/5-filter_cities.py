#!/usr/bin/python3
"""
Script that retrieves and prints all cities of a given state from db.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Execute a SQL query to fetch city names of the specified state
    cur.execute("SELECT cities.id, cities.name FROM cities\
                 INNER JOIN states ON cities.state_id = states.id\
                 WHERE states.name = %s", [argv[4]])

    # Fetch all rows from the query result
    rows = cur.fetchall()

    # Store city names in a list
    city_names = [row[1] for row in rows]

    # Print the list of city names separated by commas
    print(", ".join(city_names))

    # Clean up: close the cursor and database connection
    cur.close()
    db.close()
