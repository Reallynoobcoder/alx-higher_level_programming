#!/usr/bin/python3
"""lists all cities from the database"""

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

    query = "SELECT cities.id, cities.name, states.name AS state_name\
    FROM cities\
    JOIN states ON cities.state_id = states.id\
    ORDER BY cities.id;"
    cursor.execute(query)

    for data in cursor.fetchall():
        print(data)

    cursor.close()
    stats.close()
