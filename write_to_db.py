import sqlite3
import os

conn = sqlite3.connect("track.sqlite")
cursor = conn.cursor()

selected_file = "test"

while not os.path.exists(r"C:\Users\alejon0910\PycharmProjects\playbackPrototype"+selected_file):
    selected_file = input("File: ")


insert_query = """
INSERT INTO
    tracks(filename)
VALUES
    (selected_file);
"""


cursor.execute(insert_query)
conn.commit()