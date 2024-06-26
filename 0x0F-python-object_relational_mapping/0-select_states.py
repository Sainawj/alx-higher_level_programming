#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

def list_states(user, passwd, db_name):
    """
    Lists all states from the database.

    Args:
        user (str): The MySQL username.
        passwd (str): The MySQL password.
        db_name (str): The database name.
    """
    # Make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)

    # Create a cursor object to interact with the database
    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    # Fetch all the rows and print them
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    # Clean up process
    cur.close()
    db.close()

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./script.py <mysql_username> <mysql_password> <database_name>")
    else:
        list_states(argv[1], argv[2], argv[3])
