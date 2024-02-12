from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Rules:
    
    def __init__(self,canva,root,start,rules,leave):

        self.__start = start
        self.__rules = rules
        self.__leave = leave

        self.__w = root.winfo_screenwidth()
        self.__h = root.winfo_screenheight()


        self.__croiximage = Image.open("img/buttons/croix.png")
        self.__croiximage = self.__croiximage.resize((int(self.__w / (2020 / 90)), int(self.__h / (2020 / 150))))
        self.__croiximage = ImageTk.PhotoImage(self.__croiximage)

        self.__bg_canvas = canva
        self.__bg_canvas.create_image(self.__w /1.08, self.__h * 0.13, image=self.__croiximage, tags="croix_image")

        self.__bg_canvas.tag_bind("croix_image", "<Button-1>", self.quit_button_clicked)
        self.__bg_canvas.tag_bind("croix_image", "<Enter>", self.quit_button_enter)
        self.__bg_canvas.tag_bind("croix_image", "<Leave>", self.quit_button_leave)



        frame_width = self.__w - 100
        frame_height = self.__h - 100

        x1 = 50
        y1 = 50

        x2 = x1 + frame_width
        y2 = y1 + frame_height

        self.__bg_canvas.create_rectangle(x1, y1, x2, y2, fill="#E3D7FF", stipple="gray50" ,outline="#E3D7FF", width=10, tags="frame")
        self.__bg_canvas.create_image(self.__w /1.08, self.__h * 0.13, image=self.__croiximage, tags="croix_image")


        rules_text = """Pour commencer la partie :
Placer le plateau au centre de la table. Chaque joueur choisir sa couleur: noir ou blanc.

Le tour de jeu :
Phase 1 : placement des anneaux sur le plateau

Tour à tour, en commençant par le joueur blanc, chaque joueur place un anneau à sa couleur sur une intersection libre du plateau.

Phase 2 : déplacement des anneaux

Blanc commence. Tour à tour, chaque joueur doit déplacer un de ses anneaux en respectant les règles suivantes :

- Choisir l'anneau à déplacer
- Le joueur choisit un de ses anneaux sur le plateau.
- Placer un pion à sa couleur au centre de l'anneau
- Le joueur prend un pion dans la réserve et le place au centre de l'anneau.
- La face visible du pion doit être à la couleur du joueur.
- Déplacer l'anneau
- Le joueur doit déplacer l'anneau, en ligne droite dans une des six directions, et arrêter le parcours sur une intersection libre.
- Au cours de son déplacement, l'anneau peut survoler des intersections libres ou occupées par des pions. Par contre, l'anneau ne peut pas survoler d'autres anneaux.
- Tant que l'anneau survole des intersections libres, le joueur peut déplacer l'anneau et l'arrêter sur l'intersection de son choix. 
   Par contre, dès que l'anneau survole un ou plusieurs pions, le joueur doit l'arrêter sur la première intersection libre immédiatement après les anneaux survolés.
- Retourner les pions survolés par l'anneau
- Le joueur doit ensuite retourner tous les pions survolés par l'anneau
- Résoudre les alignements de cinq pions de même couleur
- Si le joueur réalise un alignement de cinq pions à sa couleur, il doit retirer les cinq pions du plateau et les retourner dans la réserve. 
   Pour marquer son point de victoire, il doit ensuite retirer un de ses anneaux du plateau (celui qu'il vient de déplacer ou n'importe quel autre) et le placer sur un des 3 cercles au bord du plateau.
- Si l'alignement réalisé contient plus de cinq pions, le joueur retire cinq pions contigus de son choix.
- Si plusieurs alignements à sa couleur sont réalisés, le joueur peut les résoudre dans l'ordre de son choix.
- Si des alignements adverses sont réalisés, le joueur résout d'abord ses propres alignements avant de laisser l'adversaire résoudre les siens.
- Fin de la partie
- Dès qu'un joueur possède trois anneaux de victoire, il gagne la partie."""

        self.__bg_canvas.create_text(self.__w//2, self.__h // 2, text=rules_text, fill="black", font=("Helvetica", int(2020/175), "bold"), tags="text")

    def quit_button_clicked(self, event):
        self.__bg_canvas.delete("croix_image","frame","text")

        self.__bg_canvas.create_image(self.__w/(2020/400),self.__h-175,image=self.__start, tags="start_image")
        self.__bg_canvas.create_image(self.__w/(2020/1000),self.__h-175,image=self.__rules, tags="rules_image")
        self.__bg_canvas.create_image(self.__w/(2020/1600),self.__h-175,image=self.__leave, tags="leave_image")

    def quit_button_enter(self, event):
        self.__croixhoverimage = Image.open("img/buttons/croixhover.png")
        self.__croixhoverimage=self.__croixhoverimage.resize((int(self.__w/(2020/90)),int(self.__h/(2020/150))))
        self.__croixhoverimage = ImageTk.PhotoImage(self.__croixhoverimage)
        self.__bg_canvas.itemconfig("croix_image", image=self.__croixhoverimage)

    def quit_button_leave(self, event):
        self.__bg_canvas.itemconfig("croix_image", image=self.__croiximage)

