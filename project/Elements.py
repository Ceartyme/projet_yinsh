from tkinter import *
from math import sqrt

class Elements:
    """
    Parent class of the rings and the pawns
    """
    def __init__(self,id:int,box_w:float,box_h:float,x:float,y:float,canva:Canvas) :
        """
        Constructor method of the parent class

        Args:
            id (int): id of the player
            box_w (float): width of a box in the board
            box_h (float): height of a box in the board
            x (float): x coord of the element
            y (float): y coord of the element 
            canva (_type_): canva on which the element is drawn
        """
        self._player_id:int = id
        self._color:str = "red" if self._player_id == 1 else "blue" if self._player_id == 2  else "grey" 
        self._box_dim:tuple[float,float]=(box_w,box_h)
        self._coords:tuple[float,float]=(x,y)
        self._radius:float=(self._box_dim[1]*0.95)/2
        self._side:float=sqrt((self._radius**2)*2)
        self._canva:Canvas=canva
        
    def get_player(self) -> int :
        """
        Function that let you get the id of the player

        Returns:
            int: the id of the player
        """
        return self._player_id

    def get_box(self) -> tuple[int,int]:
        """
        Function that let you get the box where the element is

        Returns:
            tuple[int,int]: indices of the box
        """
        return (round(self._coords[0]/self._box_dim[0],0),round(self._coords[1]/self._box_dim[1],0))
    
    def get_coords(self) -> tuple[int,int]:
        """
        Function that let you get the coords of the element

        Returns:
            tuple[int,int]: coords of the element
        """
        return self._coords
    
    def get_box_size(self) -> tuple[int,int]:
        """
        Function that let you get the size of the box

        Returns:
            tuple[int,int]: tuple containing the width and the height of a box
        """
        return self._box_dim
    
    
    def set_box(self,ligne:int,col:int) -> None:
        """
        Set the element in the box with indices (x,y)

        Args:
            ligne (int): x coordinate of the box
            col (int): y coordinate of the box
        """
        self._coords=(ligne*self._box_dim[0],col*self._box_dim[1])
        
    def set_coords(self,x:int,y:int) -> None:
        """
        Set the coords of the element

        Args:
            x (int): x coordinate of the element
            y (int): y coordinate of the element
        """
        self._coords=(x,y)
        
    def change_player(self) -> None:
        """
        Method to change the player of a pawn
        """
        self._player_id=3-self._player_id
        self._color = "red" if self._player_id == 1 else "blue"
        
        
class Pawn(Elements):
    """
    Class of the pawns

    This class is a subclass of the Elements class
    """
    def __init__(self, id :int ,canva:Canvas,box_w:float,box_h:float,x:float,y:float):
        """
        Constructor method of the Pawn class

        Args:
            id (int): id of the player
            canva (_type_): canva on which the element is drawn
            box_w (float): width of a box in the board
            box_h (float): height of a box in the board
            x (float): x coord of the element
            y (float): y coord of the element 
        """
        super().__init__(id,box_w,box_h,x,y,canva)
        
        
    def draw(self) -> None:
        """
        Method that draw the element on the canva
        """
        self._canva.create_oval(self._coords[0]-self._side+5,self._coords[1]-self._side+5,self._coords[0]+self._side-5,self._coords[1]+self._side-5,fill=self._color,outline='black', width=2   )
        
        
class Ring(Elements):
    """
    Class of the rings
    
    This class is a subclass of the Elements class
    """
    def __init__(self, id,canva,box_w,box_h,x,y):
        """
        Constructor method of the Ring class

        Args:
            id (int): id of the player
            canva (_type_): canva on which the element is drawn
            box_w (float): width of a box in the board
            box_h (float): height of a box in the board
            x (float): x coord of the element
            y (float): y coord of the element 
        """
        super().__init__(id,box_w,box_h,x,y,canva)

        
    def draw(self) -> None:
        """
        Method that draw the element on the canva
        """
        self._canva.create_oval(self._coords[0]-self._side,self._coords[1]-self._side,self._coords[0]+self._side,self._coords[1]+self._side,fill='',outline=self._color, width=5 )
            