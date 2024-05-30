from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Rules:
    
    def __init__(self,canva,root, box, turn, turn_player):


        self.__w = root.winfo_screenwidth()
        self.__h = root.winfo_screenheight()


        self.__croiximage = Image.open("img/buttons/croix.png")
        self.__croiximage = self.__croiximage.resize((int(self.__w / (2020 / 90)), int(self.__h / (2020 / 150))))
        self.__croiximage = ImageTk.PhotoImage(self.__croiximage)

        self.__bg_canvas = canva
        self.__bg_canvas.create_image(self.__w /1.08, self.__h * 0.13, image=self.__croiximage, tags="croix_image")

        self.__box = box
        self.__turn = turn
        self.__turn_player = turn_player

        self.__bg_canvas.tag_bind("croix_image", "<Button-1>", self.quit_button_clicked)
        self.__bg_canvas.tag_bind("croix_image", "<Enter>", self.quit_button_enter)
        self.__bg_canvas.tag_bind("croix_image", "<Leave>", self.quit_button_leave)



        frame_width = self.__w - 100
        frame_height = self.__h - 100

        x1 = 50
        y1 = 50

        x2 = x1 + frame_width
        y2 = y1 + frame_height

        self.__bg_canvas.create_rectangle(x1, y1, x2, y2, fill="#E3D7FF",outline="#AFA2FF", width=10, tags="frame")
        self.__bg_canvas.create_image(self.__w /1.08, self.__h * 0.13, image=self.__croiximage, tags="croix_image")


        rules_text = """In the game, players take turns placing their colored rings on a hexagonal board. The game has two phases:

Phase 1: Placing Rings

    Starting with the red player, each player places one of their rings on a free intersection of the board.

Phase 2: Moving Rings

    Players take turns moving one of their rings.
        - Choose a ring to move and place a piece of the player's color in its center.
        - Move the ring in a straight line, stopping at a free intersection.
        - The ring can pass over free or occupied intersections but not other rings.
        - When passing over pawns, stop at the first free intersection.
        - Turn over passed pieces.
    If a player forms a line of five of their pieces, they remove them and score a point by placing one of their rings on the edge circles.
    The game ends when a player has three victory rings."""

        self.__bg_canvas.create_text(self.__w//2, self.__h // 2, text=rules_text, fill="black", font=("Helvetica", int(self.__w/(2020/20)), "bold"), tags="text")

    def quit_button_clicked(self, event):
        self.__bg_canvas.delete("croix_image","frame","text")
        self.__box.pack()
        self.__turn.pack(pady=5)
        self.__turn_player.pack()

    def quit_button_enter(self, event):
        self.__croixhoverimage = Image.open("img/buttons/croixhover.png")
        self.__croixhoverimage=self.__croixhoverimage.resize((int(self.__w/(2020/90)),int(self.__h/(2020/150))))
        self.__croixhoverimage = ImageTk.PhotoImage(self.__croixhoverimage)
        self.__bg_canvas.itemconfig("croix_image", image=self.__croixhoverimage)

    def quit_button_leave(self, event):
        self.__bg_canvas.itemconfig("croix_image", image=self.__croiximage)
