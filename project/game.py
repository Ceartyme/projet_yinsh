from tkinter import *
from tkinter import messagebox
from Elements import Ring,Pawn
from Calculation import find_closer
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
        
        self.__canva.bind("<Button-1>",self.place)
        
        self.__box_heiht=self.__canva_height/20
        self.__box_width=self.__canva_width/12
        
        
        
        self.__rings_placed=False
        self.__player_turn=1
        self.__pawn_list=[[],[]]
        self.__ring_list=[[],[]]
        self.__forbidden_list=[(3,19),(1,19),(2,18),(1,17),(1,15),(1,5),(1,3),(1,1),(2,2),(3,1),(9,1),(10,2),(11,1),(11,3),(11,5),(11,15),(11,19),(11,17),(10,18),(9,19)]
        
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
        for list in self.__pawn_list:
            for elem in list:
                elem.draw()
        for list in self.__ring_list:
            for elem in list:
                elem.draw()
            
    def place(self, event):
        selected_x, selected_y= find_closer(event.x/self.__box_width, event.y/self.__box_heiht)
        if (not (1<=selected_x<=11 and 1<=selected_y<=19))or (selected_x,selected_y) in self.__forbidden_list:
            return
        
        if not self.__rings_placed:
            print(selected_x,selected_y)
            ring=Ring(self.__player_turn,self.__canva,self.__box_width,self.__box_heiht,selected_x*self.__box_width,selected_y*self.__box_heiht)
            print(ring.get_box())
            self.__ring_list[self.__player_turn-1].append(ring)
            self.update()
            self.__rings_placed= len(self.__ring_list)==10
        else :
            pawn = Pawn(self.__player_turn,self.__canva,self.__box_width,self.__box_heiht,selected_x*self.__box_width,selected_y*self.__box_heiht)
            self.__pawn_list[self.__player_turn-1].append(pawn)
            self.update()
            
            
            
        self.__player_turn= 3-self.__player_turn
            
            
            