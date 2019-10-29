#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from tkinter import *
from PIL import Image, ImageTk

APPLICATION_NAME = "CAA-CreateAnAlgorithm"
POURCENT_BT = 0.035

# Création de la fenêtre principale
root = Tk()

# Mise en plein écran et renommage de root
root.attributes("-fullscreen", 1)
root.title(APPLICATION_NAME)

# Largeur et hauteur de l'écran
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

# Canvas contenant les éléments visuels de l'application
main = Canvas(root, highlightthickness=0)

# Création du fond d'écran image
fond_pil = Image.open('images/fond.png')
fond_resolution = (w, h)
fond_img = ImageTk.PhotoImage(fond_pil.resize(fond_resolution))
fond = main.create_image(w / 2, h / 2, image=fond_img)

fermer_pil = Image.open('images/fermer.png')
fermerR = (int(h * POURCENT_BT * 1.5), int(h * POURCENT_BT))
fermer_img = ImageTk.PhotoImage(fermer_pil.resize(fermerR))
main.create_image(w - (fermerR[0] / 2), 0 + (fermerR[1] / 2), image=fermer_img)

reduire_pil = Image.open('images/reduire.png')
reduireR = (int(h * POURCENT_BT * 1.5), int(h * POURCENT_BT))
reduire_img = ImageTk.PhotoImage(reduire_pil.resize(reduireR))
main.create_image(w - (reduireR[0] / 2) * 3, 0 + (reduireR[1] / 2), image=reduire_img)


def reduireProg():
    root.state('iconic')


def fermerProg():
    root.quit()


def oeilDeMoscou(event):
    print(event.x, "x", event.y)

    if (w - fermerR[0] - reduireR[0]) < event.x < (w - fermerR[0]) and 0 < event.y < reduireR[1]:
        reduireProg()

    if (w - fermerR[0]) < event.x < w and 0 < event.y < reduireR[1]:
        fermerProg()


root.bind('<Button-1>', oeilDeMoscou)

# Affichage du main
main.place(x=0, y=0, width=w, height=h)

# Lancement de l'application
root.mainloop()
