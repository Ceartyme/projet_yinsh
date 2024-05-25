from tkinter import *
from math import sqrt

class Elements:
    def __init__(self,id:int,box_w:float,box_h:float,x:float,y:float,canva) :
        self._player_id = id
        self._color = "red" if self._player_id == 1 else "blue" if self._player_id == 2  else "grey" 
        self._box_dim=(box_w,box_h)
        self._coords=(x,y)
        self._radius=(self._box_dim[1]*0.95)/2
        self._side=sqrt((self._radius**2)*2)
        self._canva=canva
        
    def get_player(self) -> int :
        return self._player_id

    def get_box(self) -> tuple[int,int]:
        return (round(self._coords[0]/self._box_dim[0],0),round(self._coords[1]/self._box_dim[1],0))
    
    def get_coords(self) -> tuple[int,int]:
        return self._coords
    
    def get_box_size(self) -> tuple[int,int]:
        return self._box_dim
    
    
    def set_box(self,ligne,col) -> None:
        self._coords=(ligne*self._box_dim[0],col*self._box_dim[1])
        
    def set_coords(self,x,y) -> None:
        self._coords=(x,y)
        
    def change_player(self) -> None:
        self._player_id=3-self._player_id
        self._color = "red" if self._player_id == 1 else "blue"
        
        
class Pawn(Elements):
    def __init__(self, id :int ,canva,box_w,box_h,x,y,):
        super().__init__(id,box_w,box_h,x,y,canva)
        
        
    def draw(self) -> None:
        self._canva.create_oval(self._coords[0]-self._side+5,self._coords[1]-self._side+5,self._coords[0]+self._side-5,self._coords[1]+self._side-5,fill=self._color,outline='black', width=2   )
        
        
class Ring(Elements):
    def __init__(self, id,canva,box_w,box_h,x,y):
        super().__init__(id,box_w,box_h,x,y,canva)

        
    def draw(self) -> None:
        self._canva.create_oval(self._coords[0]-self._side,self._coords[1]-self._side,self._coords[0]+self._side,self._coords[1]+self._side,fill='',outline=self._color, width=5 )
            