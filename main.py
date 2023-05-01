from just_playback import Playback
import tkinter as tk
from tkinter import filedialog
import sqlite3
import os
import shutil


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.conn = sqlite3.connect("track.sqlite")
        self.cursor = self.conn.cursor()

        # Reset database and sounds directory
        self.cursor.execute("""DELETE FROM tracks;""")
        self.cursor.execute("""UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='tracks';""")
        self.conn.commit()

        for f in os.listdir(r"C:\Users\bigal\PycharmProjects\playbackPrototype\sounds"):
            os.remove(os.path.join(r"C:\Users\bigal\PycharmProjects\playbackPrototype\sounds", f))

        self.config(background="white")
        self.geometry("600x800")
        self.playback = Playback()

        self.button1 = tk.Button(self, text="Play File 1", width=50, height=10,
                                 command=lambda: [self.cursor.execute("""SELECT filename FROM tracks WHERE id=1"""), self.play(self.cursor.fetchall()[0][0])])
        self.button2 = tk.Button(self, text="Play File 2", width=50, height=10,
                                 command=lambda: [self.cursor.execute("""SELECT filename FROM tracks WHERE id=2"""), self.play(self.cursor.fetchall()[0][0])])
        self.button3 = tk.Button(self, text="Select Files", width=50, height=5,
                                 command=lambda: self.add())

        self.button1.place(x=100, y=100)
        self.button2.place(x=100, y=300)
        self.button3.place(x=100, y=500)

    def play(self, filepath):
        self.playback.load_file(filepath)
        self.playback.play()

    def add(self):

        self.file = filedialog.askopenfilename()
        self.basename = os.path.basename(self.file)
        shutil.copy(self.file, r"C:\Users\bigal\PycharmProjects\playbackPrototype\sounds")

        self.cursor.execute("""INSERT INTO tracks(filename) VALUES (?);""", (r"C:\Users\bigal\PycharmProjects\playbackPrototype\sounds"+(r"\""[0])+self.basename,))
        self.conn.commit()


if __name__ == "__main__":
    menu = GUI()
    menu.mainloop()
