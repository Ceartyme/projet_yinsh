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
    """
    Class Lobby: it is the lobby where the player can choose the game mode and start the game.
    In this class, there are mainly Tkinter method used.
    """
    def __init__(self):
        """
        Constructor of the class Lobby
        In there are defined a big part of the variables.
        """
        self.__root: Tk = Tk()
        self.__root.configure(bg='#000')
        self.__root.title = ("Yinsh")
        self.__root.attributes("-fullscreen", True)

        self.__w:int= self.__root.winfo_screenwidth()
        self.__h:int= self.__root.winfo_screenheight()

        self.__bgimage : Image = Image.open("img/bg/bglobby1.png")
        self.__bgimage=self.__bgimage.resize((self.__w+100,self.__h)) #2020 350/2020
        self.__bgimage1 : PhotoImage= ImageTk.PhotoImage(self.__bgimage) 

        self.__titleimage:Image = Image.open("img/bg/yinsh.png")
        self.__titleimage=self.__titleimage.resize((int(self.__w/2.3),int(self.__h/5)))
        self.__titleimage:PhotoImage = ImageTk.PhotoImage(self.__titleimage)

        self.__startimage:Image = Image.open("img/buttons/play.png")
        self.__startimage=self.__startimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225)))) #2020 340/120 
        self.__startimage1:PhotoImage = ImageTk.PhotoImage(self.__startimage) 
        
        self.__rulesimage:Image = Image.open("img/buttons/rules.png")
        self.__rulesimage=self.__rulesimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__rulesimage:PhotoImage = ImageTk.PhotoImage(self.__rulesimage)

        self.__leaveimage:Image = Image.open("img/buttons/leave.png")
        self.__leaveimage=self.__leaveimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__leaveimage1:PhotoImage = ImageTk.PhotoImage(self.__leaveimage)

        self.__bg_canva:Canvas = Canvas(self.__root,highlightthickness=0)
        self.__bg_canva.pack(fill=BOTH, expand=True)
        self.__bg_canva.create_image(-100,0,anchor=NW,image=self.__bgimage1)
        self.__bg_canva.create_image((self.__w-(self.__w/2.3))/2,self.__h/2/2,anchor=NW,image=self.__titleimage, tags="title_image")
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

        self.__bg_canva.tag_bind("return3_image", "<Button-1>", self.return3_button_clicked)
        self.__bg_canva.tag_bind("return3_image", "<Enter>", self.return3_button_hover)
        self.__bg_canva.tag_bind("return3_image", "<Leave>", self.return3_button_hoverl)

        self.__bg_canva.tag_bind("return4_image", "<Button-1>", self.return4_button_clicked)
        self.__bg_canva.tag_bind("return4_image", "<Enter>", self.return4_button_hover)
        self.__bg_canva.tag_bind("return4_image", "<Leave>", self.return4_button_hoverl)

        self.__bg_canva.tag_bind("players_image", "<Button-1>", self.players_button_clicked)
        self.__bg_canva.tag_bind("players_image", "<Enter>", self.players_button_hover)
        self.__bg_canva.tag_bind("players_image", "<Leave>", self.players_button_hoverl)        

        self.__bg_canva.tag_bind("bot_image", "<Button-1>", self.bot_button_clicked)
        self.__bg_canva.tag_bind("bot_image", "<Enter>", self.bot_button_hover)
        self.__bg_canva.tag_bind("bot_image", "<Leave>", self.bot_button_hoverl)

        self.__bg_canva.tag_bind("normal_image", "<Button-1>", self.normal_button_clicked)
        self.__bg_canva.tag_bind("normal_image", "<Enter>", self.normal_button_hover)
        self.__bg_canva.tag_bind("normal_image", "<Leave>", self.normal_button_hoverl)

        self.__bg_canva.tag_bind("blitz_image", "<Button-1>", self.blitz_button_clicked)
        self.__bg_canva.tag_bind("blitz_image", "<Enter>", self.blitz_button_hover)
        self.__bg_canva.tag_bind("blitz_image", "<Leave>", self.blitz_button_hoverl)




        self.__ai:bool=False
        
        self.__root.mainloop()




    def normal_button_clicked(self, event: Event) -> None:
        """
        Method called when the normal button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self.return3_button_clicked(event)
        self.return2_button_clicked(event)
        self.return1_button_clicked(event)
        Game(canva_lobby = self.__bg_canva,root=self.__root,blitz_mode=False,ai=self.__ai)

    def blitz_button_clicked(self,event: Event) -> None:
        """
        Method called when the blitz button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self.return3_button_clicked(event)
        self.return2_button_clicked(event)
        self.return1_button_clicked(event)
        Game(canva_lobby= self.__bg_canva,root=self.__root, blitz_mode=True,ai=self.__ai)

    def rules_button_clicked(self, event: Event) -> None:
        """
        Method called when the Rues button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        Rules(canva=self.__bg_canva,root=self.__root,box=None, turn=None, turn_player=None)

    def players_button_clicked(self, event: Event) -> None:
        """
        Method called when the 2 players button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self.__ai=False
        self.__bg_canva.delete("players_image", "bot_image", "return_image")

        self.__localimage:Image = Image.open("img/buttons/local.png")
        self.__localimage=self.__localimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__localimage:PhotoImage = ImageTk.PhotoImage(self.__localimage)

        self.__onlineimage:Image = Image.open("img/buttons/online.png")
        self.__onlineimage=self.__onlineimage.resize((int(self.__w/(2020/445)),int(self.__h/(2020/225))))
        self.__onlineimage:PhotoImage = ImageTk.PhotoImage(self.__onlineimage)

        self.__returnimage3:Image = Image.open("img/buttons/return.png")
        self.__returnimage3=self.__returnimage3.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnimage3:PhotoImage = ImageTk.PhotoImage(self.__returnimage3)

        self.__bg_canva.create_image(self.__w/(1980/350),self.__h-175, image=self.__localimage, tags="local_image")
        self.__bg_canva.create_image(self.__w/(1980/975),self.__h-175, image=self.__onlineimage, tags="online_image")
        self.__bg_canva.create_image(self.__w/(1980/1650),self.__h-175, image=self.__returnimage3, tags="return2_image")

        self.__bg_canva.tag_bind("local_image", "<Button-1>", self.local_button_clicked)
        self.__bg_canva.tag_bind("local_image", "<Enter>", self.local_button_hover)
        self.__bg_canva.tag_bind("local_image", "<Leave>", self.local_button_hoverl)

        self.__bg_canva.tag_bind("online_image", "<Button-1>", self.online_button_clicked)
        self.__bg_canva.tag_bind("online_image", "<Enter>", self.online_button_hover)
        self.__bg_canva.tag_bind("online_image", "<Leave>", self.online_button_hoverl)


    def bot_button_clicked(self, event: Event) -> None:
        """
        Method called when the Versus AI button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self.__ai = True
        self.__bg_canva.delete("players_image", "bot_image", "return_image")

        self.__normalimage:Image = Image.open("img/buttons/normal.png")
        self.__normalimage=self.__normalimage.resize((int(self.__w/(2020/445)),int(self.__h/(2020/225))))
        self.__normalimage:PhotoImage = ImageTk.PhotoImage(self.__normalimage)

        self.__blitzimage:Image = Image.open("img/buttons/blitz.png")
        self.__blitzimage=self.__blitzimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__blitzimage:PhotoImage = ImageTk.PhotoImage(self.__blitzimage)

        self.__returnimage4:Image = Image.open("img/buttons/return.png")
        self.__returnimage4=self.__returnimage4.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnimage4:PhotoImage = ImageTk.PhotoImage(self.__returnimage4)

        self.__bg_canva.create_image(self.__w/(1980/350),self.__h-175,image=self.__normalimage, tags="normal_image")
        self.__bg_canva.create_image(self.__w/(1980/1000),self.__h-175,image=self.__blitzimage, tags="blitz_image")
        self.__bg_canva.create_image(self.__w/(1980/1650),self.__h-175,image=self.__returnimage4, tags="return4_image")
        
    def start_button_clicked(self,event: Event) -> None:
        """
        Method called when the Play button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self.__bg_canva.delete("start_image", "rules_image", "leave_image")
    
        self.__playersimage:Image = Image.open("img/buttons/players.png")
        self.__playersimage=self.__playersimage.resize((int(self.__w/(2020/545)),int(self.__h/(2020/225))))
        self.__playersimage:PhotoImage = ImageTk.PhotoImage(self.__playersimage)

        self.__botimage:Image = Image.open("img/buttons/bot.png")
        self.__botimage=self.__botimage.resize((int(self.__w/(2020/400)),int(self.__h/(2020/225))))
        self.__botimage:PhotoImage = ImageTk.PhotoImage(self.__botimage)

        self.__returnimage:Image = Image.open("img/buttons/return.png")
        self.__returnimage=self.__returnimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnimage:PhotoImage = ImageTk.PhotoImage(self.__returnimage)

        self.__bg_canva.create_image(self.__w/(1980/350),self.__h-175, image=self.__playersimage, tags="players_image")
        self.__bg_canva.create_image(self.__w/(1980/1025),self.__h-175, image=self.__botimage, tags="bot_image")
        self.__bg_canva.create_image(self.__w/(1980/1650),self.__h-175, image=self.__returnimage, tags="return_image")

        

    def leave_button_clicked(self, event: Event) -> None:
        """
        Method called when the leave button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self.__root.destroy()

    def local_button_clicked(self, event: Event) -> None:
        """
        Method called when the local button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self.__bg_canva.delete("local_image", "online_image", "return2_image")

        self.__normalimage:Image = Image.open("img/buttons/normal.png")
        self.__normalimage=self.__normalimage.resize((int(self.__w/(2020/445)),int(self.__h/(2020/225))))
        self.__normalimage:PhotoImage = ImageTk.PhotoImage(self.__normalimage)

        self.__blitzimage:Image = Image.open("img/buttons/blitz.png")
        self.__blitzimage=self.__blitzimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__blitzimage:PhotoImage = ImageTk.PhotoImage(self.__blitzimage)


        self.__bg_canva.create_image(self.__w/(1980/350),self.__h-175,image=self.__normalimage, tags="normal_image")
        self.__bg_canva.create_image(self.__w/(1980/1000),self.__h-175,image=self.__blitzimage, tags="blitz_image")
        self.__bg_canva.create_image(self.__w/(1980/1650),self.__h-175,image=self.__returnimage, tags="return3_image")

    def online_button_clicked(self, event: Event) -> None:
        """
        Method called when the online button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        Mutliplayer(self.__bg_canva, self.__root, box = None, turn = None, turn_player = None)

    def return1_button_clicked(self, event: Event) -> None:
        """
        Method called when the first return button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """

        self.__bg_canva.delete("players_image", "bot_image", "return_image")

        self.__bg_canva.create_image(self.__w/(2020/400),self.__h-175,image=self.__startimage1, tags="start_image")
        self.__bg_canva.create_image(self.__w/(2020/1000),self.__h-175,image=self.__rulesimage, tags="rules_image")
        self.__bg_canva.create_image(self.__w/(2020/1600),self.__h-175,image=self.__leaveimage1, tags="leave_image")


    def return2_button_clicked(self, event: Event) -> None:
        """
        Method called when the second return button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """

        self.__bg_canva.delete("local_image", "online_image", "return2_image")

        self.__bg_canva.create_image(self.__w/(1980/350),self.__h-175, image=self.__playersimage, tags="players_image")
        self.__bg_canva.create_image(self.__w/(1980/1025),self.__h-175, image=self.__botimage, tags="bot_image")
        self.__bg_canva.create_image(self.__w/(1980/1650),self.__h-175, image=self.__returnimage, tags="return_image")



    def return3_button_clicked(self, event: Event) -> None:
        """
        Method called when the third return button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """

        self.__bg_canva.delete("normal_image", "blitz_image", "return3_image")

        self.__bg_canva.create_image(self.__w/(1980/350),self.__h-175, image=self.__localimage, tags="local_image")
        self.__bg_canva.create_image(self.__w/(1980/1000),self.__h-175, image=self.__onlineimage, tags="online_image")
        self.__bg_canva.create_image(self.__w/(1980/1650),self.__h-175, image=self.__returnimage, tags="return2_image")

    def return4_button_clicked(self, event: Event) -> None:
        """
        Method called when the fourth return button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """

        self.__bg_canva.delete("normal_image", "blitz_image", "return4_image")

        self.__bg_canva.create_image(self.__w/(1980/350),self.__h-175, image=self.__playersimage, tags="players_image")
        self.__bg_canva.create_image(self.__w/(1980/1000),self.__h-175, image=self.__botimage, tags="bot_image")
        self.__bg_canva.create_image(self.__w/(1980/1650),self.__h-175, image=self.__returnimage, tags="return2_image")





    def normal_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the nomal button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("normal_image", image=self.__normalimage)     

    def blitz_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the blitz button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("blitz_image", image=self.__blitzimage)    

    def rules_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the rules button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("rules_image", image=self.__rulesimage)

    def players_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the 2 Players button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("players_image", image=self.__playersimage)

    def bot_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the Versus Bot button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("bot_image", image=self.__botimage)

    def start_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the Play button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("start_image", image=self.__startimage1)

    def leave_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the leave button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("leave_image", image=self.__leaveimage1)

    def local_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the local button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("local_image", image=self.__localimage)

    def online_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the online button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("online_image", image=self.__onlineimage)

    def return1_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the first return button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("return_image", image=self.__returnimage) 

    def return2_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the second return button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("return2_image", image=self.__returnimage)

    def  return3_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the third return button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("return3_image", image=self.__returnimage)

    def return4_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the fourth return button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__bg_canva.itemconfig("return4_image", image=self.__returnimage)


    def local_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the local button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__localhoverimage:Image = Image.open("img/buttons/localhover.png")
        self.__localhoverimage=self.__localhoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__localhoverimage:PhotoImage = ImageTk.PhotoImage(self.__localhoverimage)
        self.__bg_canva.itemconfig("local_image", image=self.__localhoverimage)

    def online_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the online button

        Args:
            event (Event): contains all the informations of the hovering
        """
        self.__onlinehoverimage:Image = Image.open("img/buttons/onlinehover.png")
        self.__onlinehoverimage=self.__onlinehoverimage.resize((int(self.__w/(2020/445)),int(self.__h/(2020/225))))
        self.__onlinehoverimage:PhotoImage = ImageTk.PhotoImage(self.__onlinehoverimage)
        self.__bg_canva.itemconfig("online_image", image=self.__onlinehoverimage)

    def normal_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the normal button

        Args:
            event (Event): contains all the informations of the hovering
        """
        self.__normalhoverimage:Image = Image.open("img/buttons/normalhover.png")
        self.__normalhoverimage=self.__normalhoverimage.resize((int(self.__w/(2020/445)),int(self.__h/(2020/225))))
        self.__normalhoverimage:PhotoImage = ImageTk.PhotoImage(self.__normalhoverimage)
        self.__bg_canva.itemconfig("normal_image", image=self.__normalhoverimage)

    def blitz_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the blitz button

        Args:
            event (Event): contains all the informations of the hovering
        """
        self.__blitzhoverimage:Image = Image.open("img/buttons/blitzhover.png")
        self.__blitzhoverimage=self.__blitzhoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__blitzhoverimage:PhotoImage = ImageTk.PhotoImage(self.__blitzhoverimage)
        self.__bg_canva.itemconfig("blitz_image", image=self.__blitzhoverimage)

    def rules_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the Rules button

        Args:
            event (Event): contains all the informations of the hovering
        """
        self.__ruleshoverimage:Image = Image.open("img/buttons/ruleshover.png")
        self.__ruleshoverimage=self.__ruleshoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__ruleshoverimage:PhotoImage = ImageTk.PhotoImage(self.__ruleshoverimage)
        self.__bg_canva.itemconfig("rules_image", image=self.__ruleshoverimage)

    def players_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the 2 Players button

        Args:
            event (Event): contains all the informations of the hovering
        """
        self.__playershoverimage:Image = Image.open("img/buttons/playershover.png")
        self.__playershoverimage=self.__playershoverimage.resize((int(self.__w/(2020/545)),int(self.__h/(2020/225))))
        self.__playershoverimage:PhotoImage = ImageTk.PhotoImage(self.__playershoverimage)
        self.__bg_canva.itemconfig("players_image", image=self.__playershoverimage)
    
    def bot_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the Versus AI button

        Args:
            event (Event): contains all the informations of the hovering
        """
        self.__bothoverimage:Image = Image.open("img/buttons/bothover.png")
        self.__bothoverimage=self.__bothoverimage.resize((int(self.__w/(2020/400)),int(self.__h/(2020/225))))
        self.__bothoverimage:PhotoImage = ImageTk.PhotoImage(self.__bothoverimage)
        self.__bg_canva.itemconfig("bot_image", image=self.__bothoverimage)
    
    def start_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the Play button

        Args:
            event (Event): contains all the informations of the hovering
        """
        self.__starthoverimage:Image = Image.open("img/buttons/playhover.png")
        self.__starthoverimage=self.__starthoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225)))) #2020 340/120 
        self.__starthoverimage:PhotoImage = ImageTk.PhotoImage(self.__starthoverimage)
        self.__bg_canva.itemconfig("start_image", image=self.__starthoverimage)

    def leave_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the Leave button

        Args:
            event (Event): contains all the informations of the hovering
        """
        self.__leavehoverimage:Image = Image.open("img/buttons/leavehover.png")
        self.__leavehoverimage=self.__leavehoverimage.resize((int(self.__w/(2020/340)),int(self.__h/(2020/225))))
        self.__leavehoverimage:PhotoImage = ImageTk.PhotoImage(self.__leavehoverimage)
        self.__bg_canva.itemconfig("leave_image", image=self.__leavehoverimage)

    def return1_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the first return button

        Args:
            event (Event): contains all the informations of the hovering
        """
        self.__returnhoverimage:Image = Image.open("img/buttons/returnhover.png")
        self.__returnhoverimage=self.__returnhoverimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnhoverimage:PhotoImage = ImageTk.PhotoImage(self.__returnhoverimage)
        self.__bg_canva.itemconfig("return_image", image=self.__returnhoverimage)

    def return2_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the second return button

        Args:
            event (Event): contains all the informations of the hovering
        """
        self.__return2hoverimage:Image = Image.open("img/buttons/returnhover.png")
        self.__return2hoverimage=self.__return2hoverimage.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__return2hoverimage:PhotoImage = ImageTk.PhotoImage(self.__return2hoverimage)
        self.__bg_canva.itemconfig("return2_image", image=self.__return2hoverimage) 

    def return3_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the third return button

        Args:
            event (Event): contains all the informations of the hovering
        """
        self.__returnhoverimage3:Image = Image.open("img/buttons/returnhover.png")
        self.__returnhoverimage3=self.__returnhoverimage3.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnhoverimage3:PhotoImage = ImageTk.PhotoImage(self.__returnhoverimage3)

        self.__bg_canva.itemconfig("return3_image", image=self.__returnhoverimage3)

    def return4_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the fourth return button

        Args:
            event (Event): contains all the informations of the hovering
        """
        self.__returnhoverimage4:Image = Image.open("img/buttons/returnhover.png")
        self.__returnhoverimage4=self.__returnhoverimage4.resize((int(self.__w/(2020/440)),int(self.__h/(2020/225))))
        self.__returnhoverimage4:PhotoImage = ImageTk.PhotoImage(self.__returnhoverimage4)

        self.__bg_canva.itemconfig("return4_image", image=self.__returnhoverimage4)


lobby = Lobby()