import tkinter as tk


class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer test")
        self.master.geometry("400x300")
        self.remaining_time = 6

        self.time_label = tk.Label(self.master, text=str(self.remaining_time))
        self.time_label.pack()

        self.update_time()
        self.master.mainloop()

    def update_time(self):
        if self.remaining_time > 1:
            self.remaining_time -= 1 
            self.time_label.configure(text=str(self.remaining_time))
            self.master.after(1000, self.update_time)
        else :
            self.start_text = "The game is started..."
            self.time_label.configure(text=self.start_text)


root = tk.Tk()
timer = Timer(root)
