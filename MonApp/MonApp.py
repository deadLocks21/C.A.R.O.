#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from tkinter import *
from MonApp.widgetsBase import *
from MonApp.widgetsMethodes import *


def createRoot():
    print("[TK] Création de la fenetre")
    return Tk()


def setFullScreen(r):
    """Mettre une fenetre en plein écran"""
    r.attributes("-fullscreen", 1)
    print("[TK] Passage de l'affichage de %s en fullscreen" % r)


def setRootName(r, nomF):
    """Nommer une fenetre avec le parametre nomF"""
    r.title(nomF)
    print("[TK] La fenetre %s a été renommé en %s" % (r, nomF))


def getScreenWidth(r):
    """Retourner la largeur de l'ecran"""
    return r.winfo_screenwidth()


def getScreenHeight(r):
    """Retourner la hauteur de l'ecran"""
    return r.winfo_screenheight()


def resizeScreen(r, x, y):
    """Redimensionner la taille de la fenetre"""
    r.geometry("%s*%s" % (str(x), str(y)))
    print("[TK] Redimensionnement de la fenetre %s à la taille suivante : %ix%i" % (r, x, y))


def startApp(r):
    """Lancer l'application"""
    r.mainloop()
    print("[TK] Lancement de la fenetre %s" % r)


def createCanvas(info, r):
    """Creer et retourne un canvas a partir d'une ligne de la BDD"""
    # Selectionner les info de la recherche
    info = dernierResultat(info)

    # Transformer les infos en variables
    (nomCanvas, root, borderwidth, background, height, highlightbackground, highlightcolor, highlightthickness, relief,
     width, x, y) = info

    # Creer le canvas
    c = Canvas(r, background=background, borderwidth=borderwidth, highlightbackground=highlightbackground,
               highlightcolor=highlightcolor, highlightthickness=highlightthickness, relief=relief)

    print("[TK] Création du canvas %s" % nomCanvas)
    return c  # Retourner le canvas


def placeCanvas(info, canvas, w, h):
    """Place un canvas a partir d'une ligne de la BDD"""
    # Selectionner les info de la recherche
    info = dernierResultat(info)

    # Transformer les infos en variables
    (nomCanvas, root, borderwidth, background, height, highlightbackground, highlightcolor, highlightthickness, relief,
     width, x, y) = info

    canvas.place(x=x, y=y, width=w, height=h)  # Placement du canvas
    print("[TK] Placement du canvas %s en x=%i et y= %i" % (nomCanvas, x, y))


def createButton(info, r):
    """Creer et retourne un bouton a partir d'une ligne de la BDD"""
    # Selectionner les info de la recherche
    info = dernierResultat(info)

    print(info)

    # Transformer les infos en variables
    (nomButton, root, text, textvariable, relief, bg, fg, font, image, borderwidth, x, y, width, height, command) = info

    # Creer le canvas
    b = Button(r, text=text, textvariable=textvariable, relief=relief, bg=bg, fg=fg, font=font, image=image, borderwidth=borderwidth, width=width, height=height, command=command)

    print("[TK] Création du bouton %s" % nomButton)
    return b  # Retourner le canvas


def placeButton(info, b):
    """Place un bouton a partir d'une ligne de la BDD"""
    # Selectionner les info de la recherche
    info = dernierResultat(info)

    # Transformer les infos en variables
    (nomButton, root, text, textvariable, relief, bg, fg, font, image, borderwidth, x, y, width, height, command) = info

    b.place(x=x, y=y)  # Placement du canvas
    print("[TK] Placement du canvas %s en x=%i et y= %i" % (nomButton, x, y))


def createLb(info, r):
    """Creer et retourne un label a partir d'une ligne de la BDD"""
    # Selectionner les info de la recherche
    info = dernierResultat(info)

    # Transformer les infos en variables
    (nomLabel, root, text, textvariable, bg, font, x, y, width, height) = info

    l = Label(r, text, textvariable, bg, font)


def CPcanvas(nC, r):
    """Méthode qui permet de créer et afficher un canvas"""
    c = createCanvas(selectItemByName(nC, "canvas"), r)
    placeCanvas(selectItemByName(nC, "canvas"), c, getScreenWidth(r), getScreenHeight(r))

    print("[TK] Création et affichage du canvas %s" % nC)
    return c


def CPbutton(nB, r):
    """Méthode qui permet de créer et afficher un canvas"""
    b = createButton(selectItemByName(nB, "button"), r)
    placeButton(selectItemByName(nB, "button"), b)

    print("[TK] Création et affichage du bouton %s" % nB)
    return b


