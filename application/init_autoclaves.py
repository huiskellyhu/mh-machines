import sqlite3

connection = sqlite3.connect('database.db')

with open('application\schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

insert_query = "INSERT INTO autoclaves (id, mname, stat, created, setting) VALUES (?, ?, ?, ?, ?)"
ac_to_insert = [(0,'WASHER','FREE','2023-09-18 00:00:00', "LIQUID15"),
            (1,'AUTOCLAVE 1','FREE','2023-09-18 00:00:00',"LIQUID15"),
            (2,'AUTOCLAVE 2','FREE','2023-09-18 00:00:00',"LIQUID15"),
            (3,'AUTOCLAVE 3','FREE','2023-09-18 00:00:00',"LIQUID15"),
            (4,'AUTOCLAVE 4','FREE','2023-09-18 00:00:00',"LIQUID15"),
            (5,'AUTOCLAVE 5','FREE','2023-09-18 00:00:00',"LIQUID15"),
            (6,'AUTOCLAVE 6','FREE','2023-09-18 00:00:00',"LIQUID15")]

cursor.executemany(insert_query, ac_to_insert)

connection.commit()
connection.close()
