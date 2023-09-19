import sqlite3

connection = sqlite3.connect('database.db')

with open('backend\schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

insert_query = "INSERT INTO autoclaves (id, stat, created) VALUES (?, ?, ?)"
ac_to_insert = [(0,'FREE','2023-09-18 00:00:00'),
            (1,'FREE','2023-09-18 00:00:00'),
            (2,'FREE','2023-09-18 00:00:00'),
            (3,'FREE','2023-09-18 00:00:00'),
            (4,'FREE','2023-09-18 00:00:00'),
            (5,'FREE','2023-09-18 00:00:00'),
            (6,'FREE','2023-09-18 00:00:00')]

cursor.executemany(insert_query, ac_to_insert)

connection.commit()
connection.close()
