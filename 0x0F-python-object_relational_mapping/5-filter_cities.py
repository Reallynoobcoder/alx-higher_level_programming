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
    state_agr = argv[4]

    query = "SELECT cities.name \
             FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s \
             ORDER BY cities.id;"

    cursor.execute(query, (state_agr,))

    rows = cursor.fetchall()

    if rows:
        flag = 0
        for row in rows:
            if flag == 1:
                print(", ", end="")
            print(row[0], end="")
            flag = 1
    print()

    cursor.close()
    stats.close()
