from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class EndGame():
    """
    Class parent used to display the win screen
    """
    def __init__(self,canva:Canvas,root:Tk):
        """
        Constructor of the class

        Args:
            canva (Canvas): Canva on which the screen is drawn
            root (Tk): Main window of the game
        """
        self._w:int = root.winfo_screenwidth()
        self._h:int = root.winfo_screenheight()
        self.__frame_width:int = self._w- 100
        self.__frame_height:int = self._h - 100
        self._x1:int = 50
        self._y1:int = 50
        self._x2:int = self._x1 + self.__frame_width
        self._y2:int = self._y1 + self.__frame_height

        self._root = root
        self._bg_canvas:Canvas = canva

        self.__menu_image:Image = Image.open("img/buttons/menu.png")
        self.__menu_image=self.__menu_image.resize((int(self._w/(2020/340)),int(self._h/(2020/225))))
        self.__menu_image:PhotoImage = ImageTk.PhotoImage(self.__menu_image)
        
        self._bg_canvas.create_rectangle(self._x1, self._y1, self._x2, self._y2, fill="#E3D7FF",outline="#AFA2FF", width=10, tags="frame")
        self._bg_canvas.create_image(self._w/(2020/1000),self._h-175,image=self.__menu_image, tags="menu_image")

        self._bg_canvas.tag_bind("menu_image", "<Button-1>", self.menu_button_clicked)
        self._bg_canvas.tag_bind("menu_image", "<Enter>", self.menu_button_enter)
        self._bg_canvas.tag_bind("menu_image", "<Leave>", self.menu_button_leave)

    def menu_button_clicked(self, event:Event):
        """
        Method called when the menu button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self._bg_canvas.destroy()

    def menu_button_enter(self, event:Event):
        """
        Method that will be called when the mouse hover the menu button in order to modify its appearance

        Args:
            event (Event): contains all the informations of the button hovering
        """
        self.__menu_hover_image:Image = Image.open("img/buttons/menuhover.png")
        self.__menu_hover_image=self.__menu_hover_image.resize((int(self._w/(2020/340)),int(self._h/(2020/225))))
        self.__menu_hover_image:PhotoImage = ImageTk.PhotoImage(self.__menu_hover_image)
        
        self._bg_canvas.itemconfig("menu_image", image=self.__menu_hover_image)

    def menu_button_leave(self, event:Event):
        """
        Method that will be called when the mouse leave the menu button in order to modify its appearance

        Args:
            event (Event): contains all the informations of the button hovering
        """
        self._bg_canvas.itemconfig("menu_image", image=self.__menu_image)



class EndGameRed(EndGame):
    """
    Class used to display the red win screen
    This class inherits from the EndGame class
    """
    def __init__(self,canva:Canvas,root:Tk):
        """
        Constructor of the class

        Args:
            canva (Canvas): Canva on which the screen is drawn
            root (Tk): Main window of the game
        """
        super().__init__(canva,root)
        
        self.__red_win:Image = Image.open("img/bg/redwin.png")
        self.__red_win = self.__red_win.resize((int(self._w/2.3),int(self._h/3.2)))
        self.__red_win:PhotoImage = ImageTk.PhotoImage(self.__red_win) 
        
        self._bg_canvas.create_image(self._w/2, self._h / 2, image=self.__red_win, tags="redwin_image")

class EndGameBlue(EndGame):
    """
    Class used to display the blue win screen
    This class inherits from the EndGame class
    """
    def __init__(self,canva,root):
        """
        Constructor of the class

        Args:
            canva (Canvas): Canva on which the screen is drawn
            root (Tk): Main window of the game
        """
        super().__init__(canva,root)

        self.__blue_win:Image = Image.open("img/bg/bluewin.png")
        self.__blue_win = self.__blue_win.resize((int(self._w/2.3),int(self._h/3.2)))
        self.__blue_win:PhotoImage = ImageTk.PhotoImage(self.__blue_win)
        
        self._bg_canvas.create_image(self._w/2, self._h / 2, image=self.__blue_win, tags="bluewin_image")

class EndGameDraw(EndGame):
    """
    Class used to display the draw screen
    This class inherits from the EndGame class
    """
    def __init__(self,canva,root):
        """
        Constructor of the class

        Args:
            canva (Canvas): Canva on which the screen is drawn
            root (Tk): Main window of the game
        """
        super().__init__(canva,root)

        self.__draw:Image = Image.open("img/bg/draw.png")
        self.__draw = self.__draw.resize((int(self._w/2.3),int(self._h/3.2)))
        self.__draw:PhotoImage = ImageTk.PhotoImage(self.__draw)
        
        self._bg_canvas.create_image(self._w/2, self._h / 2, image=self.__draw, tags="draw_image")