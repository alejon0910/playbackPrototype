import sqlite3

conn = sqlite3.connect("track.sqlite")
cursor = conn.cursor()


create_tracks_table = """
CREATE TABLE IF NOT EXISTS tracks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL
);
"""

cursor.execute(create_tracks_table)
conn.close()