#!/usr/bin/python3

from tkinter import *

def deplacement_balle():
	global dx, dy
	canevas.move(balle,dx ,dy)
	Fenetre.after(10, deplacement_balle)

def deplacement_raq():
	global rx, ry
	canevas.move(raquette, rx, ry)
	Fenetre.after(8, deplacement_raq)


#Deplacement des modules
dx, rx = 2, 0
dy, ry = 0, 1

#Fenetre graphique
Fenetre = Tk()
canevas = Canvas(Fenetre, width=700, height=500, bg='white', bd=8, cursor='rtl_logo')
canevas.pack()

#Initialisation des modules
raquette = canevas.create_rectangle(10, 100, 30, 200, fill='red', width=2)
raquette = canevas.create_rectangle(700, 300, 680, 400, fill='blue', width=2)
balle = canevas.create_oval(340, 240, 360, 260, fill='green', width=2)
canevas.create_line(350, 0, 350, 500, fill='black')

#Initialisation des buton
Bouton_Quitter = Button(Fenetre, text='Quitter', command = Fenetre.destroy)
Bouton_Quitter.pack()
Bouton_Debut = Button(Fenetre, text='Start', command = balle)
Bouton_Debut.pack()

deplacement_raq()
deplacement_balle()

#Boucle infinie
Fenetre.mainloop()