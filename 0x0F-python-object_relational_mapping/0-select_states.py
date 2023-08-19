#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # define commandline arguments
    uName = sys.argv[1]
    paswd = sys.argv[2]
    dtbase = sys.argv[3]
    
    db = MySQLdb.connect(user=uName, password=paswd, database=dtbase)
    cur = db.cursor()
    # execute SQL query using execute() method
    cur.execute("SELECT * FROM states ORDER BY id")

    # fetch a single row using fetchall()
    for state in cur.fetchall():
        print(state)
