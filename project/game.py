from tkinter import *
from tkinter import messagebox
from Elements import Ring,Pawn
import Calculation as calc
from PIL import Image, ImageTk
import random as rd


class Game:
    def __init__(self,canva_lobby,root) -> None:
        self.__root = root
        self.__blitz_mode= False
        self.__ai=True
        
        self.__canva_window_width=self.__root.winfo_screenwidth()
        self.__canva_window_height=self.__root.winfo_screenheight()
        self.__canva_window=Canvas(canva_lobby,width=self.__canva_window_width,height=self.__canva_window_height, highlightthickness=0, background="black")
        self.__canva_window.pack(fill=BOTH, expand=True, anchor=NW)
        
        self.__canva_width=self.__root.winfo_screenwidth()/2.3
        self.__canva_height=self.__root.winfo_screenheight()/1.4
        self.__canva=Canvas(self.__canva_window, width=self.__canva_width, height=self.__canva_height,highlightthickness=0, background="black")
        self.__canva.pack()
        
        self.__canva.bind("<Button-1>",self.click)
        
        
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
        self.__selecting_ring=False
        self.__selecting_line=False
        self.__player_selecting=0
        self.__endGame=False
        self.__previousHover=(0,0)
        self.__previousLine=((0,0),(0,0))
        
        self.update()
        
        
    def update(self):
        self.drawing_update()
        if self.__endGame:
            self.__canva.unbind("<Button-1>")
        
    
    def move(self,event):
        hover=calc.find_closer(event.x/self.__box_width, event.y/self.__box_heiht)
        if self.__selecting_line and hover!=self.__previousHover:
            self.__previousHover=hover
            self.findLine(hover)
            self.update()
    
    def findLine(self,hover):
        for elem in self.__line_list[2:]:
            if hover==calc.get_middle(elem[0][0][0],elem[0][0][1],elem[0][1][0],elem[0][1][1]) and elem[1]==self.__player_selecting:
                self.__previousLine=elem[0]
                return
        for elem in self.__line_list[2:]:
            if hover in calc.get_around_middle(elem[0][0][0],elem[0][0][1],elem[0][1][0],elem[0][1][1]) and elem[1]==self.__player_selecting:
                self.__previousLine=elem[0]
                return
        for elem in self.__line_list[2:] :
            if (float(hover[0]),float(hover[1])) in elem[0] and elem[1]==self.__player_selecting :
                self.__previousLine=elem[0]
                return
        self.__previousLine=((0,0),(0,0))
    
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
        if self.__previousLine!=((0,0),(0,0)) and self.__selecting_line:
            self.__canva.create_line(self.__previousLine[0][0]*self.__box_width,self.__previousLine[0][1]*self.__box_heiht,self.__previousLine[1][0]*self.__box_width,self.__previousLine[1][1]*self.__box_heiht,fill="green",width=4)
        
    def click(self,event):
        selected_x, selected_y= calc.find_closer(event.x/self.__box_width, event.y/self.__box_heiht)
        if self.__selecting_ring:
            if self.selectRing(selected_x,selected_y):
                for i in range (2):
                    if len(self.__ring_list[i])==2:
                        print("J"+str(i+1)+" gagne")
                        self.__endGame=True
                        self.update()
                self.check_ligne()
        elif self.__selecting_line and self.__previousLine!=((0,0),(0,0)) and not (self.__player_turn==2 and self.__ai):
            self.remove_line(self.__previousLine)
            self.__selecting_line=False
            self.__previousLine=((0,0),(0,0))
            self.__selecting_ring=True
            self.__canva.unbind("<Motion>")
            self.__canva.unbind("<Button-3>")
            self.update()         
        elif not self.__selecting_line and not self.__selecting_ring and not (self.__player_turn==2 and self.__ai):
            self.place(selected_x,selected_y)
            if not self.__selecting_line and not self.__selecting_ring and (self.__player_turn==2 and self.__ai):
                self.__root.after(1000, self.bot_turn)
                
    def bot_turn(self):
        if not self.__rings_placed:
            temp_cos=(0,0)
            while not calc.possible_position(temp_cos[0],temp_cos[1],self.__forbidden_list) or calc.position_in_list(temp_cos[0],temp_cos[1],self.__ring_list[0]) or calc.position_in_list(temp_cos[0],temp_cos[1],self.__ring_list[1]) :
                temp_cos=(rd.randint(1,11),rd.randint(1,19))
            ring=Ring(self.__player_turn,self.__canva,self.__box_width,self.__box_heiht,temp_cos[0]*self.__box_width,temp_cos[1]*self.__box_heiht)
            self.__ring_list[self.__player_turn-1].append(ring)
            self.update()
            self.__rings_placed= len(self.__ring_list[0])==5 and len(self.__ring_list[1])==5
            self.__player_turn= 3-self.__player_turn
        elif self.__selecting_line:
            choice=self.__line_list[2+rd.choice(calc.get_all_index_line(self.__player_selecting,self.__line_list[2:]))][0]
            self.remove_line(choice)
            self.__selecting_line=False
            self.__selecting_ring=True
            self.update()
            self.__root.after(1000, self.bot_turn)
        elif self.__selecting_ring:
            self.__ring_list[1].remove(self.__ring_list[1][rd.randint(0,len(self.__ring_list[1])-1)])
            self.update()
            self.__selecting_ring=False
            for i in range (2):
                if len(self.__ring_list[i])==2:
                    print("J"+str(i+1)+" gagne")
                    self.__endGame=True
                    self.update()
            self.check_ligne()
        else:
            ring:Ring=rd.choice(self.__ring_list[1])
            self.possible_move(ring.get_box()[0],ring.get_box()[1])
            while self.__possible_list==[]:
                ring:Ring=rd.choice(self.__ring_list[1])
                self.possible_move(ring.get_box()[0],ring.get_box()[1])
            pawn = Pawn(2,self.__canva,self.__box_width,self.__box_heiht,ring.get_coords()[0],ring.get_coords()[1])
            self.__pawn_list[1].append(pawn)
            self.update()
            self.__root.after(500, self.bot_move, ring)
    
    def bot_move(self,ring:Ring):
        place=rd.choice(self.__possible_list)
        previous_coords=ring.get_box()
        ring.set_box(place[0],place[1])
        self.exchange(place,previous_coords)
        self.__possible_list=[]
        self.update()
                    
    def change_line(self,event):
        index=calc.get_line_index(self.__previousLine[0][0],self.__previousLine[0][1],self.__previousLine[1][0],self.__previousLine[1][1],self.__line_list[2:])
        if index==-1:
            print("Error index wrong")
            return
        next_index=calc.get_index_next_line(self.__previousHover[0],self.__previousHover[1],self.__line_list[2:],index,self.__player_selecting)
        self.__previousLine=self.__line_list[next_index+2][0]
        self.update()
        
        
            
    
    def selectRing(self,selected_x,selected_y) -> bool:
        index=calc.get_index(selected_x,selected_y,self.__ring_list[self.__player_selecting-1])
        if index!=-1:
            self.__ring_list[self.__player_selecting-1].pop(index)
            self.__selecting_ring=False
            self.update()
        return index!=-1 
    
           
    def place(self, selected_x, selected_y):
        
        selected_ring=False
        if (not (1<=selected_x<=11 and 1<=selected_y<=19))or (selected_x,selected_y) in self.__forbidden_list:
            return
        
        if not self.__rings_placed:
            if not (calc.position_in_list(selected_x,selected_y,self.__ring_list[0]) or calc.position_in_list(selected_x,selected_y,self.__ring_list[1])):
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
                    index = calc.get_index(previous_coords[0],previous_coords[1],self.__ring_list[self.__player_turn-1])
                    self.__ring_list[self.__player_turn-1][index].set_box(selected_x,selected_y)
                    self.__possible_list=[]
                    self.exchange((selected_x,selected_y),previous_coords)                    
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
                    if calc.position_in_list(temp_x,temp_y,self.__ring_list[0]) or calc.position_in_list(temp_x,temp_y, self.__ring_list[1]):
                        break
                    elif calc.position_in_list(temp_x,temp_y,self.__pawn_list[0]) or calc.position_in_list(temp_x,temp_y, self.__pawn_list[1]):
                        while (not empty_found) and temp_x+1*(-1)**i>=1 and temp_x+1*(-1)**i<=11 and temp_y+1*(-1)**j>=1 and temp_y+1*(-1)**j<=19 and (temp_x+1*(-1)**i,temp_y+1*(-1)**j) not in self.__forbidden_list:
                            temp_x=temp_x+1*(-1)**i
                            temp_y=temp_y+1*(-1)**j
                            if calc.position_in_list(temp_x,temp_y,self.__ring_list[0]) or calc.position_in_list(temp_x,temp_y, self.__ring_list[1]):
                                break
                            elif calc.position_in_list(temp_x,temp_y,self.__pawn_list[0]) or calc.position_in_list(temp_x,temp_y, self.__pawn_list[1]):
                                pass
                            else :
                                empty_found=True
                                self.__possible_list.append((temp_x,temp_y))
                                break
                        empty_found=False
                        break
                    self.__possible_list.append((temp_x,temp_y))
                    
        for i in range(2):
            temp_y=y
            while temp_y+2*(-1)**i>=1 and temp_y+2*(-1)**i<=19 and (x,temp_y+2*(-1)**i) not in self.__forbidden_list:
                temp_y=temp_y+2*(-1)**i
                if calc.position_in_list(x,temp_y,self.__ring_list[0]) or calc.position_in_list(x,temp_y, self.__ring_list[1]):
                    break
                elif calc.position_in_list(x,temp_y,self.__pawn_list[0]) or calc.position_in_list(x,temp_y, self.__pawn_list[1]):
                    while (not empty_found) and temp_y+2*(-1)**i>=1 and temp_y+2*(-1)**i<=19 and (x,temp_y+2*(-1)**i) not in self.__forbidden_list:
                        temp_y=temp_y+2*(-1)**i
                        if calc.position_in_list(x,temp_y,self.__ring_list[0]) or calc.position_in_list(x,temp_y, self.__ring_list[1]):
                            break
                        elif calc.position_in_list(x,temp_y,self.__pawn_list[0]) or calc.position_in_list(x,temp_y, self.__pawn_list[1]):
                            pass
                        else :
                            empty_found=True
                            self.__possible_list.append((x,temp_y))
                            break
                    empty_found=False
                    break
                self.__possible_list.append((x,temp_y))
                
                
    
    def exchange(self,new_coords : tuple[int,int],previous_coords : tuple[int,int]):
        x_change=-1 if new_coords[0]<previous_coords[0] else 1 if new_coords[0]>previous_coords[0] else 0
        y_change=-1 if new_coords[1]<previous_coords[1] else 1
        y_change= y_change*2 if new_coords[1]==previous_coords[1] else y_change
        previous_coords=previous_coords[0]+x_change,previous_coords[1]+y_change
        while previous_coords!=new_coords: 
            index1=calc.get_index(previous_coords[0],previous_coords[1],self.__pawn_list[0])
            index2=calc.get_index(previous_coords[0],previous_coords[1],self.__pawn_list[1])
            if index1!=-1:
                self.__pawn_list[0][index1].change_player()
                pawn=self.__pawn_list[0].pop(index1)
                self.__pawn_list[1].append(pawn)
            elif index2!=-1:
                self.__pawn_list[1][index2].change_player()
                pawn =self.__pawn_list[1].pop(index2)
                self.__pawn_list[0].append(pawn)
            previous_coords=previous_coords[0]+x_change,previous_coords[1]+y_change
        self.check_ligne()
        
            
            
    def check_ligne(self):
        self.__line_list=[0,[]]
        for arr in self.__pawn_list:
            for elem in arr:
                self.verif_line(elem , arr)
        if self.__line_list[0]!=0:
            self.line_blitz() if self.__blitz_mode else self.line_normal()
        else :
            self.__player_turn=3-self.__player_turn
            
    
    def verif_line(self,elem, arr):
        i=1
        temp=elem.get_box()
        coords=[temp[0],temp[1]]
        while i<5:
            coords[0],coords[1]=coords[0]+1,coords[1]+1
            if i==4 and calc.position_in_list(coords[0],coords[1],arr):
                self.__line_list.append([(elem.get_box(),(coords[0],coords[1])),elem.get_player()])
                self.__line_list[1].append(elem.get_player())
                self.__line_list[0]+=1
            elif not calc.position_in_list(coords[0],coords[1],arr):
                i=10
            i+=1
                
        i=1
        coords=[temp[0],temp[1]]
        while i<5:
            coords[0],coords[1]=coords[0]+1,coords[1]-1
            if i==4 and calc.position_in_list(coords[0],coords[1],arr):
                self.__line_list.append([(elem.get_box(),(coords[0],coords[1])),elem.get_player()])
                self.__line_list[1].append(elem.get_player())
                self.__line_list[0]+=1
            elif not calc.position_in_list(coords[0],coords[1],arr):
                i=10
            i+=1

        i=1
        coords=[temp[0],temp[1]]
        while i<5:
            coords[1]=coords[1]+2
            if i==4 and calc.position_in_list(coords[0],coords[1],arr):
                self.__line_list.append([(elem.get_box(),(coords[0],coords[1])),elem.get_player()])
                self.__line_list[1].append(elem.get_player())
                self.__line_list[0]+=1
            elif not calc.position_in_list(coords[0],coords[1],arr):
                i=10
            i+=1
            
    def line_blitz(self):
        if 1 in self.__line_list[1] and 2 in self.__line_list[1]:
            print("Egalité")
        elif 1 in self.__line_list[1]:
            print("J1 gagne")
        elif 2 in self.__line_list[1]:
            print("J2 gagne")
        else :
            return
        self.__endGame=True
    
    def line_normal(self):
        if self.__line_list[1].count(self.__player_turn)>0:
            self.__player_selecting=self.__player_turn
            self.__selecting_line=True
            if self.__player_selecting==2 and self.__ai==True:
                self.__root.after(1000,self.bot_turn)
            else:
                self.__canva.bind("<Motion>",self.move)
                self.__canva.bind("<Button-3>",self.change_line)
        elif self.__line_list[1].count(3-self.__player_turn)>0:
            self.__player_selecting=3-self.__player_turn
            self.__selecting_line=True
            if self.__player_selecting==2 and self.__ai==True:
                self.__root.after(1000,self.bot_turn)
            else:
                self.__canva.bind("<Motion>",self.move)
                self.__canva.bind("<Button-3>",self.change_line)
            
    
    
    def remove_line(self,line):
        diff_x=(line[1][0]-line[0][0])/4
        diff_y=(line[1][1]-line[0][1])/4
        for i in range(5):
            index=calc.get_index(line[0][0]+diff_x*i,line[0][1]+diff_y*i,self.__pawn_list[self.__player_selecting-1])
            if index==-1:
                print("Error index wrong")
                return
            self.__pawn_list[self.__player_selecting-1].pop(index)
        self.update()
        
    

            
        
            
            
            