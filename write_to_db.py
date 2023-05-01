import sqlite3
import os

conn = sqlite3.connect("track.sqlite")
cursor = conn.cursor()

selected_file = "test"

while not os.path.exists(r"C:\Users\bigal\PycharmProjects\playbackPrototype"+selected_file):
    selected_file = input("File: ")

selected_file = r"C:\Users\bigal\PycharmProjects\playbackPrototype"+selected_file


insert_query = """
INSERT INTO
    tracks(filename)
VALUES
    (?);
"""


cursor.execute(insert_query, (selected_file,))
conn.commit()