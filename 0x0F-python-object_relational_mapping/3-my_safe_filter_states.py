#!/usr/bin/python3
"""
   takes in an argument and displays all values in the states
   table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # innitialize command line arguments
    usrName = sys.argv[1]
    paswd = sys.argv[2]
    dtbase = sys.argv[3]
    stateName = sys.argv[4]

    # open database connection
    db = MySQLdb.connect(port=3306, user=usrName, password=paswd, db=dtbase)

    # access database interface
    c = db.cursor()

    # execute SQL query using execute() method
    str = "SELECT * FROM states WHERE BINARY `name` = '{}' ORDER BY id"
    c.execute(str.format(stateName))

    # fetch a single row using fetchall()
    for state in c.fetchall():
        print(state)
