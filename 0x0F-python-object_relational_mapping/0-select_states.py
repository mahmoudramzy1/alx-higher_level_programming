#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect (
            host = "localhost",
            port = 3306,
            user = sys.argv[1],
            password = sys.argv[2],
            database = sys.argv[3]
            )

    mycursor = conn.cursor()

    mycursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = mycursor.fetchall()
    for state in states:
        print(state)
    mycursor.close()
    conn.close()
