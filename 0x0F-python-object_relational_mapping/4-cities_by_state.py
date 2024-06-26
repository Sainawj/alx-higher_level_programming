#!/usr/bin/python3
"""
Script-lists all cities from the db
"""
import MySQLdb
from sys import argv

# The code not to be executed when imported
if __name__ == '__main__':
    # make a connection to the db
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
