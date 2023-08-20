#!/usr/bin/python3
""" Module to connect to the database and print the data from the
    Table: States with specific number.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    usrName = sys.argv[1]
    pswd = sys.argv[2]
    db_name = sys.argv[3]
    stateName = sys.argv[4]

    db = MySQLdb.connect(port=3306, user=usrName,
                         passwd=pswd, db=db_name)

    cursor = db.cursor()

    cursor.execute("""SELECT cities.name FROM states
                    INNER JOIN cities
                    ON states.id = cities.state_id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC""", (stateName,))

    data = cursor.fetchall()

    city = []
    for row in data:
        city.append(row[0])
    print(*city, sep=", ")

    cursor.close()
    db.close()
