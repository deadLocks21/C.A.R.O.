#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from tkinter import *
from PIL import Image, ImageTk

APPLICATION_NAME="CAA-CreateAnAlgorithm"


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
photo = Image.open('images/fond.png')
resolution = (w, h)
img = ImageTk.PhotoImage(photo.resize(resolution))
fond = main.create_image(w/2, h/2, image=img)


# Affichage du main
main.place(x=0, y=0, width=w, height=h)


# Lancement de l'application
root.mainloop()
