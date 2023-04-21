from just_playback import Playback
import tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(background="white")
        self.geometry("600x800")
        self.playback = Playback()
        self.button1 = tk.Button(self, text="Play!", width=50, height=10,
                                 command=lambda: self.play(r"Cheery Monday.mp3"))
        self.button2 = tk.Button(self, text="Play!", width=50, height=10,
                                 command=lambda: self.play(r"Monkeys Spinning Monkeys.mp3"))
        self.button1.place(x=100, y=100)
        self.button2.place(x=100, y=400)
    def play(self, filepath):
        self.playback.load_file(filepath)
        self.playback.play()

if __name__ == "__main__":
    menu = GUI()
    menu.mainloop()
    while 'normal' == menu.state():
        continue