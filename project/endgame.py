from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class EndGameRed():
    
    def __init__(self,canva,root):


        self.__w = root.winfo_screenwidth()
        self.__h = root.winfo_screenheight()


        self.__redwin = Image.open("img/bg/redwin.png")
        self.__redwin = self.__redwin.resize((int(self.__w/2.3),int(self.__h/3.2)))
        self.__redwin = ImageTk.PhotoImage(self.__redwin)

        self.__bg_canvas = canva
        self.__bg_canvas.create_image(self.__w /2, self.__h / 2, image=self.__redwin, tags="redwin_image")

        frame_width = self.__w - 100
        frame_height = self.__h - 100

        x1 = 50
        y1 = 50

        x2 = x1 + frame_width
        y2 = y1 + frame_height

        self.__bg_canvas.create_rectangle(x1, y1, x2, y2, fill="#E3D7FF",outline="#AFA2FF", width=10, tags="frame")
        self.__bg_canvas.create_image(self.__w /2, self.__h / 2, image=self.__redwin, tags="redwin_image")

        self.__menuimage = Image.open("img/buttons/menu.png")
        self.__menuimage=self.__menuimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__menuimage = ImageTk.PhotoImage(self.__menuimage)

        self.__bg_canvas.create_image(self.__w/(2020/1000),self.__h-175,image=self.__menuimage, tags="menu_image")

        self.__bg_canvas.tag_bind("menu_image", "<Button-1>", self.menu_button_clicked)
        self.__bg_canvas.tag_bind("menu_image", "<Enter>", self.menu_button_enter)
        self.__bg_canvas.tag_bind("menu_image", "<Leave>", self.menu_button_leave)

    def menu_button_clicked(self, event):
        self.__bg_canvas.destroy()

    def menu_button_enter(self, event):
        self.__menuhoverimage = Image.open("img/buttons/menuhover.png")
        self.__menuhoverimage=self.__menuhoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__menuhoverimage = ImageTk.PhotoImage(self.__menuhoverimage)
        self.__bg_canvas.itemconfig("menu_image", image=self.__menuhoverimage)

    def menu_button_leave(self, event):
        self.__bg_canvas.itemconfig("menu_image", image=self.__menuimage)

class EndGameBlue():
    
    def __init__(self,canva,root):


        self.__w = root.winfo_screenwidth()
        self.__h = root.winfo_screenheight()


        self.__bluewin = Image.open("img/bg/bluewin.png")
        self.__bluewin = self.__bluewin.resize((int(self.__w/2.3),int(self.__h/3.2)))
        self.__bluewin = ImageTk.PhotoImage(self.__bluewin)

        self.__bg_canvas = canva
        self.__bg_canvas.create_image(self.__w /2, self.__h / 2, image=self.__bluewin, tags="bluewin_image")

        frame_width = self.__w - 100
        frame_height = self.__h - 100

        x1 = 50
        y1 = 50

        x2 = x1 + frame_width
        y2 = y1 + frame_height

        self.__bg_canvas.create_rectangle(x1, y1, x2, y2, fill="#E3D7FF",outline="#AFA2FF", width=10, tags="frame")
        self.__bg_canvas.create_image(self.__w /2, self.__h / 2, image=self.__bluewin, tags="bluewin_image")

        self.__menuimage = Image.open("img/buttons/menu.png")
        self.__menuimage=self.__menuimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__menuimage = ImageTk.PhotoImage(self.__menuimage)

        self.__bg_canvas.create_image(self.__w/(2020/1000),self.__h-175,image=self.__menuimage, tags="menu_image")

        self.__bg_canvas.tag_bind("menu_image", "<Button-1>", self.menu_button_clicked)
        self.__bg_canvas.tag_bind("menu_image", "<Enter>", self.menu_button_enter)
        self.__bg_canvas.tag_bind("menu_image", "<Leave>", self.menu_button_leave)

    def menu_button_clicked(self, event):
        self.__bg_canvas.destroy()

    def menu_button_enter(self, event):
        self.__menuhoverimage = Image.open("img/buttons/menuhover.png")
        self.__menuhoverimage=self.__menuhoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__menuhoverimage = ImageTk.PhotoImage(self.__menuhoverimage)
        self.__bg_canvas.itemconfig("menu_image", image=self.__menuhoverimage)

    def menu_button_leave(self, event):
        self.__bg_canvas.itemconfig("menu_image", image=self.__menuimage)

