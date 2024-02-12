from tkinter import *
from tkinter import messagebox
from Elements import Ring,Pawn
from PIL import Image, ImageTk

class Game:
    def __init__(self,canva_lobby,root) -> None:
        self.__root = root
        
        
        
        self.__canva_window_width=self.__root.winfo_screenwidth()
        self.__canva_window_height=self.__root.winfo_screenheight()
        self.__canva_window=Canvas(canva_lobby,width=self.__canva_window_width,height=self.__canva_window_height, highlightthickness=0, background="black")
        self.__canva_window.pack(fill=BOTH, expand=True, anchor=NW)
        
        self.__canva_width=self.__root.winfo_screenwidth()/2.3
        self.__canva_height=self.__root.winfo_screenheight()/1.5
        self.__canva=Canvas(self.__canva_window, width=self.__canva_width, height=self.__canva_height,highlightthickness=0, background="white")
        self.__canva.pack()
        
        self.__box_heiht=self.__canva_height/20
        self.__box_width=self.__canva_width/12
        ring=Ring(2,self.__canva,self.__box_width,self.__box_heiht,0,0)
        ring.set_box(8,6)
        self.__ring_list=[ring]
        pawn=Pawn(1,self.__canva,self.__box_width,self.__box_heiht,0,0)
        pawn.set_box(3,5)
        self.__pawn_list=[pawn]
        
        self.update()
        
          
    def update(self):
        self.drawing_update()
    
    def drawing_update(self):
        self.__canva.delete('all')
        for i in range(2):
            for j in range(2):
                self.__canva.create_line(self.__canva_width*i+(-1)**i*2*self.__box_width,self.__canva_height*j+(-1)**j*4*self.__box_heiht,self.__canva_width*i+(-1)**i*5*self.__box_width,self.__canva_height*j+(-1)**j*1*self.__box_heiht,fill="black",width=2)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,self.__canva_height*j+(-1)**j*7*self.__box_heiht,self.__canva_width*i+(-1)**i*7*self.__box_width,self.__canva_height*j+(-1)**j*1*self.__box_heiht,fill="black",width=2)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,self.__canva_height*j+(-1)**j*9*self.__box_heiht,self.__canva_width*i+(-1)**i*8*self.__box_width,self.__canva_height*j+(-1)**j*2*self.__box_heiht,fill="black",width=2)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,self.__canva_height*j+(-1)**j*11*self.__box_heiht,self.__canva_width*i+(-1)**i*9*self.__box_width,self.__canva_height*j+(-1)**j*3*self.__box_heiht,fill="black",width=2)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,self.__canva_height*j+(-1)**j*13*self.__box_heiht,self.__canva_width*i+(-1)**i*10*self.__box_width,self.__canva_height*j+(-1)**j*4*self.__box_heiht,fill="black",width=2)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*2*self.__box_width,self.__canva_height*j+(-1)**j*14*self.__box_heiht,self.__canva_width*i+(-1)**i*10*self.__box_width,self.__canva_height*j+(-1)**j*6*self.__box_heiht,fill="black",width=2)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,13*self.__box_heiht,self.__canva_width*i+(-1)**i*1*self.__box_width,7*self.__box_heiht,fill="black",width=2)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*2*self.__box_width,16*self.__box_heiht,self.__canva_width*i+(-1)**i*2*self.__box_width,4*self.__box_heiht,fill="black",width=2)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*3*self.__box_width,17*self.__box_heiht,self.__canva_width*i+(-1)**i*3*self.__box_width,3*self.__box_heiht,fill="black",width=2)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*4*self.__box_width,18*self.__box_heiht,self.__canva_width*i+(-1)**i*4*self.__box_width,2*self.__box_heiht,fill="black",width=2)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*5*self.__box_width,19*self.__box_heiht,self.__canva_width*i+(-1)**i*5*self.__box_width,1*self.__box_heiht,fill="black",width=2)
        self.__canva.create_line(self.__canva_width*i+(-1)**i*6*self.__box_width,18*self.__box_heiht,self.__canva_width*i+(-1)**i*6*self.__box_width,2*self.__box_heiht,fill="black",width=2)
        for elem in self.__pawn_list:
            elem.draw()
        for elem in self.__ring_list:
            elem.draw()