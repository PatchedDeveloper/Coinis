import sqlite3

conn =sqlite3.connect('games.db')

cursor = conn.cursor()

# cursor.execute('''CREATE TABLE GAME(id INTEGER PRIMARY KEY , solution)''')

# cursor.execute('''INSERT INTO GAME(id,solution) VALUES(?, ?)''', (1, "[123,123,123,12,3]"))

cursor.execute("Select * from GAME")

games = cursor.fetchall()
print(games)

conn.commit()
conn.close()