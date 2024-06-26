#!/usr/bin/python3
"""
This script retrieves and lists all cities of a specified state by querying a MySQL database.
"""
import MySQLdb
from sys import argv

# Ensure the script runs only when executed directly, not when imported
if __name__ == '__main__':
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    # Query to fetch cities based on the input state name
    cur.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])

    rows = cur.fetchall()
    city_names = []
    for row in rows:
        city_names.append(row[1])
    # Print the names of cities retrieved from the database
    print(", ".join(city_names))

    # Clean up: Close the cursor and database connection
    cur.close()
    db.close()
