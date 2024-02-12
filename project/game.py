from tkinter import *
from tkinter import messagebox
from Elements import Ring,Pawn
from PIL import Image, ImageTk

class Game:
    def __init__(self,canva_lobby,root) -> None:
        self.__root = root
        self.__canva_lobby=canva_lobby
        
        self.__canva_width=self.__root.winfo_screenwidth()/2.3
        self.__canva_height=self.__root.winfo_screenheight()/1.5
        self.__box_heiht=self.__canva_height/20
        self.__box_width=self.__canva_width/12
        self.__canva=Canvas(self.__root, width=self.__canva_width, height=self.__canva_height,highlightthickness=0)
        self.__canva.pack()
        ring=Ring(2,self.__canva,self.__box_width,self.__box_heiht,0,0)
        ring.set_box(8,6)
        self.__ring_list=[ring]
        pawn=Pawn(1,self.__canva,self.__box_width,self.__box_heiht,0,0)
        pawn.set_box(3,5)
        self.__pawn_list=[pawn]
        
        self.update()
        self.__root.mainloop()
        
        self.__croiximage = Image.open("img/buttons/croix.png")
        self.__croiximage = self.__croiximage.resize((int(self.__canva_width / (2020 / 90)), int(self.__canva_height / (2020 / 150))))
        self.__croiximage = ImageTk.PhotoImage(self.__croiximage)

        self.__canva.tag_bind("croix_image", "<Button-1>", self.close)


        self.__canva.create_image(self.__canva_width /1.08, self.__canva_height * 0.13, image=self.__croiximage, tags="croix_image")
        
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
            
    def close(self, event):
        self.__canva.delete("croix_image","frame","text")
        self.__canva.pack_forget()

        self.__canva_lobby.create_image(self.__w/(2020/400),self.__h-175,image=self.__start, tags="start_image")
        self.__canva_lobby.create_image(self.__w/(2020/1000),self.__h-175,image=self.__rules, tags="rules_image")
        self.__canva_lobby.create_image(self.__w/(2020/1600),self.__h-175,image=self.__leave, tags="leave_image")