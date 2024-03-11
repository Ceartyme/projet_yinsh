from tkinter import *
from math import sqrt

class Elements:
    def __init__(self,id:int,box_w:float,box_h:float,x:float,y:float,canva) :
        self._player_id = id
        self._color = "red" if self._player_id == 1 else "blue"
        self._box_dim=(box_w,box_h)
        self._coords=(x,y)
        self._radius=(self._box_dim[1]*0.9)/2
        self._side=sqrt((self._radius**2)*2)
        self._canva=canva
        
    def get_player(self):
        return self._player_id

    def get_box(self):
        return (self._coords[0]/self._box_dim[0],self._coords[1]/self._box_dim[1])
    
    def get_coords(self):
        return self._coords
    
    def get_box_size(self):
        return self._box_dim
    
    
    def set_box(self,ligne,col):
        self._coords=(col*self._box_dim[0],ligne*self._box_dim[1])
        
    def set_coords(self,x,y):
        self._coords=(x,y)
        
    def change_player(self):
        self._player_id=3-self._player_id
        self._color = "red" if self._player_id == 1 else "blue"
        
        
class Pawn(Elements):
    def __init__(self, id,canva,box_w,box_h,x,y):
        super().__init__(id,box_w,box_h,x,y,canva)
        
        
    def draw(self):
        self._canva.create_oval(self._coords[0]-self._side,self._coords[1]-self._side,self._coords[0]+self._side,self._coords[1]+self._side,fill=self._color,outline='black', width=2   )
        
        
class Ring(Elements):
    def __init__(self, id,canva,box_w,box_h,x,y):
        super().__init__(id,box_w,box_h,x,y,canva)

        
    def draw(self):
        self._canva.create_oval(self._coords[0]-self._side,self._coords[1]-self._side,self._coords[0]+self._side,self._coords[1]+self._side,fill='',outline=self._color, width=5 )
            