#!/usr/bin/python3
""" Module to connect to the database and print the data from the
    Table: States.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # define commandline arguments
    uName = sys.argv[1]
    paswd = sys.argv[2]
    dtbase = sys.argv[3]

    # Open database connection
    db = MySQLdb.connect(port=3306, user=uName, passwd=paswd, db=dtbase)

    # access to database interface
    cur = db.cursor()

    # execute SQL query using execute() method
    cur.execute("SELECT * FROM states ORDER BY id")

    # fetch a single row using fetchall()
    for state in cur.fetchall():
        print(state)
