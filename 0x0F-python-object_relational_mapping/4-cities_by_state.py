#!/usr/bin/python3
"""
   a script that lists all cities from the
   database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # innitialize command line arguments
    usrName = sys.argv[1]
    paswd = sys.argv[2]
    dtbase = sys.argv[3]

    # connect to database
    db = MySQLdb.connect(port=3306, user=usrName, passwd=paswd, db=dtbase)

    # access database interface
    c = db.cursor()

    # execute
    c.execute("""SELECT cities.id, cities.name, states.name
               FROM cities
               INNER JOIN states
               ON cities.state_id = states.id
               ORDER BY cities.id""")

    # fetch data
    for city in c.fetchall():
        print(city)

    # close execute
    c.close()
    db.close()
