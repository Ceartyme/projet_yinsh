from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Rules:
    
    def __init__(self,canva,root,start,rules,leave):

        self.__start = start
        self.__rules = rules
        self.__leave = leave

        self.__w = root.winfo_screenwidth()
        self.__h = root.winfo_screenheight()


        self.__croiximage = Image.open("img/buttons/croix.png")
        self.__croiximage = self.__croiximage.resize((int(self.__w / (2020 / 90)), int(self.__h / (2020 / 150))))
        self.__croiximage = ImageTk.PhotoImage(self.__croiximage)

        self.__bg_canvas = canva
        self.__bg_canvas.create_image(self.__w /1.08, self.__h * 0.13, image=self.__croiximage, tags="croix_image")

        self.__bg_canvas.tag_bind("croix_image", "<Button-1>", self.quit_button_clicked)
        self.__bg_canvas.tag_bind("croix_image", "<Enter>", self.quit_button_enter)
        self.__bg_canvas.tag_bind("croix_image", "<Leave>", self.quit_button_leave)



        frame_width = self.__w - 100
        frame_height = self.__h - 100

        x1 = 50
        y1 = 50

        x2 = x1 + frame_width
        y2 = y1 + frame_height

        self.__bg_canvas.create_rectangle(x1, y1, x2, y2, fill="#E3D7FF", stipple="gray50" ,outline="#E3D7FF", width=10, tags="frame")
        self.__bg_canvas.create_image(self.__w /1.08, self.__h * 0.13, image=self.__croiximage, tags="croix_image")


        rules_text = """To start the game :
Place the board in the centre of the table. Each player chooses their colour: black or white.

The game turn :
Phase 1: placing the rings on the board

In turn, starting with the white player, each player places a ring of their own colour on a free intersection of the board.

Phase 2: moving the rings

White starts. In turn, each player must move one of their rings according to the following rules:

- Choose the ring to move
- The player chooses one of his rings on the board.
- Place a piece of your colour in the centre of the ring.
- The player takes a piece from the reserve and places it in the centre of the ring.
- The visible side of the piece must be the player's colour.
- Move the ring
- The player must move the ring in a straight line in one of the six directions, stopping at a free intersection.
- As it moves, the ring may pass over intersections that are free or occupied by pawns. However, the ring cannot pass over other rings.
- As long as the ring is flying over free intersections, the player can move the ring and stop it on the intersection of his choice. 
   However, as soon as the ring flies over one or more pawns, the player must stop it on the first free intersection immediately after the rings it flies over.
- Turning over the pieces over which the ring has passed
- The player must then turn over all the pieces over which the ring has passed.
- Solving lines of five checkers of the same colour
- If a player completes a line-up of five pieces of the same colour, he must remove the five pieces from the board and return them to the reserve. 
   To score his victory point, he must then remove one of his rings from the board (the one he has just moved or any other) and place it on one of the 3 circles at the edge of the board.
- If the alignment contains more than five pieces, the player removes five contiguous pieces of his choice.
- If several alignments of the player's colour are created, the player may resolve them in any order.
- If an opponent's line-up is created, the player first solves his own line-up before letting the opponent solve his.
- End of the game
- As soon as a player has three victory rings, he wins the game."""

        self.__bg_canvas.create_text(self.__w//2, self.__h // 2, text=rules_text, fill="black", font=("Helvetica", int(2020/175), "bold"), tags="text")

    def quit_button_clicked(self, event):
        self.__bg_canvas.delete("croix_image","frame","text")

        self.__bg_canvas.create_image(self.__w/(2020/400),self.__h-175,image=self.__start, tags="start_image")
        self.__bg_canvas.create_image(self.__w/(2020/1000),self.__h-175,image=self.__rules, tags="rules_image")
        self.__bg_canvas.create_image(self.__w/(2020/1600),self.__h-175,image=self.__leave, tags="leave_image")

    def quit_button_enter(self, event):
        self.__croixhoverimage = Image.open("img/buttons/croixhover.png")
        self.__croixhoverimage=self.__croixhoverimage.resize((int(self.__w/(2020/90)),int(self.__h/(2020/150))))
        self.__croixhoverimage = ImageTk.PhotoImage(self.__croixhoverimage)
        self.__bg_canvas.itemconfig("croix_image", image=self.__croixhoverimage)

    def quit_button_leave(self, event):
        self.__bg_canvas.itemconfig("croix_image", image=self.__croiximage)

