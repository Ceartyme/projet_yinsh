from rules import *
from game import *
from multiplayer import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from pygame import mixer
import pygame

    


class Lobby:

    def __init__(self):
        self.__root = Tk()
        self.__root.configure(bg='#000')
        self.__root.title = ("Yinsh")
        self.__root.attributes("-fullscreen", True)

        self.__w= self.__root.winfo_screenwidth()
        self.__h= self.__root.winfo_screenheight()

        self.__bgimage = Image.open("img/bg/test.gif")
        self.__bgimage=self.__bgimage.resize((self.__w+100,self.__h)) #2020 350/2020
        self.__bgimage1 = ImageTk.PhotoImage(self.__bgimage) 

        self.__titleimage = Image.open("img/bg/yinsh.png")
        self.__titleimage=self.__titleimage.resize((int(self.__w/2.3),int(self.__h/5)))
        self.__titleimage = ImageTk.PhotoImage(self.__titleimage)

        self.__startimage = Image.open("img/buttons/test.png")
        self.__startimage=self.__startimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225)))) #2020 340/120 
        self.__startimage1 = ImageTk.PhotoImage(self.__startimage) 
        
        self.__rulesimage = Image.open("img/buttons/rules.png")
        self.__rulesimage=self.__rulesimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__rulesimage = ImageTk.PhotoImage(self.__rulesimage)

        self.__leaveimage = Image.open("img/buttons/leave.png")
        self.__leaveimage=self.__leaveimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__leaveimage1 = ImageTk.PhotoImage(self.__leaveimage)

        self.__bg_canva = Canvas(self.__root,highlightthickness=0)
        self.__bg_canva.pack(fill=BOTH, expand=True)
        self.__bg_canva.create_image(-100,0,anchor=NW,image=self.__bgimage1)
        self.__bg_canva.create_image(self.__w/2/2,self.__h/2/2,anchor=NW,image=self.__titleimage, tags="title_image")
        self.__bg_canva.create_image(self.__w/(2020/400),self.__h-175,image=self.__startimage1, tags="start_image")
        self.__bg_canva.create_image(self.__w/(2020/1000),self.__h-175,image=self.__rulesimage, tags="rules_image")
        self.__bg_canva.create_image(self.__w/(2020/1600),self.__h-175,image=self.__leaveimage1, tags="leave_image")

        self.__bg_canva.tag_bind("start_image", "<Button-1>", self.start_button_clicked)
        self.__bg_canva.tag_bind("start_image", "<Enter>", self.start_button_hover)
        self.__bg_canva.tag_bind("start_image", "<Leave>", self.start_button_hoverl)

        self.__bg_canva.tag_bind("rules_image", "<Button-1>", self.rules_button_clicked)
        self.__bg_canva.tag_bind("rules_image", "<Enter>", self.rules_button_hover)
        self.__bg_canva.tag_bind("rules_image", "<Leave>", self.rules_button_hoverl)

        self.__bg_canva.tag_bind("leave_image", "<Button-1>", self.leave_button_clicked)
        self.__bg_canva.tag_bind("leave_image", "<Enter>", self.leave_button_hover)
        self.__bg_canva.tag_bind("leave_image", "<Leave>", self.leave_button_hoverl)

        self.__bg_canva.tag_bind("return_image", "<Button-1>", self.return1_button_clicked)
        self.__bg_canva.tag_bind("return_image", "<Enter>", self.return1_button_hover)
        self.__bg_canva.tag_bind("return_image", "<Leave>", self.return1_button_hoverl)

        self.__bg_canva.tag_bind("return2_image", "<Button-1>", self.return2_button_clicked)
        self.__bg_canva.tag_bind("return2_image", "<Enter>", self.return2_button_hover)
        self.__bg_canva.tag_bind("return2_image", "<Leave>", self.return2_button_hoverl)

        self.__bg_canva.tag_bind("players_image", "<Button-1>", self.players_button_clicked)
        self.__bg_canva.tag_bind("players_image", "<Enter>", self.players_button_hover)
        self.__bg_canva.tag_bind("players_image", "<Leave>", self.players_button_hoverl)        

        self.__bg_canva.tag_bind("bot_image", "<Button-1>", self.players_button_clicked)
        self.__bg_canva.tag_bind("bot_image", "<Enter>", self.bot_button_hover)
        self.__bg_canva.tag_bind("bot_image", "<Leave>", self.bot_button_hoverl)

        self.__bg_canva.tag_bind("normal_image", "<Button-1>", self.normal_button_clicked)
        self.__bg_canva.tag_bind("normal_image", "<Enter>", self.normal_button_hover)
        self.__bg_canva.tag_bind("normal_image", "<Leave>", self.normal_button_hoverl)

        self.__bg_canva.tag_bind("blitz_image", "<Button-1>", self.blitz_button_clicked)
        self.__bg_canva.tag_bind("blitz_image", "<Enter>", self.blitz_button_hover)
        self.__bg_canva.tag_bind("blitz_image", "<Leave>", self.blitz_button_hoverl)

        self.__root.mainloop()

    def button_sound(self):
        pygame.init()
        pygame.mixer.init()
        son = pygame.mixer.Sound('music/game_start.mp3')
        channel = pygame.mixer.Channel(1)
        channel.play(son)

    def start_button_clicked(self,event):
        self.__bg_canva.delete("start_image", "rules_image", "leave_image")
    
        self.__playersimage = Image.open("img/buttons/players.png")
        self.__playersimage=self.__playersimage.resize((int(self.__w/(2020/545)),int(self.__h/(2020/225))))
        self.__playersimage = ImageTk.PhotoImage(self.__playersimage)

        self.__botimage = Image.open("img/buttons/bot.png")
        self.__botimage=self.__botimage.resize((int(self.__w/(2020/400)),int(self.__h/(2020/225))))
        self.__botimage = ImageTk.PhotoImage(self.__botimage)

        self.__returnimage = Image.open("img/buttons/return.png")
        self.__returnimage=self.__returnimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnimage = ImageTk.PhotoImage(self.__returnimage)

        self.__bg_canva.create_image(self.__w/(1980/350),self.__h-175, image=self.__playersimage, tags="players_image")
        self.__bg_canva.create_image(self.__w/(1980/1025),self.__h-175, image=self.__botimage, tags="bot_image")
        self.__bg_canva.create_image(self.__w/(1980/1650),self.__h-175, image=self.__returnimage, tags="return_image")

    def rules_button_clicked(self, event):
        self.__bg_canva.delete("start_image", "rules_image", "leave_image")
        Rules(canva=self.__bg_canva,root=self.__root,start=self.__startimage1, rules=self.__rulesimage, leave=self.__leaveimage1)
        
    def leave_button_clicked(self, event):
        self.__root.destroy()

    def return1_button_clicked(self, event):
        self.__bg_canva.delete("players_image", "bot_image", "return_image")

        self.__bg_canva.create_image(self.__w/(2020/400),self.__h-175,image=self.__startimage1, tags="start_image")
        self.__bg_canva.create_image(self.__w/(2020/1000),self.__h-175,image=self.__rulesimage, tags="rules_image")
        self.__bg_canva.create_image(self.__w/(2020/1600),self.__h-175,image=self.__leaveimage1, tags="leave_image")

    def players_button_clicked(self, event):
        self.__bg_canva.delete("players_image", "bot_image", "return_image")

        self.__normalimage = Image.open("img/buttons/normal.png")
        self.__normalimage=self.__normalimage.resize((int(self.__w/(2020/445)),int(self.__h/(2020/225))))
        self.__normalimage = ImageTk.PhotoImage(self.__normalimage)

        self.__blitzimage = Image.open("img/buttons/blitz.png")
        self.__blitzimage=self.__blitzimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__blitzimage = ImageTk.PhotoImage(self.__blitzimage)

        self.__returnimage2 = Image.open("img/buttons/return.png")
        self.__returnimage2=self.__returnimage2.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnimage2 = ImageTk.PhotoImage(self.__returnimage2)

        self.__bg_canva.create_image(self.__w/(1980/350),self.__h-175,image=self.__normalimage, tags="normal_image")
        self.__bg_canva.create_image(self.__w/(1980/1000),self.__h-175,image=self.__blitzimage, tags="blitz_image")
        self.__bg_canva.create_image(self.__w/(1980/1650),self.__h-175,image=self.__returnimage2, tags="return2_image")

    def return2_button_clicked(self, event):
        self.__bg_canva.delete("normal_image", "blitz_image", "return2_image")

        self.__bg_canva.create_image(self.__w/(1980/350),self.__h-175,image=self.__playersimage, tags="players_image")
        self.__bg_canva.create_image(self.__w/(1980/1025),self.__h-175,image=self.__botimage, tags="bot_image")
        self.__bg_canva.create_image(self.__w/(1980/1650),self.__h-175,image=self.__returnimage, tags="return_image")

    def normal_button_clicked(self, event):
        self.button_sound()
        self.__bg_canva.delete("normal_image", "blitz_image", "return2_image", "title_image")
        
        Multiplayer(canva = self.__bg_canva,root=self.__root,normal=self.__normalimage, blitz=self.__blitzimage, return1=self.__returnimage2)

    def blitz_button_clicked(self,event):
        self.button_sound()
        self.__bg_canva.delete("normal_image", "blitz_image", "return2_image", "title_image")       

        Multiplayer(canva = self.__bg_canva,root=self.__root,normal=self.__normalimage, blitz=self.__blitzimage, return1=self.__returnimage2)

    def start_button_hover(self, event):
        self.__starthoverimage = Image.open("img/buttons/playhover.png")
        self.__starthoverimage=self.__starthoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225)))) #2020 340/120 
        self.__starthoverimage = ImageTk.PhotoImage(self.__starthoverimage)
        self.__bg_canva.itemconfig("start_image", image=self.__starthoverimage)

    def start_button_hoverl(self, event):
        self.__bg_canva.itemconfig("start_image", image=self.__startimage1)

    def rules_button_hover(self, event):
        self.__ruleshoverimage = Image.open("img/buttons/ruleshover.png")
        self.__ruleshoverimage=self.__ruleshoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__ruleshoverimage = ImageTk.PhotoImage(self.__ruleshoverimage)
        self.__bg_canva.itemconfig("rules_image", image=self.__ruleshoverimage)

    def rules_button_hoverl(self, event):
        self.__bg_canva.itemconfig("rules_image", image=self.__rulesimage)

    def leave_button_hover(self, event):
        self.__leavehoverimage = Image.open("img/buttons/leavehover.png")
        self.__leavehoverimage=self.__leavehoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__leavehoverimage = ImageTk.PhotoImage(self.__leavehoverimage)
        self.__bg_canva.itemconfig("leave_image", image=self.__leavehoverimage)

    def leave_button_hoverl(self, event):
        self.__bg_canva.itemconfig("leave_image", image=self.__leaveimage1)

    def return1_button_hover(self, event):
        self.__returnhoverimage = Image.open("img/buttons/returnhover.png")
        self.__returnhoverimage=self.__returnhoverimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnhoverimage = ImageTk.PhotoImage(self.__returnhoverimage)
        self.__bg_canva.itemconfig("return_image", image=self.__returnhoverimage)

    def return1_button_hoverl(self, event):
        self.__bg_canva.itemconfig("return_image", image=self.__returnimage) 
        
    def bot_button_hover(self, event):
        self.__bothoverimage = Image.open("img/buttons/bothover.png")
        self.__bothoverimage=self.__bothoverimage.resize((int(self.__w/(2020/400)),int(self.__h/(2020/225))))
        self.__bothoverimage = ImageTk.PhotoImage(self.__bothoverimage)
        self.__bg_canva.itemconfig("bot_image", image=self.__bothoverimage)

    def bot_button_hoverl(self, event):
        self.__bg_canva.itemconfig("bot_image", image=self.__botimage)

    def return2_button_hover(self, event):
        self.__return2hoverimage = Image.open("img/buttons/returnhover.png")
        self.__return2hoverimage=self.__return2hoverimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__return2hoverimage = ImageTk.PhotoImage(self.__return2hoverimage)
        self.__bg_canva.itemconfig("return2_image", image=self.__return2hoverimage)

    def return2_button_hoverl(self, event):
        self.__bg_canva.itemconfig("return2_image", image=self.__returnimage)

    def players_button_hover(self, event):
        self.__playershoverimage = Image.open("img/buttons/playershover.png")
        self.__playershoverimage=self.__playershoverimage.resize((int(self.__w/(2020/545)),int(self.__h/(2020/225))))
        self.__playershoverimage = ImageTk.PhotoImage(self.__playershoverimage)
        self.__bg_canva.itemconfig("players_image", image=self.__playershoverimage)

    def players_button_hoverl(self, event):
        self.__bg_canva.itemconfig("players_image", image=self.__playersimage)

    def normal_button_hover(self, event):
        self.__normalhoverimage = Image.open("img/buttons/normalhover.png")
        self.__normalhoverimage=self.__normalhoverimage.resize((int(self.__w/(2020/445)),int(self.__h/(2020/225))))
        self.__normalhoverimage = ImageTk.PhotoImage(self.__normalhoverimage)
        self.__bg_canva.itemconfig("normal_image", image=self.__normalhoverimage)

    def normal_button_hoverl(self, event):
        self.__bg_canva.itemconfig("normal_image", image=self.__normalimage)     

    def blitz_button_hover(self, event):
        self.__blitzhoverimage = Image.open("img/buttons/blitzhover.png")
        self.__blitzhoverimage=self.__blitzhoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__blitzhoverimage = ImageTk.PhotoImage(self.__blitzhoverimage)
        self.__bg_canva.itemconfig("blitz_image", image=self.__blitzhoverimage)

    def blitz_button_hoverl(self, event):
        self.__bg_canva.itemconfig("blitz_image", image=self.__blitzimage)    



lobby = Lobby()