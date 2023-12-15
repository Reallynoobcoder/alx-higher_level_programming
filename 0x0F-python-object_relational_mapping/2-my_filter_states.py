#!/usr/bin/python3
"""script that takes in an argument and displays all values"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    stats = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )

    cursor = stats.cursor()

    query = "SELECT * FROM states WHERE NAME LIKE BINARY '{}' \
    ORDER BY id ASC;".format(argv[4])
    cursor.execute(query)

    rows = cursor.fetchall()

    for data in rows:
        print(data)

    cursor.close()
    stats.close()
