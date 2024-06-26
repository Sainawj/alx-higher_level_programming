#!/usr/bin/python3
""" Script that lists all states from the database """
import MySQLdb
from sys import argv

# The code not be executed when imported
if __name__ == '__main__':

    # connecting to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # To give us the ability to have multiple seperate working environments
    # using the same connection to the database.
    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
