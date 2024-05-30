from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Mutliplayer:
    
    def __init__(self,canva,root, box, turn, turn_player):


        self.__w = root.winfo_screenwidth()
        self.__h = root.winfo_screenheight()


        self.__returnimage = Image.open("img/buttons/return.png")
        self.__returnimage = self.__returnimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnimage = ImageTk.PhotoImage(self.__returnimage)

        self.__bg_canvas = canva

        self.__box = box
        self.__turn = turn
        self.__turn_player = turn_player

        self.__bg_canvas.tag_bind("return4_image", "<Button-1>", self.return_button_clicked)
        self.__bg_canvas.tag_bind("return4_image", "<Enter>", self.return_button_enter)
        self.__bg_canvas.tag_bind("return4_image", "<Leave>", self.return_button_leave)



        frame_width = self.__w - 100
        frame_height = self.__h - 100

        x1 = 50
        y1 = 50

        x2 = x1 + frame_width
        y2 = y1 + frame_height

        self.__bg_canvas.create_rectangle(x1, y1, x2, y2, fill="#E3D7FF",outline="#AFA2FF", width=10, tags="frame")
        self.__bg_canvas.create_image(self.__w/(2020/1000),self.__h-175, image=self.__returnimage, tags="return4_image")


        multiplayer_text =  """
                                  Not implemented yet.

                              Multiplayer coming soon!

                                        Stay tuned!
                            """

        self.__bg_canvas.create_text(self.__w/2.7, self.__h / 2.5, text=multiplayer_text, fill="black", font=("Helvetica", int(self.__w/(2020/50)), "bold"), tags="text")

    def return_button_clicked(self, event):
        self.__bg_canvas.delete("return4_image","frame","text")

    def return_button_enter(self, event):
        self.__returnhoverimage = Image.open("img/buttons/returnhover.png")
        self.__returnhoverimage=self.__returnhoverimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnhoverimage = ImageTk.PhotoImage(self.__returnhoverimage)
        self.__bg_canvas.itemconfig("return4_image", image=self.__returnhoverimage)

    def return_button_leave(self, event):
        self.__bg_canvas.itemconfig("return4_image", image=self.__returnimage)
