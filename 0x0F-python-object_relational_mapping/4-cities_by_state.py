#!/usr/bin/python3
"""
This script lists all cities from the
database `hbtn_0e_0_usa`.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    # Execute the query to fetch cities sorted by cities.id
    cursor.execute("SELECT cities.id, cities.name, \
                        states.name FROM cities JOIN states ON \
                        cities.state_id = states.id ORDER BY cities.id ASC")
    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
