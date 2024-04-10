from tkinter import *
from tkinter import messagebox
from Elements import Ring,Pawn
from Calculation import find_closer,position_in_list, get_index
from PIL import Image, ImageTk


class Game:
    def __init__(self,canva_lobby,root) -> None:
        self.__root = root
        
        
        
        self.__canva_window_width=self.__root.winfo_screenwidth()
        self.__canva_window_height=self.__root.winfo_screenheight()
        self.__canva_window=Canvas(canva_lobby,width=self.__canva_window_width,height=self.__canva_window_height, highlightthickness=0, background="black")
        self.__canva_window.pack(fill=BOTH, expand=True, anchor=NW)
        
        self.__canva_width=self.__root.winfo_screenwidth()/2.3
        self.__canva_height=self.__root.winfo_screenheight()/1.4
        self.__canva=Canvas(self.__canva_window, width=self.__canva_width, height=self.__canva_height,highlightthickness=0, background="black")
        self.__canva.pack()
        
        self.__canva.bind("<Button-1>",self.place)
        
        self.__box_heiht=self.__canva_height/20
        self.__box_width=self.__canva_width/12
        
        
        
        self.__rings_placed=False
        self.__pawn_placed=False
        self.__player_turn=1
        self.__pawn_list=[[],[]]
        self.__ring_list=[[],[]]
        self.__forbidden_list=[(3,19),(1,19),(2,18),(1,17),(1,15),(1,5),(1,3),(1,1),(2,2),(3,1),(9,1),(10,2),(11,1),(11,3),(11,5),(11,15),(11,19),(11,17),(10,18),(9,19)]
        self.__possible_list=[]
        self.__display_possible=True
        self.__line_list=[0,[]]
        
        self.update()
        
        
    def update(self):
        self.drawing_update()
        
    
    def drawing_update(self):
        self.__canva.delete('all')
        for i in range(2):
            for j in range(2):
                self.__canva.create_line(self.__canva_width*i+(-1)**i*2*self.__box_width,self.__canva_height*j+(-1)**j*4*self.__box_heiht,self.__canva_width*i+(-1)**i*5*self.__box_width,self.__canva_height*j+(-1)**j*1*self.__box_heiht,fill="white",width=2)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,self.__canva_height*j+(-1)**j*7*self.__box_heiht,self.__canva_width*i+(-1)**i*7*self.__box_width,self.__canva_height*j+(-1)**j*1*self.__box_heiht,fill="white",width=2)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,self.__canva_height*j+(-1)**j*9*self.__box_heiht,self.__canva_width*i+(-1)**i*8*self.__box_width,self.__canva_height*j+(-1)**j*2*self.__box_heiht,fill="white",width=2)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,self.__canva_height*j+(-1)**j*11*self.__box_heiht,self.__canva_width*i+(-1)**i*9*self.__box_width,self.__canva_height*j+(-1)**j*3*self.__box_heiht,fill="white",width=2)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,self.__canva_height*j+(-1)**j*13*self.__box_heiht,self.__canva_width*i+(-1)**i*10*self.__box_width,self.__canva_height*j+(-1)**j*4*self.__box_heiht,fill="white",width=2)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*2*self.__box_width,self.__canva_height*j+(-1)**j*14*self.__box_heiht,self.__canva_width*i+(-1)**i*10*self.__box_width,self.__canva_height*j+(-1)**j*6*self.__box_heiht,fill="white",width=2)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,13*self.__box_heiht,self.__canva_width*i+(-1)**i*1*self.__box_width,7*self.__box_heiht,fill="white",width=2)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*2*self.__box_width,16*self.__box_heiht,self.__canva_width*i+(-1)**i*2*self.__box_width,4*self.__box_heiht,fill="white",width=2)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*3*self.__box_width,17*self.__box_heiht,self.__canva_width*i+(-1)**i*3*self.__box_width,3*self.__box_heiht,fill="white",width=2)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*4*self.__box_width,18*self.__box_heiht,self.__canva_width*i+(-1)**i*4*self.__box_width,2*self.__box_heiht,fill="white",width=2)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*5*self.__box_width,19*self.__box_heiht,self.__canva_width*i+(-1)**i*5*self.__box_width,1*self.__box_heiht,fill="white",width=2)
        self.__canva.create_line(self.__canva_width*i+(-1)**i*6*self.__box_width,18*self.__box_heiht,self.__canva_width*i+(-1)**i*6*self.__box_width,2*self.__box_heiht,fill="white",width=2)
        for list in self.__pawn_list:
            for elem in list:
                elem.draw()
        for list in self.__ring_list:
            for elem in list:
                elem.draw()
        if self.__display_possible:
            for elem in self.__possible_list:
                Pawn(0,self.__canva,self.__box_width,self.__box_heiht,elem[0]*self.__box_width,elem[1]*self.__box_heiht).draw()
            
    def place(self, event):
        selected_x, selected_y= find_closer(event.x/self.__box_width, event.y/self.__box_heiht)
        selected_ring=False
        if (not (1<=selected_x<=11 and 1<=selected_y<=19))or (selected_x,selected_y) in self.__forbidden_list:
            return
        
        if not self.__rings_placed:
            if not (position_in_list(selected_x,selected_y,self.__ring_list[0]) or position_in_list(selected_x,selected_y,self.__ring_list[1])):
                ring=Ring(self.__player_turn,self.__canva,self.__box_width,self.__box_heiht,selected_x*self.__box_width,selected_y*self.__box_heiht)
                self.__ring_list[self.__player_turn-1].append(ring)
                self.update()
                self.__rings_placed= len(self.__ring_list[0])==5 and len(self.__ring_list[1])==5
                self.__player_turn= 3-self.__player_turn
        else :
            for elem in self.__ring_list[self.__player_turn-1]:
                if elem.get_box()==(selected_x,selected_y):
                    selected_ring=True 
            if selected_ring:
                if self.__pawn_placed:
                    del(self.__pawn_list[self.__player_turn-1][-1])
                    pawn = Pawn(self.__player_turn,self.__canva,self.__box_width,self.__box_heiht,selected_x*self.__box_width,selected_y*self.__box_heiht)
                    self.__pawn_list[self.__player_turn-1].append(pawn)
                    self.possible_move(selected_x,selected_y)
                    self.update()

                else:
                    pawn = Pawn(self.__player_turn,self.__canva,self.__box_width,self.__box_heiht,selected_x*self.__box_width,selected_y*self.__box_heiht)
                    self.__pawn_list[self.__player_turn-1].append(pawn)
                    self.possible_move(selected_x,selected_y)
                    self.update()
                    self.__pawn_placed=True
            elif self.__pawn_placed :
                if (selected_x,selected_y) in self.__possible_list:
                    self.__pawn_placed=False
                    previous_coords=self.__pawn_list[self.__player_turn-1][-1].get_box()
                    index = get_index(previous_coords[0],previous_coords[1],self.__ring_list[self.__player_turn-1])
                    self.__ring_list[self.__player_turn-1][index].set_box(selected_x,selected_y)
                    self.__possible_list=[]
                    self.exchange((selected_x,selected_y),previous_coords)
                    self.__player_turn=3-self.__player_turn
                    
                else :
                    del(self.__pawn_list[self.__player_turn-1][-1])
                    self.__pawn_placed=False
                    self.__possible_list=[]
                self.update()
                
    
    def possible_move(self,x : int,y : int):
        empty_found=False
        self.__possible_list=[]
        for i in range(2):
            for j in range (2):
                temp_x,temp_y=x,y
                while temp_x+1*(-1)**i>=1 and temp_x+1*(-1)**i<=11 and temp_y+1*(-1)**j>=1 and temp_y+1*(-1)**j<=19 and (temp_x+1*(-1)**i,temp_y+1*(-1)**j) not in self.__forbidden_list:
                    temp_x=temp_x+1*(-1)**i
                    temp_y=temp_y+1*(-1)**j
                    if position_in_list(temp_x,temp_y,self.__ring_list[0]) or position_in_list(temp_x,temp_y, self.__ring_list[1]):
                        break
                    elif position_in_list(temp_x,temp_y,self.__pawn_list[0]) or position_in_list(temp_x,temp_y, self.__pawn_list[1]):
                        while (not empty_found) and temp_x+1*(-1)**i>=1 and temp_x+1*(-1)**i<=11 and temp_y+1*(-1)**j>=1 and temp_y+1*(-1)**j<=19 and (temp_x+1*(-1)**i,temp_y+1*(-1)**j) not in self.__forbidden_list:
                            temp_x=temp_x+1*(-1)**i
                            temp_y=temp_y+1*(-1)**j
                            if position_in_list(temp_x,temp_y,self.__ring_list[0]) or position_in_list(temp_x,temp_y, self.__ring_list[1]):
                                break
                            elif position_in_list(temp_x,temp_y,self.__pawn_list[0]) or position_in_list(temp_x,temp_y, self.__pawn_list[1]):
                                pass
                            else :
                                empty_found=True
                                self.__possible_list.append((temp_x,temp_y))
                                break
                        empty_found=False
                        break
                    self.__possible_list.append((temp_x,temp_y))
    
    def exchange(self,new_coords : tuple[int,int],previous_coords : tuple[int,int]):
        x_change=-1 if new_coords[0]<previous_coords[0] else 1
        y_change=-1 if new_coords[1]<previous_coords[1] else 1
        previous_coords=previous_coords[0]+x_change,previous_coords[1]+y_change
        while previous_coords!=new_coords: 
            index1=get_index(previous_coords[0],previous_coords[1],self.__pawn_list[0])
            index2=get_index(previous_coords[0],previous_coords[1],self.__pawn_list[1])
            if index1!=-1:
                self.__pawn_list[0][index1].change_player()
                pawn=self.__pawn_list[0].pop(index1)
                self.__pawn_list[1].append(pawn)
            elif index2!=-1:
                self.__pawn_list[1][index2].change_player()
                pawn =self.__pawn_list[1].pop(index2)
                self.__pawn_list[0].append(pawn)
            previous_coords=previous_coords[0]+x_change,previous_coords[1]+y_change
        self.check_win()
            
            
    def check_win(self):
        self.__line_list=[0,[]]
        for arr in self.__pawn_list:
            for elem in arr:
                self.verif_line(elem , arr)
        if self.__line_list[0]!=0:
            print("il y a ",self.__line_list[0]," lignes")
            for i in range(self.__line_list[0]):
                print(self.__line_list[1][i])
    
    def verif_line(self,elem, arr):
        i=1
        temp=elem.get_box()
        coords=[temp[0],temp[1]]
        while i<5:
            coords[0],coords[1]=coords[0]+1,coords[1]+1
            if i==4 and position_in_list(coords[0],coords[1],arr):
                self.__line_list.append((elem.get_coords(),(coords[0],coords[1])))
                self.__line_list[1].append(elem.get_player())
                self.__line_list[0]+=1
            elif not position_in_list(coords[0],coords[1],arr):
                i=10
            i+=1
                
        i=1
        temp=elem.get_box()
        coords=[temp[0],temp[1]]
        while i<5:
            coords[0],coords[1]=coords[0]+1,coords[1]-1
            if i==4 and position_in_list(coords[0],coords[1],arr):
                self.__line_list.append((elem.get_coords(),(coords[0],coords[1])))
                self.__line_list[1].append(elem.get_player())
                self.__line_list[0]+=1
            elif not position_in_list(coords[0],coords[1],arr):
                i=10
            i+=1
            
            
        
            
            
            