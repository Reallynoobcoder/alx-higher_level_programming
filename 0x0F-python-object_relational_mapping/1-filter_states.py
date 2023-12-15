#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)"""

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

    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
    cursor.execute(query)

    rows = cursor.fetchall()

    for data in rows:
        print(data)

    cursor.close()
    stats.close()
