#!/usr/bin/python3
"""
Script - lists all states with a name starting with N from the db
"""
import MySQLdb
from sys import argv

# The code not be executed when imported
if __name__ == '__main__':
    # make a connection to the db
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Gives the ability to have multiple seperate working environments through
    # the same connection to the db.
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
