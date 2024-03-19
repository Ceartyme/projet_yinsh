import tkinter as tk


class Turn:
    def __init__(self, master):
        self.master = master
        self.master.title("turn test")
        self.master.geometry("400x300")


        self.turn_label = tk.Label(self.master)
        self.turn_player_label = tk.Label(self.master)

        self.turn_player_label.pack()
        self.turn_label.pack()

        self.turn_counter = 1

        self.turn_label.configure(text="turn : " + str(self.turn_counter))
        
        player_color = "Red" if self.turn_counter % 2 == 0 else "Blue"
        self.turn_player_label.configure(text="Player : " + player_color)

        self.turn_button = tk.Button(self.master, text="Next", command=self.update_turn)
        self.turn_button.pack()

        self.master.mainloop()

    def update_turn(self):
        self.turn_counter += 1
        self.turn_label.configure(text="turn : " + str(self.turn_counter))

        player_color = "Red" if self.turn_counter % 2 == 0 else "Blue"
        self.turn_player_label.configure(text="Player : " + player_color)



        
root = tk.Tk()
turnr = Turn(root)