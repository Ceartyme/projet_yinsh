import tkinter as tk
from datetime import datetime


class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer test")
        self.master.geometry("400x300")
        self.time_elapsed = datetime.now()

        self.time_label = tk.Label(self.master, text="00:00:00")
        self.time_label.pack()

        self.update_time()
        self.master.mainloop()

    def update_time(self):
        self.current_time = datetime.now()
        self.time_difference = self.current_time - self.time_elapsed
        time_text = str(self.time_difference).split(".")[0]

        self.time_label.configure(text=time_text)
        self.master.after(1000, self.update_time)


root = tk.Tk()
timer = Timer(root)