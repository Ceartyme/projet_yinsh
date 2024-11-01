from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Rules:
    
    def __init__(self,canva:Canvas,root:Tk, box:Canvas, turn_player:Label,mode:int=0) -> None:
        """
        Constructor of the class Rules
        In there are defined a big part of the variables.
        """

        self.__w:int = root.winfo_screenwidth()
        self.__h:int = root.winfo_screenheight()

        self.__croix_image:Image = Image.open("img/buttons/croix.png")
        self.__croix_image = self.__croix_image.resize((int(self.__w / (2020 / 90)), int(self.__h / (2020 / 150))))
        self.__croix_image:PhotoImage = ImageTk.PhotoImage(self.__croix_image)

        self.__bg_canvas:Canvas = canva
        self.__bg_canvas.create_image(self.__w /1.08, self.__h * 0.13, image=self.__croix_image, tags="croix_image")

        self.__root: Tk = root
        self.__box:Canvas = box
        self.__turn_player:Label = turn_player
        self.__mode:int=mode

        self.__bg_canvas.tag_bind("croix_image", "<Button-1>", self.quit_button_clicked)
        self.__bg_canvas.tag_bind("croix_image", "<Enter>", self.quit_button_enter)
        self.__bg_canvas.tag_bind("croix_image", "<Leave>", self.quit_button_leave)



        frame_width:int = self.__w - 100
        frame_height:int = self.__h - 100
        x1:int = 50
        y1:int = 50
        x2:int = x1 + frame_width
        y2:int = y1 + frame_height

        self.__bg_canvas.create_rectangle(x1, y1, x2, y2, fill="#E3D7FF",outline="#AFA2FF", width=10, tags="frame")
        self.__bg_canvas.create_image(self.__w /1.08, self.__h * 0.13, image=self.__croix_image, tags="croix_image")

        self.__ajout:str=("\n\tMode normal :" if mode==0 else "")+("\n\tThe game ends when a player has 3 victory rings\n"if (mode==0 or mode==1) else "")+("\n\tMode Blitz :" if mode==0 else "")+("\n\tThe game ends when a player makes a line of 5 rings\n"if (mode==0 or mode==2) else "")

        rules_text:str = """In the game, players take turns placing their colored rings on a hexagonal board. The game has two phases:

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
    
Phase 3: End of the Game
    """+self.__ajout

        self.__bg_canvas.create_text(self.__w//2, self.__h // 2, text=rules_text, fill="black", font=("Helvetica", int(self.__w/(2020/20)), "bold"), tags="text")

    def quit_button_clicked(self, event:Event) -> None:
        """
        Method called when the quit button is clicked

        Args:
            event (Event): Contains all the informations of the button clicking
        """
        self.__bg_canvas.delete("croix_image","frame","text")
        if self.__mode!=0:
            self.__box.pack()
            self.__turn_player.pack()

    def quit_button_enter(self, event:Event) -> None:
        """
        Method called when the quit button is hovered

        Args:
            event (Event): Contains all the informations of the button hovering
        """
        self.__croix_hover_image:Image = Image.open("img/buttons/croixhover.png")
        self.__croix_hover_image=self.__croix_hover_image.resize((int(self.__w/(2020/90)),int(self.__h/(2020/150))))
        self.__croix_hover_image:PhotoImage = ImageTk.PhotoImage(self.__croix_hover_image)
        self.__bg_canvas.itemconfig("croix_image", image=self.__croix_hover_image)

    def quit_button_leave(self, event:Event) -> None:
        """
        Method called when the quit button is not hovered

        Args:
            event (Event): Contains all the informations of the button hovering
        """
        self.__bg_canvas.itemconfig("croix_image", image=self.__croix_image)
