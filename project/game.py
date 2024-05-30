from tkinter import *
from tkinter import messagebox
from rules import Rules
from endgame import *
from Elements import Ring,Pawn
import Calculation as calc
from PIL import Image, ImageTk
import random as rd


class Game:
    """
    Class that handles the game, its graphics and does everything linked to the game actions or the player's input
    """
    def __init__(self,canva_lobby:Canvas,root:Tk,blitz_mode:bool,ai:bool) -> None:
        self.__root:Tk = root
        self.__blitz_mode : bool = blitz_mode
        self.__ai : bool=ai
        
        self.__canva_window_width:int=self.__root.winfo_screenwidth()
        self.__canva_window_height:int=self.__root.winfo_screenheight()
        self.__canva_window:Canvas=Canvas(canva_lobby,width=self.__canva_window_width,height=self.__canva_window_height, highlightthickness=0, background="black")
        self.__canva_window.pack(fill=BOTH, expand=True, anchor=NW)
        
        self.__bg_image:Image = Image.open("img/bg/bglobby1.png")
        self.__bg_image=self.__bg_image.resize((1920,1080)) #2020 350/2020
        self.__bg_image:PhotoImage = ImageTk.PhotoImage(self.__bg_image) 

        self.__bg_image2:Image = Image.open("img/bg/bglobby2.png")
        self.__bg_image2=self.__bg_image2.resize((1920,1080)) #2020 350/2020
        self.__bg_image2:PhotoImage = ImageTk.PhotoImage(self.__bg_image2)

        self.__bg_image3:Image = Image.open("img/bg/bglobby3.png")
        self.__bg_image3=self.__bg_image3.resize((1920,1080)) #2020 350/2020
        self.__bg_image3:PhotoImage = ImageTk.PhotoImage(self.__bg_image3)

        self.__bg_count:int = 1

        self.__canva_window.create_image(0,0,anchor=NW,image=self.__bg_image, tags="bgimage")
        
        self.__canva_width:float=self.__root.winfo_screenwidth()/2.3
        self.__canva_height:float=self.__root.winfo_screenheight()/1.4
        self.__canva:Canvas=Canvas(self.__canva_window, width=self.__canva_width, height=self.__canva_height,highlightthickness=0, background="white")
        self.__canva.pack()
        
        self.__canva.bind("<Button-1>",self.click)
        
        
        self.__box_height:float=self.__canva_height/20
        self.__box_width:float=self.__canva_width/12
        
        
        self.__rings_placed:bool=False
        self.__pawn_placed:bool=False
        self.__player_turn:int=1
        self.__turn_counter:int=0
        self.__pawn_list:list[list[Pawn]]=[[],[]]
        self.__ring_list:list[list[Ring]]=[[],[]]
        self.__forbidden_list:list[tuple[int,int]]=[(3,19),(1,19),(2,18),(1,17),(1,15),(1,5),(1,3),(1,1),(2,2),(3,1),(9,1),(10,2),(11,1),(11,3),(11,5),(11,15),(11,19),(11,17),(10,18),(9,19)]
        self.__possible_list:list[tuple[int,int]]=[]
        self.__line_list:list=[0,[]]
        self.__selecting_ring:bool=False
        self.__selecting_line:bool=False
        self.__player_selecting:int=0
        self.__end_game:bool=False
        self.__previous_hover:tuple[int,int]=(0,0)
        self.__previous_line:tuple[tuple[int,int],tuple[int,int]]=((0,0),(0,0))


        
        self.update()

        font:tuple = ("Helvetica", int(self.__canva_window_width / (2020 / 30)), "bold")

        self.__turn_label:Label = Label(self.__canva_window, font=font, bg="#E3D7FF")
        self.__turn_player_label:Label = Label(self.__canva_window, font=font, bg="#E3D7FF")

        self.__turn_label.pack(pady=5)
        self.__turn_player_label.pack()


        self.__turn_label.configure(text="Turn : " + str(self.__player_turn))
        
        player_color:str = "Blue" if self.__player_turn % 2 == 0 else "Red"
        self.__turn_player_label.configure(text="Player : " + player_color)    

        self.__leave_image_path:str = "img/buttons/leave.png"

        self.__leave_image:Image = Image.open(self.__leave_image_path)
        self.__leave_image = self.__leave_image.resize((int(self.__canva_window_width / (2020 / 340)), int(self.__canva_window_height / (2020 / 225))))
        self.__leave_image1:PhotoImage = ImageTk.PhotoImage(self.__leave_image)

        self.__canva_window.create_image(self.__canva_window_width/(2020/1740),self.__canva_window_height/ (1080/260), image=self.__leave_image1, tags="leave_image")

        self.__canva_window.tag_bind("leave_image", "<Button-1>", self.leave_button_clicked)
        self.__canva_window.tag_bind("leave_image", "<Enter>", self.leave_button_hover)
        self.__canva_window.tag_bind("leave_image", "<Leave>", self.leave_button_hoverl)



        self.__restart_image_path:str = "img/buttons/restart.png"

        self.__restart_image:Image = Image.open(self.__restart_image_path)
        self.__restart_image = self.__restart_image.resize((int(self.__canva_window_width / (2020 / 400)), int(self.__canva_window_height / (2020 / 225))))
        self.__restart_image1:PhotoImage = ImageTk.PhotoImage(self.__restart_image)

        self.__canva_window.create_image(self.__canva_window_width/(2020/1740),self.__canva_window_height/(1080/470), image=self.__restart_image1, tags="restart_image")

        self.__canva_window.tag_bind("restart_image", "<Button-1>", self.restart_button_clicked)
        self.__canva_window.tag_bind("restart_image", "<Enter>", self.restart_button_hover)
        self.__canva_window.tag_bind("restart_image", "<Leave>", self.restart_button_hoverl)



        self.__rules_image_path:str = "img/buttons/rules.png"

        self.__rules_image:Image = Image.open(self.__rules_image_path)
        self.__rules_image = self.__rules_image.resize((int(self.__canva_window_width / (2020 / 400)), int(self.__canva_window_height / (2020 / 225))))
        self.__rules_image1:PhotoImage = ImageTk.PhotoImage(self.__rules_image)

        self.__canva_window.create_image(self.__canva_window_width/(2020/1740),self.__canva_window_height/(1080/680), image=self.__rules_image1, tags="rules_image")

        self.__canva_window.tag_bind("rules_image", "<Button-1>", self.rules_button_clicked)
        self.__canva_window.tag_bind("rules_image", "<Enter>", self.rules_button_hover)
        self.__canva_window.tag_bind("rules_image", "<Leave>", self.rules_button_hoverl)



        self.__right_arrow_path:str = "img/buttons/right_arrow.png"

        self.__right_arrow:Image = Image.open(self.__right_arrow_path)
        self.__right_arrow = self.__right_arrow.resize((int(self.__canva_window_width / (2020 / 90)), int(self.__canva_window_height / (2020 / 160))))
        self.__right_arrow1:PhotoImage = ImageTk.PhotoImage(self.__right_arrow)

        self.__canva_window.create_image(self.__canva_window_width/(2020/1950),self.__canva_window_height-60, image=self.__right_arrow1, tags="right_arrow_image")

        self.__canva_window.tag_bind("right_arrow_image", "<Button-1>", self.right_button_clicked)
        self.__canva_window.tag_bind("right_arrow_image", "<Enter>", self.right_button_hover)
        self.__canva_window.tag_bind("right_arrow_image", "<Leave>", self.right_button_hoverl)



        self.__left_arrow_path:str = "img/buttons/left_arrow.png"

        self.__left_arrow:Image = Image.open(self.__left_arrow_path)
        self.__left_arrow = self.__left_arrow.resize((int(self.__canva_window_width / (2020 / 90)), int(self.__canva_window_height / (2020 / 160))))
        self.__left_arrow1:PhotoImage = ImageTk.PhotoImage(self.__left_arrow)

        self.__canva_window.create_image(self.__canva_window_width/(2020/1850),self.__canva_window_height-60, image=self.__left_arrow1, tags="left_arrow_image")

        self.__canva_window.tag_bind("left_arrow_image", "<Button-1>", self.left_button_clicked)
        self.__canva_window.tag_bind("left_arrow_image", "<Enter>", self.left_button_hover)
        self.__canva_window.tag_bind("left_arrow_image", "<Leave>", self.left_button_hoverl)



        self.__grey_circle_path:str = "img/circles/gray_circle.png"

        self.__grey_circle:Image = Image.open(self.__grey_circle_path)
        self.__grey_circle = self.__grey_circle.resize((int(self.__canva_window_width / (2020 / 140)), int(self.__canva_window_height / (2020 / 235))))
        self.__grey_circle1:PhotoImage = ImageTk.PhotoImage(self.__grey_circle)
        self.__grey_circle2:PhotoImage = ImageTk.PhotoImage(self.__grey_circle)
        self.__grey_circle3:PhotoImage = ImageTk.PhotoImage(self.__grey_circle)
        self.__grey_circle4:PhotoImage = ImageTk.PhotoImage(self.__grey_circle)
        self.__grey_circle5:PhotoImage = ImageTk.PhotoImage(self.__grey_circle)
        self.__grey_circle6:PhotoImage = ImageTk.PhotoImage(self.__grey_circle)

        self.__canva_window.create_image(self.__canva_window_width/(2020/1640),self.__canva_window_height-95, image=self.__grey_circle1, tags="greycircle_image1")
        self.__canva_window.create_image(self.__canva_window_width/(2020/1480),self.__canva_window_height-95, image=self.__grey_circle2, tags="greycircle_image2")
        self.__canva_window.create_image(self.__canva_window_width/(2020/1320),self.__canva_window_height-95, image=self.__grey_circle3, tags="greycircle_image3")

        self.__canva_window.create_image(self.__canva_window_width/(2020/690),self.__canva_window_height-95, image=self.__grey_circle4, tags="greycircle_image4")
        self.__canva_window.create_image(self.__canva_window_width/(2020/530),self.__canva_window_height-95, image=self.__grey_circle5, tags="greycircle_image5")
        self.__canva_window.create_image(self.__canva_window_width/(2020/370),self.__canva_window_height-95, image=self.__grey_circle6, tags="greycircle_image6")
        
    """
    def update_turn(self) -> None:
        
        Update the player turn and display it on the screen
        
        self.__turn_counter += 1
        self.__turn_label.configure(text="Turn : " + str(self.__player_turn))

        player_color = "Blue" if self.__player_turn % 2 == 0 else "Red"
        self.__turn_player_label.configure(text="Player : " + player_color)  
    """
    
    def display_msg(self,msg:str,player:int) -> None:
        """
        Method that will display a message on the screen

        Args:
            msg (str): message to display
            player (int): player who won
        """
        self.__msg_label.configure(text="Player " + str(player) + " won !")
    
    def update(self) -> None:
        """
        Updates the game by calling the drawing_update function and unbinding the click event if the game is over
        """   
        self.drawing_update()
        if self.__end_game:
            self.__canva.unbind("<Button-1>")
        
    
    def move(self,event:Event) -> None:
        """
        Method that will be called when the player is moving the mouse and will call a method that will select the line hovered by the player

        Args:
            event (Event): contains all the informations of the hovering of the mouse
        """
        hover:tuple[int,int]=calc.find_closer(event.x/self.__box_width, event.y/self.__box_height)
        if self.__selecting_line and hover!=self.__previous_hover:
            self.__previous_hover=hover
            self.find_line(hover)
            self.update()
    
    def find_line(self,hover:tuple[int,int]) -> None:
        """
        Method that will find the line hovered by the player

        Args:
            hover (tuple[int,int]): coordinates of the closest point around the player's mouse
        """
        for elem in self.__line_list[2:]:
            if hover==calc.get_middle(elem[0][0][0],elem[0][0][1],elem[0][1][0],elem[0][1][1]) and elem[1]==self.__player_selecting:
                self.__previous_line=elem[0]
                return
        for elem in self.__line_list[2:]:
            if hover in calc.get_around_middle(elem[0][0][0],elem[0][0][1],elem[0][1][0],elem[0][1][1]) and elem[1]==self.__player_selecting:
                self.__previous_line=elem[0]
                return
        for elem in self.__line_list[2:] :
            if (float(hover[0]),float(hover[1])) in elem[0] and elem[1]==self.__player_selecting :
                self.__previous_line=elem[0]
                return
        self.__previous_line=((0,0),(0,0))
    
    def drawing_update(self) -> None:
        """
        Method that will use a bunch of methods of tkinter in order to draw the game (the rings, the pawns and the board)
        """
        self.__canva.delete('all')
        for i in range(2):
            for j in range(2):
                self.__canva.create_line(self.__canva_width*i+(-1)**i*2*self.__box_width,self.__canva_height*j+(-1)**j*4*self.__box_height,self.__canva_width*i+(-1)**i*5*self.__box_width,self.__canva_height*j+(-1)**j*1*self.__box_height,fill="black",width=6)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,self.__canva_height*j+(-1)**j*7*self.__box_height,self.__canva_width*i+(-1)**i*7*self.__box_width,self.__canva_height*j+(-1)**j*1*self.__box_height,fill="black",width=6)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,self.__canva_height*j+(-1)**j*9*self.__box_height,self.__canva_width*i+(-1)**i*8*self.__box_width,self.__canva_height*j+(-1)**j*2*self.__box_height,fill="black",width=6)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,self.__canva_height*j+(-1)**j*11*self.__box_height,self.__canva_width*i+(-1)**i*9*self.__box_width,self.__canva_height*j+(-1)**j*3*self.__box_height,fill="black",width=6)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,self.__canva_height*j+(-1)**j*13*self.__box_height,self.__canva_width*i+(-1)**i*10*self.__box_width,self.__canva_height*j+(-1)**j*4*self.__box_height,fill="black",width=6)
                self.__canva.create_line(self.__canva_width*i+(-1)**i*2*self.__box_width,self.__canva_height*j+(-1)**j*14*self.__box_height,self.__canva_width*i+(-1)**i*10*self.__box_width,self.__canva_height*j+(-1)**j*6*self.__box_height,fill="black",width=6)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*1*self.__box_width,13*self.__box_height,self.__canva_width*i+(-1)**i*1*self.__box_width,7*self.__box_height,fill="black",width=6)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*2*self.__box_width,16*self.__box_height,self.__canva_width*i+(-1)**i*2*self.__box_width,4*self.__box_height,fill="black",width=6)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*3*self.__box_width,17*self.__box_height,self.__canva_width*i+(-1)**i*3*self.__box_width,3*self.__box_height,fill="black",width=6)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*4*self.__box_width,18*self.__box_height,self.__canva_width*i+(-1)**i*4*self.__box_width,2*self.__box_height,fill="black",width=6)
            self.__canva.create_line(self.__canva_width*i+(-1)**i*5*self.__box_width,19*self.__box_height,self.__canva_width*i+(-1)**i*5*self.__box_width,1*self.__box_height,fill="black",width=6)
        self.__canva.create_line(self.__canva_width*i+(-1)**i*6*self.__box_width,18*self.__box_height,self.__canva_width*i+(-1)**i*6*self.__box_width,2*self.__box_height,fill="black",width=6)
        for list in self.__pawn_list:
            for elem in list:
                elem.draw()
        for list in self.__ring_list:
            for elem in list:
                elem.draw()
        for elem in self.__possible_list:
            Pawn(0,self.__canva,self.__box_width,self.__box_height,elem[0]*self.__box_width,elem[1]*self.__box_height).draw()
        if self.__previous_line!=((0,0),(0,0)) and self.__selecting_line:
            self.__canva.create_line(self.__previous_line[0][0]*self.__box_width,self.__previous_line[0][1]*self.__box_height,self.__previous_line[1][0]*self.__box_width,self.__previous_line[1][1]*self.__box_height,fill="green",width=4)
        
    def click(self,event:Event) -> None:
        """
        Method that will be called when the player clicks on the board and will call different method depending on the situation of the game

        Args:
            event (Event): contains all the informations of the clicking of the mouse
        """
        selected_x:int
        selected_y:int
        selected_x, selected_y= calc.find_closer(event.x/self.__box_width, event.y/self.__box_height)
        if self.__selecting_ring:
            if self.select_ring(selected_x,selected_y):
                for i in range (2):
                    if len(self.__ring_list[i])==2:
                        self.__canva.pack_forget()
                        self.__turn_label.pack_forget()
                        self.__turn_player_label.pack_forget()
                        EndGameRed(self.__canva_window,self.__root) if i==0 else EndGameBlue(self.__canva_window,self.__root)
                        self.__end_game=True
                        self.update()
                        return
                self.check_line(True)
        elif self.__selecting_line and self.__previous_line!=((0,0),(0,0)) and not (self.__player_turn==2 and self.__ai):
            self.remove_line(self.__previous_line)
            self.__selecting_line=False
            self.__previous_line=((0,0),(0,0))
            self.__selecting_ring=True
            self.__canva.unbind("<Motion>")
            self.__canva.unbind("<Button-3>")
            self.update()         
        elif not self.__selecting_line and not self.__selecting_ring and not (self.__player_turn==2 and self.__ai):
            self.place(selected_x,selected_y)
            if not self.__selecting_line and not self.__selecting_ring and (self.__player_turn==2 and self.__ai):
                self.__root.after(1000, self.bot_turn)
                
                
    def bot_turn(self) -> None:
        """
        Method that will be called in order to make the bot's turn
        """
        if not self.__rings_placed:
            temp_cos:tuple[int,int]=(0,0)
            while not calc.possible_position(temp_cos[0],temp_cos[1],self.__forbidden_list) or calc.position_in_list(temp_cos[0],temp_cos[1],self.__ring_list[0]) or calc.position_in_list(temp_cos[0],temp_cos[1],self.__ring_list[1]) :
                temp_cos=(rd.randint(1,11),rd.randint(1,19))
            ring:Ring=Ring(self.__player_turn,self.__canva,self.__box_width,self.__box_height,temp_cos[0]*self.__box_width,temp_cos[1]*self.__box_height)
            self.__ring_list[self.__player_turn-1].append(ring)
            self.update()
            self.__rings_placed= len(self.__ring_list[0])==5 and len(self.__ring_list[1])==5
            self.__player_turn= 3-self.__player_turn
        elif self.__selecting_line:
            choice:tuple[tuple[int,int],tuple[int,int]]=self.__line_list[2+rd.choice(calc.get_all_index_line(self.__player_selecting,self.__line_list[2:]))][0]
            self.remove_line(choice)
            self.__selecting_line=False
            self.__selecting_ring=True
            self.update()
            self.__root.after(500, self.bot_turn)
        elif self.__selecting_ring:
            self.__ring_list[1].remove(self.__ring_list[1][rd.randint(0,len(self.__ring_list[1])-1)])
            self.update()
            self.__selecting_ring=False
            for i in range (2):
                if len(self.__ring_list[i])==2:
                    self.__canva.pack_forget()
                    self.__turn_label.pack_forget()
                    self.__turn_player_label.pack_forget()
                    EndGameRed(self.__canva_window,self.__root) if i==0 else EndGameBlue(self.__canva_window,self.__root)
                    self.__end_game=True
                    self.update()
                    return
            self.check_line(True)
        else:
            ring:Ring=rd.choice(self.__ring_list[1])
            self.possible_move(ring.get_box()[0],ring.get_box()[1])
            while self.__possible_list==[]:
                ring=rd.choice(self.__ring_list[1])
                self.possible_move(ring.get_box()[0],ring.get_box()[1])
            
            pawn:Pawn = Pawn(2,self.__canva,self.__box_width,self.__box_height,ring.get_coords()[0],ring.get_coords()[1])
            self.__pawn_list[1].append(pawn)
            place:tuple[int,int]=rd.choice(self.__possible_list)
            previous_coords:tuple[int,int]=ring.get_box()
            ring.set_box(place[0],place[1])
            self.exchange(place,previous_coords)
            self.__possible_list=[]
            self.update()
                    
    def change_line(self,event:Event) -> None:
        """
        Method that will be called when the player is right-clicking and will change the line hovered by a green line if there is another line on the same box where the mouse is

        Args:
            event (Event): contains all the informations of the right-clicking of the mouse
        """
        index:int=calc.get_line_index(self.__previous_line[0][0],self.__previous_line[0][1],self.__previous_line[1][0],self.__previous_line[1][1],self.__line_list[2:])
        if index==-1:
            print("Error index wrong")
            return
        next_index:int=calc.get_index_next_line(self.__previous_hover[0],self.__previous_hover[1],self.__line_list[2:],index,self.__player_selecting)
        self.__previous_line=self.__line_list[next_index+2][0]
        self.update()
        
        
            
    
    def select_ring(self,selected_x:int,selected_y:int) -> bool:
        """
        Function that will remove the ring selected by a player if there is a ring where the player clicks

        Args:
            selected_x (int): first coordinate selected by a player
            selected_y (int): second coordinate selected by a player

        Returns:
            bool: return true if a ring is selected else return false
        """
        index:int=calc.get_index(selected_x,selected_y,self.__ring_list[self.__player_selecting-1])
        if index!=-1:
            self.__ring_list[self.__player_selecting-1].pop(index)
            self.__selecting_ring=False
            self.update()
        return index!=-1 
    
           
    def place(self, selected_x:int, selected_y:int) -> None:
        """
        Method that will place a ring on the board or a pawn on the board or move a ring depending of what the player is supposed to do

        Args:
            selected_x (int): first coordinate selected by a player
            selected_y (int): second coordinate selected by a player
        """
        selected_ring:bool=False
        if (not (1<=selected_x<=11 and 1<=selected_y<=19))or (selected_x,selected_y) in self.__forbidden_list:
            return
        
        if not self.__rings_placed:
            if not (calc.position_in_list(selected_x,selected_y,self.__ring_list[0]) or calc.position_in_list(selected_x,selected_y,self.__ring_list[1])):
                ring:Ring=Ring(self.__player_turn,self.__canva,self.__box_width,self.__box_height,selected_x*self.__box_width,selected_y*self.__box_height)
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
                    pawn:Pawn = Pawn(self.__player_turn,self.__canva,self.__box_width,self.__box_height,selected_x*self.__box_width,selected_y*self.__box_height)
                    self.__pawn_list[self.__player_turn-1].append(pawn)
                    self.possible_move(selected_x,selected_y)
                    self.update()

                else:
                    pawn:Pawn = Pawn(self.__player_turn,self.__canva,self.__box_width,self.__box_height,selected_x*self.__box_width,selected_y*self.__box_height)
                    self.__pawn_list[self.__player_turn-1].append(pawn)
                    self.possible_move(selected_x,selected_y)
                    self.update()
                    self.__pawn_placed=True
            elif self.__pawn_placed :
                if (selected_x,selected_y) in self.__possible_list:
                    self.__pawn_placed=False
                    previous_coords=self.__pawn_list[self.__player_turn-1][-1].get_box()
                    index:int = calc.get_index(previous_coords[0],previous_coords[1],self.__ring_list[self.__player_turn-1])
                    self.__ring_list[self.__player_turn-1][index].set_box(selected_x,selected_y)
                    self.__possible_list=[]
                    self.exchange((selected_x,selected_y),previous_coords)                    
                else :
                    del(self.__pawn_list[self.__player_turn-1][-1])
                    self.__pawn_placed=False
                    self.__possible_list=[]
                self.update()
                
    
    def possible_move(self,x : int,y : int) -> None:
        """
        Method that will update the possible move list by filling it with the possible move of the player depending of the position of the ring

        Args:
            x (int): first coordinate of the ring
            y (int): second coordinate of the ring
        """
        empty_found:bool=False
        self.__possible_list=[]
        temp_x:int
        temp_y:int
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
                
                
    
    def exchange(self,new_coords : tuple[int,int],previous_coords : tuple[int,int]) -> None:
        """
        Method that will change the player and the color of pawn between the two coordinates

        Args:
            new_coords (tuple[int,int]): first coordinates
            previous_coords (tuple[int,int]): second coordinates
        """
        x_change:int=-1 if new_coords[0]<previous_coords[0] else 1 if new_coords[0]>previous_coords[0] else 0
        y_change:int=-1 if new_coords[1]<previous_coords[1] else 1
        y_change= y_change*2 if new_coords[1]==previous_coords[1] else y_change
        previous_coords=previous_coords[0]+x_change,previous_coords[1]+y_change
        while previous_coords!=new_coords: 
            index1:int=calc.get_index(previous_coords[0],previous_coords[1],self.__pawn_list[0])
            index2:int=calc.get_index(previous_coords[0],previous_coords[1],self.__pawn_list[1])
            if index1!=-1:
                self.__pawn_list[0][index1].change_player()
                pawn:Pawn=self.__pawn_list[0].pop(index1)
                self.__pawn_list[1].append(pawn)
            elif index2!=-1:
                self.__pawn_list[1][index2].change_player()
                pawn:Pawn =self.__pawn_list[1].pop(index2)
                self.__pawn_list[0].append(pawn)
            previous_coords=previous_coords[0]+x_change,previous_coords[1]+y_change
        self.check_line()
        
            
            
    def check_line(self,line_before:bool=False) -> None:
        """
        Method that will call another to check if a line is made and if it is, will call another method that will react depending of the gamemode

        Args:
            line_before (bool, optional): True if a line has been selected just before. Defaults to False.
        """
        self.__line_list=[0,[]]
        for arr in self.__pawn_list:
            for elem in arr:
                self.verif_line(elem , arr)
        if self.__line_list[0]!=0:
            self.line_blitz() if self.__blitz_mode else self.line_normal()
        else :
            self.__player_turn=3-self.__player_turn
            if line_before and self.__player_turn==2 and self.__ai:
                self.__root.after(1000,self.bot_turn())
            
    
    def verif_line(self,elem: Pawn, arr: list[Pawn]) -> None:
        """
        Method that will verify if there is a line below a pawn or on the two diagonals on its right

        Args:
            elem (Pawn): The pawn from which we will verify if there is a line below it or on the two diagonals on its right
            arr (list[Pawn]): list of all the pawns of the player that owns the first pawn
        """
        i:int=1
        temp:tuple[int,int]=elem.get_box()
        coords:list=[temp[0],temp[1]]
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
            
    def line_blitz(self) -> None:
        """
        Method that will be called if a line if made in blitz mode
        As soon as a line is made, the method will announce the winner
        """
        if 1 in self.__line_list[1] and 2 in self.__line_list[1]:
            EndGameDraw(self.__canva_window,self.__root)
        elif 1 in self.__line_list[1]:
            print('test')
            EndGameRed(self.__canva_window,self.__root) 
        elif 2 in self.__line_list[1]:
            EndGameBlue(self.__canva_window,self.__root)
        else :
            return
        self.__canva.pack_forget()
        self.__turn_label.pack_forget()
        self.__turn_player_label.pack_forget()
        self.__end_game=True
        self.update()
    
    def line_normal(self) -> None:
        """
        Method that will be called if a line if made in normal mode
        This method will check who made a line and will let him remove his line and one of his pawns
        """
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
            
    
    
    def remove_line(self,line:tuple[tuple[int,int],tuple[int,int]]) -> None:
        """
        Method that removes all the pawns of a line from the board

        Args:
            line (tuple[tuple[int,int],tuple[int,int]]): the line that will be removed
        """
        diff_x:int=(line[1][0]-line[0][0])/4
        diff_y:int=(line[1][1]-line[0][1])/4
        for i in range(5):
            index:int=calc.get_index(line[0][0]+diff_x*i,line[0][1]+diff_y*i,self.__pawn_list[self.__player_selecting-1])
            if index==-1:
                print("Error index wrong")
                return
            self.__pawn_list[self.__player_selecting-1].pop(index)
        self.update()

    def change_bg(self,nb:int) -> None:
        """
        Method that will change the background

        Args:
            nb (int): the number of the background
        """
        if nb == 1:
            self.__canva_window.itemconfig("bgimage", image=self.__bg_image)
        elif nb == 2:
            self.__canva_window.itemconfig("bgimage", image=self.__bg_image2)
        elif nb == 3:
            self.__canva_window.itemconfig("bgimage", image=self.__bg_image3)


    def leave_button_clicked(self, event: Event) -> None:
        """
        Method called when the leave button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self.__canva_window.destroy()

    def restart_button_clicked(self, event: Event) -> None:
        """
        Method called when the leave button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self.__pawn_list = [[], []]
        self.__ring_list = [[], []]
        self.__line_list = [0, []]
        self.__possible_list = []
        self.__turn_counter = 0
        self.__player_turn = 1
        
        self.__rings_placed=False
        self.__pawn_placed=False
        
        self.__selecting_ring=False
        self.__selecting_line=False
        self.__end_game=False
        self.__previous_hover=(0,0)
        self.__previous_line=((0,0),(0,0))

        self.update()

    def rules_button_clicked(self, event: Event) -> None:
        """
        Method called when the Rules button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self.__canva.pack_forget()
        self.__turn_label.pack_forget()
        self.__turn_player_label.pack_forget()
        Rules(canva=self.__canva_window,root=self.__root,box=self.__canva, turn=self.__turn_label, turn_player=self.__turn_player_label,mode=1+int(self.__blitz_mode))

    def right_button_clicked(self, event: Event) -> None:
        """
        Method called when the right arrow button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self.__bg_count += 1
        if self.__bg_count > 3:
            self.__bg_count = 1
        self.change_bg(self.__bg_count)

    def left_button_clicked(self, event: Event) -> None:
        """
        Method called when the left arrow button is clicked

        Args:
            event (Event): contains all the informations of the button clicking
        """
        self.__bg_count -= 1
        if self.__bg_count < 1:
            self.__bg_count = 3
        self.change_bg(self.__bg_count)


    def leave_button_hover(self, event: Event) -> None:
        """
        Method called when you leave the leave button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__leave_hover_image_path = "img/buttons/leavehover.png"

        self.__leave_hover_image = Image.open(self.__leave_hover_image_path)
        self.__leave_hover_image = self.__leave_hover_image.resize((int(self.__canva_window_width / (2020 / 340)), int(self.__canva_window_height / (2020 / 225))))
        self.__leave_hover_image1 = ImageTk.PhotoImage(self.__leave_hover_image)
        self.__canva_window.itemconfig("leave_image", image=self.__leave_hover_image1)

    def restart_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the restart button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__restarthoverimage_path = "img/buttons/restarthover.png"

        self.__restarthoverimage = Image.open(self.__restarthoverimage_path)
        self.__restarthoverimage = self.__restarthoverimage.resize((int(self.__canva_window_width / (2020 / 400)), int(self.__canva_window_height / (2020 / 225))))
        self.__restarthoverimage1 = ImageTk.PhotoImage(self.__restarthoverimage)
        self.__canva_window.itemconfig("restart_image", image=self.__restarthoverimage1)

    def rules_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the rules button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__ruleshoverimage_path = "img/buttons/ruleshover.png"

        self.__ruleshoverimage = Image.open(self.__ruleshoverimage_path)
        self.__ruleshoverimage = self.__ruleshoverimage.resize((int(self.__canva_window_width / (2020 / 400)), int(self.__canva_window_height / (2020 / 225))))
        self.__ruleshoverimage1 = ImageTk.PhotoImage(self.__ruleshoverimage)
        self.__canva_window.itemconfig("rules_image", image=self.__ruleshoverimage1)

    def right_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the right-arrow button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__right_arrowhoverimage_path = "img/buttons/right_arrowhover.png"

        self.__right_arrowhoverimage = Image.open(self.__right_arrowhoverimage_path)
        self.__right_arrowhoverimage = self.__right_arrowhoverimage.resize((int(self.__canva_window_width / (2020 / 90)), int(self.__canva_window_height / (2020 / 160))))
        self.__right_arrowhoverimage1 = ImageTk.PhotoImage(self.__right_arrowhoverimage)
        self.__canva_window.itemconfig("right_arrow_image", image=self.__right_arrowhoverimage1)

    def left_button_hover(self, event: Event) -> None:
        """
        Method called when you hover the left-arrow button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__left_arrowhoverimage_path = "img/buttons/left_arrowhover.png"

        self.__left_arrowhoverimage = Image.open(self.__left_arrowhoverimage_path)
        self.__left_arrowhoverimage = self.__left_arrowhoverimage.resize((int(self.__canva_window_width / (2020 / 90)), int(self.__canva_window_height / (2020 / 160))))
        self.__left_arrowhoverimage1 = ImageTk.PhotoImage(self.__left_arrowhoverimage)
        self.__canva_window.itemconfig("left_arrow_image", image=self.__left_arrowhoverimage1)



    def leave_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the leave button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__canva_window.itemconfig("leave_image", image=self.__leave_image1)    

    def restart_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the restart button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__canva_window.itemconfig("restart_image", image=self.__restart_image1)    

    def rules_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the rules button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__canva_window.itemconfig("rules_image", image=self.__rules_image1)

    def right_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the right-arrow button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__canva_window.itemconfig("right_arrow_image", image=self.__right_arrow1)

    def left_button_hoverl(self, event: Event) -> None:
        """
        Method called when you leave the left-arrow button

        Args:
            event (Event): contains all the informations of the event
        """
        self.__canva_window.itemconfig("left_arrow_image", image=self.__left_arrow1)