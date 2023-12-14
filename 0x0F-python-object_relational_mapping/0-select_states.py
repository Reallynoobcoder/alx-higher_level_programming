#!/usr/bin/python3
"""script that lists all states from the database"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    stats = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    cursor = stats.cursor()

    cursor.execute("SELECT id, name FROM states ORDER BY id ASC;")

    for data in cursor:
        print(data)

    cursor.close()
    stats.close()
