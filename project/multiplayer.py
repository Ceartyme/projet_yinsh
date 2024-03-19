from game import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time

class Multiplayer:

    def __init__(self, canva ,root, normal, blitz, return1):

        self.__red = 256
        self.__blue = 256
        self.__green = 256

        self.__return = return1
        self.__normal = normal
        self.__blitz = blitz
        self.__bg_canvas = canva
        self.__root = root

        self.__w = root.winfo_screenwidth()
        self.__h = root.winfo_screenheight()

        self.__bgimage = Image.open("img/bg/test.gif")
        self.__bgimage=self.__bgimage.resize((self.__w+100,self.__h)) #2020 350/2020
        self.__bgimage1 = ImageTk.PhotoImage(self.__bgimage) 

        self.__localimage = Image.open("img/buttons/local.png")
        self.__localimage = self.__localimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__localimage = ImageTk.PhotoImage(self.__localimage)
        
        self.__hostimage = Image.open("img/buttons/host.png")
        self.__hostimage = self.__hostimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__hostimage = ImageTk.PhotoImage(self.__hostimage)

        self.__joinimage = Image.open("img/buttons/join.png")
        self.__joinimage = self.__joinimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__joinimage = ImageTk.PhotoImage(self.__joinimage)

        self.__returnimage = Image.open("img/buttons/return.png")
        self.__returnimage=self.__returnimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnimage = ImageTk.PhotoImage(self.__returnimage)

        self.__bg_canvas.create_image(self.__w/(2020/400),self.__h-600, image=self.__localimage, tags="local_image")
        self.__bg_canvas.create_image(self.__w/(2020/1000),self.__h-600, image=self.__hostimage, tags="host_image")
        self.__bg_canvas.create_image(self.__w/(2020/1600),self.__h-600, image=self.__joinimage, tags="join_image")
        self.__bg_canvas.create_image(self.__w/(1980/1000),self.__h-175, image=self.__returnimage, tags="return3_image")

        self.__bg_canvas.tag_bind("local_image", "<Button-1>", self.local_button_clicked)
        self.__bg_canvas.tag_bind("local_image", "<Enter>", self.local_button_enter)
        self.__bg_canvas.tag_bind("local_image", "<Leave>", self.local_button_leave)

        self.__bg_canvas.tag_bind("host_image", "<Button-1>", self.host_button_clicked)
        self.__bg_canvas.tag_bind("host_image", "<Enter>", self.host_button_enter)
        self.__bg_canvas.tag_bind("host_image", "<Leave>", self.host_button_leave)

        self.__bg_canvas.tag_bind("join_image", "<Button-1>", self.join_button_clicked)
        self.__bg_canvas.tag_bind("join_image", "<Enter>", self.join_button_enter)
        self.__bg_canvas.tag_bind("join_image", "<Leave>", self.join_button_leave)

        self.__bg_canvas.tag_bind("return3_image", "<Button-1>", self.return3_button_clicked)
        self.__bg_canvas.tag_bind("return3_image", "<Enter>", self.return3_button_enter)
        self.__bg_canvas.tag_bind("return3_image", "<Leave>", self.return3_button_leave)

    def local_button_clicked(self, event):
        self.__bg_canvas.delete("join_image", "local_image", "return3_image", "host_image","frame")

        Game(self.__bg_canvas,self.__root)

        
    def host_button_clicked(self, event):
        self.__bg_canvas.delete("join_image", "local_image", "return3_image", "host_image","frame")

        self.__bg_canvas.create_image(self.__w/(2020/1000),self.__h-175,image=self.__return, tags="return5_image")

        host_text = "Your code is"

        self.__bg_canvas.create_rectangle(self.__w//2-150,self.__h/2.5-30, self.__w//2+150, self.__h/2.5+25, fill="#E3D7FF",outline="#AFA2FF", width=5 ,tags="frame")
        self.__bg_canvas.create_text(self.__w//2,self.__h/2.5, text=host_text, font=("Helvetica", int(self.__w / (2020 / 30)), "bold"), fill="black", tags="text")

        self.__bg_canvas.tag_bind("return5_image", "<Button-1>", self.return5_button_clicked)
        self.__bg_canvas.tag_bind("return5_image", "<Enter>", self.return5_button_enter)
        self.__bg_canvas.tag_bind("return5_image", "<Leave>", self.return5_button_leave) 

    def join_button_clicked(self, event):
        self.__bg_canvas.delete("join_image", "local_image", "return3_image", "host_image","frame")

        self.__bg_canvas.create_image(self.__w/(1980/725),self.__h-175,image=self.__joinimage, tags="join_image")
        self.__bg_canvas.create_image(self.__w/(1980/1225),self.__h-175,image=self.__return, tags="return4_image")

        self.__bg_canvas.tag_bind("return4_image", "<Button-1>", self.return4_button_clicked)
        self.__bg_canvas.tag_bind("return4_image", "<Enter>", self.return4_button_enter)
        self.__bg_canvas.tag_bind("return4_image", "<Leave>", self.return4_button_leave)

        join_text = "Enter the code"       

        self.__bg_canvas.create_text(self.__w//2, self.__h // 2.5, text=join_text, fill="black", font=("Helvetica", int(self.__w/(2020/30)), "bold"), tags="text")

        self.__entry = Entry(self.__bg_canvas)
        self.__entry.config(font=('Arial', 20), justify=CENTER, bg="#E3D7FF", fg="black", insertbackground="black", relief="flat", borderwidth=5, highlightthickness=5, highlightbackground="#AFA2FF")
        self.__entry.place(x = self.__w // 3,y= self.__h // 2, width=self.__w/3,height=self.__h/15)

    def return5_button_clicked(self, event):
        self.__bg_canvas.delete("return5_image","frame", "text")
        
        self.__bg_canvas.create_image(self.__w/(2020/400),self.__h-600, image=self.__localimage, tags="local_image")
        self.__bg_canvas.create_image(self.__w/(2020/1000),self.__h-600, image=self.__hostimage, tags="host_image")
        self.__bg_canvas.create_image(self.__w/(2020/1600),self.__h-600, image=self.__joinimage, tags="join_image")
        self.__bg_canvas.create_image(self.__w/(1980/1000),self.__h-175, image=self.__returnimage, tags="return3_image")

    def return4_button_clicked(self, event):
        self.__bg_canvas.delete("join_image", "return4_image","frame","text")
        self.__entry.destroy()

        self.__bg_canvas.create_image(self.__w/(2020/400),self.__h-600, image=self.__localimage, tags="local_image")
        self.__bg_canvas.create_image(self.__w/(2020/1000),self.__h-600, image=self.__hostimage, tags="host_image")
        self.__bg_canvas.create_image(self.__w/(2020/1600),self.__h-600, image=self.__joinimage, tags="join_image")
        self.__bg_canvas.create_image(self.__w/(1980/1000),self.__h-175, image=self.__returnimage, tags="return3_image")

    def return3_button_clicked(self, event):
        self.__bg_canvas.delete("join_image", "local_image", "return3_image", "host_image","frame")

        self.__bg_canvas.create_image(self.__w/(1980/350),self.__h-175,image=self.__normal, tags="normal_image")
        self.__bg_canvas.create_image(self.__w/(1980/1025),self.__h-175,image=self.__blitz, tags="blitz_image")
        self.__bg_canvas.create_image(self.__w/(1980/1650),self.__h-175,image=self.__return, tags="return2_image")


    def local_button_enter(self, event):
        self.__localhoverimage = Image.open("img/buttons/localhover.png")
        self.__localhoverimage=self.__localhoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__localhoverimage = ImageTk.PhotoImage(self.__localhoverimage)
        self.__bg_canvas.itemconfig("local_image", image=self.__localhoverimage)

    def local_button_leave(self, event):
        self.__bg_canvas.itemconfig("local_image", image=self.__localimage)

    def host_button_enter(self, event):
        self.__hosthoverimage = Image.open("img/buttons/hosthover.png")
        self.__hosthoverimage=self.__hosthoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__hosthoverimage = ImageTk.PhotoImage(self.__hosthoverimage)
        self.__bg_canvas.itemconfig("host_image", image=self.__hosthoverimage)

    def host_button_leave(self, event):
        self.__bg_canvas.itemconfig("host_image", image=self.__hostimage)

    def join_button_enter(self, event):
        self.__joinhoverimage = Image.open("img/buttons/joinhover.png")
        self.__joinhoverimage=self.__joinhoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__joinhoverimage = ImageTk.PhotoImage(self.__joinhoverimage)
        self.__bg_canvas.itemconfig("join_image", image=self.__joinhoverimage)

    def join_button_leave(self, event):
        self.__bg_canvas.itemconfig("join_image", image=self.__joinimage)

    def return3_button_enter(self, event):
        self.__returnhoverimage = Image.open("img/buttons/returnhover.png")
        self.__returnhoverimage=self.__returnhoverimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnhoverimage = ImageTk.PhotoImage(self.__returnhoverimage)
        self.__bg_canvas.itemconfig("return3_image", image=self.__returnhoverimage)

    def return3_button_leave(self, event):

        self.__bg_canvas.itemconfig("return3_image", image=self.__returnimage)

    def return4_button_enter(self, event):
        self.__returnhoverimage = Image.open("img/buttons/returnhover.png")
        self.__returnhoverimage=self.__returnhoverimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnhoverimage = ImageTk.PhotoImage(self.__returnhoverimage)
        self.__bg_canvas.itemconfig("return4_image", image=self.__returnhoverimage)

    def return4_button_leave(self, event):

        self.__bg_canvas.itemconfig("return4_image", image=self.__returnimage)

    def return5_button_enter(self, event):
        self.__returnhoverimage = Image.open("img/buttons/returnhover.png")
        self.__returnhoverimage=self.__returnhoverimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnhoverimage = ImageTk.PhotoImage(self.__returnhoverimage)
        self.__bg_canvas.itemconfig("return5_image", image=self.__returnhoverimage)

    def return5_button_leave(self, event):

        self.__bg_canvas.itemconfig("return5_image", image=self.__returnimage)
