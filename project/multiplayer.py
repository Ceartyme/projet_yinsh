from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Mutliplayer:
    """
    Class Multiplayer: it is the class used to display the multiplayer screen.
    """

    def __init__(self,canva:Canvas,root:Tk, box:Canvas, turn:int, turn_player:Label) -> None:
        """
        Constructor of the class Multiplayer
        In there are defined a big part of the variables.
        """


        self.__w:int = root.winfo_screenwidth()
        self.__h:int = root.winfo_screenheight()


        self.__returnimage:Image = Image.open("img/buttons/return.png")
        self.__returnimage:Image = self.__returnimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnimage:PhotoImage = ImageTk.PhotoImage(self.__returnimage)

        self.__bg_canvas:Canvas = canva

        self.__box:Canvas = box
        self.__turn:int = turn
        self.__turn_player:int = turn_player

        self.__bg_canvas.tag_bind("return4_image", "<Button-1>", self.return_button_clicked)
        self.__bg_canvas.tag_bind("return4_image", "<Enter>", self.return_button_enter)
        self.__bg_canvas.tag_bind("return4_image", "<Leave>", self.return_button_leave)



        frame_width:int = self.__w - 100
        frame_height:int = self.__h - 100

        x1:int = 50
        y1:int = 50

        x2:int = x1 + frame_width
        y2:int = y1 + frame_height

        self.__bg_canvas.create_rectangle(x1, y1, x2, y2, fill="#E3D7FF",outline="#AFA2FF", width=10, tags="frame")
        self.__bg_canvas.create_image(self.__w/(2020/1000),self.__h-175, image=self.__returnimage, tags="return4_image")


        multiplayer_text:str =  """
                                  Not implemented yet.

                              Multiplayer coming soon!

                                        Stay tuned!
                            """

        self.__bg_canvas.create_text(self.__w/2.7, self.__h / 2.5, text=multiplayer_text, fill="black", font=("Helvetica", int(self.__w/(2020/50)), "bold"), tags="text")

    def return_button_clicked(self, event: Event) -> None:
        """
        Method called when the return button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """

        self.__bg_canvas.delete("return4_image","frame","text")

    def return_button_enter(self, event: Event) -> None:
        """
        Method called when you hover the return button

        Args:
            event (Event): contains all the informations of the hovering   
        """
        self.__returnhoverimage = Image.open("img/buttons/returnhover.png")
        self.__returnhoverimage=self.__returnhoverimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnhoverimage = ImageTk.PhotoImage(self.__returnhoverimage)
        self.__bg_canvas.itemconfig("return4_image", image=self.__returnhoverimage)

    def return_button_leave(self, event: Event) -> None:
        """
        Method called when you leave the return button

        Args:
            event (Event): contains all the informations of the leaving
        """
        self.__bg_canvas.itemconfig("return4_image", image=self.__returnimage)
