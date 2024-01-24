from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from pygame import mixer
import pygame

class Rules:
    
    def __init__(self):
        self.__root = Tk()
        self.__root.title("Rules")
        self.__root.config(bg="black")

        rules_text = ("""Pour commencer la partie \n Placer le plateau au centre de la table. Chaque joueur choisir sa couleur: noir ou blanc. \n Le tour de jeu \nPhase 1: placement des anneaux sur le plateauTour à tour, en commençant par le joueur blanc, chaque joueur place un anneau à sa couleur sur une intersection libre du plateau.

Phase 2: déplacement des anneaux

Blanc commence. Tour à tour, chaque joueur doit déplacer un de ses anneaux en respectant les règles suivantes:

Choisir l'anneau à déplacer
Le joueur choisit un de ses anneaux sur le plateau.
Placer un pion à sa couleur au centre de l'anneau
Le joueur prend un pion dans la réserve et le place au centre de l'anneau.
La face visible du pion doit être à la couleur du joueur.
Déplacer l'anneau
Le joueur doit déplacer l'anneau, en ligne droite dans une des six directions, et arrêter le parcours sur une intersection libre.
Au cours de son déplacement, l'anneau peut survoler des intersections libres ou occupées par des pions. Par contre, l'anneau ne peut pas survoler d'autres anneaux.
Tant que l'anneau survole des intersections libres, le joueur peut déplacer l'anneau et l'arrêter sur l'intersection de son choix. Par contre, dès que l'anneau survole un ou plusieurs pions, le joueur doit l'arrêter sur la première intersection libre immédiatement après les anneaux survolés.
Retourner les pions survolés par l'anneau
Le joueur doit ensuite retourner tous les pions survolés par l'anneau
Résoudre les alignements de cinq pions de même couleur
Si le joueur réalise un alignement de cinq pions à sa couleur, il doit retirer les cinq pions du plateau et les retourner dans la réserve. Pour marquer son point de victoire, il doit ensuite retirer un de ses anneaux du plateau (celui qu'il vient de déplacer ou n'importe quel autre) et le placer sur un des 3 cercles au bord du plateau.
Si l'alignement réalisé contient plus de cinq pions, le joueur retire cinq pions contigus de son choix.
Si plusieurs alignements à sa couleur sont réalisés, le joueur peut les résoudre dans l'ordre de son choix.
Si des alignements adverses sont réalisés, le joueur résout d'abord ses propres alignements avant de laisser l'adversaire résoudre les siens.
Fin de la partie
Dès qu'un joueur possède trois anneaux de victoire, il gagne la partie.""")
        label = Label(self.__root, text=rules_text, padx=20, pady=20, bg="black", foreground="white")                                       
        label.pack()                                                                                                                         

        self.__root.mainloop()