#!/usr/bin/python3
"""Select states from a database and list it."""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           port=3306, passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities INNER JOIN\
                states ON cities.state_id = states.id WHERE\
                states.name = %s ORDER BY cities.id ASC", (state_name,))
    query_rows = cur.fetchall()
    city_names = [row[1] for row in query_rows]
    if city_names:
        print(", ".join(city_names))
    cur.close()
    conn.close()
