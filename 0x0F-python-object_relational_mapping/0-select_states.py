#!/usr/bin/python3
import MySQLdb
import sys

# define commandline arguments
uName = sys.argv[1]
paswd = sys.argv[2]
dtbase = sys.argv[3]

db = MySQLdb.connect(user=uName, password=paswd, database=dtbase)
cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id")
for state in cur.fetchall():
    print(state)
