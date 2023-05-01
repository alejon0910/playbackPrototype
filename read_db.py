import sqlite3
import playsound

conn = sqlite3.connect("track.sqlite")
cursor = conn.cursor()

cursor.execute("""SELECT filename FROM tracks WHERE id=1""")
filepath = cursor.fetchall()[0][0]

print(filepath)
playsound.playsound(filepath)