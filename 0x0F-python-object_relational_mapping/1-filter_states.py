#!/usr/bin/python3
"""
   lists all states with a name starting with N
   from the database
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # innitialize command line arguments
    usrName = sys.argv[1]
    paswd = sys.argv[2]
    dtbase = sys.argv[3]

    # open database connection
    db = MySQLdb.connect(port=3306, user=usrName, password=paswd, db=dtbase)

    # access database interface
    c = db.cursor()

    # execute SQL query using execute() method
    c.execute("SELECT * FROM states ORDER BY id")

    # fetch a single row using fetchall()
    for state in c.fetchall():
        if (state[1][0] == 'N'):
            print(state)
