#!/usr/bin/python3
"""script that takes in an argument and displays all values
and is safe from MySQL injections
"""

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

    query = "SELECT * FROM states WHERE NAME LIKE BINARY %s ORDER BY id ASC;"
    cursor.execute(query, (argv[4] + '%',))

    for data in cursor.fetchall():
        print(data)

    cursor.close()
    stats.close()
