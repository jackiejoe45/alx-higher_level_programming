#!/usr/bin/python3
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    ur = sys.argv[1]
    pd = sys.argv[2]
    db = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host="localhost", port=3306, user=ur, passwd=pd, db=db)
        cursor = db.cursor()

        # Execute the query to fetch states sorted by states.id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        # Fetch all rows and print them
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Close cursor and connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
