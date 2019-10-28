#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from tkinter import *
from MonApp.widgetsBase import *
from MonApp.widgetsMethodes import *



def setFullScreen(r):
    """Mettre une fenetre en plein écran"""
    r.attributes("-fullscreen", 1)


def setRootName(r, nomF):
    """Nommer une fenetre avec le parametre nomF"""
    r.title(nomF)


def getScreenWidth(r):
    """Retourner la largeur de l'ecran"""
    return r.winfo_screenwidth()


def getScreenHeight(r):
    """Retourner la hauteur de l'ecran"""
    return r.winfo_screenheight()


def resizeScreen(r, x, y):
    """Redimensionner la taille de la fenetre"""
    r.geometry("%s*%s" % (str(x), str(y)))


def startApp(r):
    """Lancer l'application"""
    r.mainloop()


def createCanvas(info, r):
    """Creer et retourne un canvas a partir d'une ligne de la BDD"""
    # Selectionner les info de la recherche
    for row in info:
        row = row

    # Transformer les infos en variables
    (nomCanvas, root, borderwidth, background, height, highlightbackground, highlightcolor, highlightthickness, relief, width, x, y) = row

    # Creer le canvas
    c = Canvas(r, background=background, borderwidth=borderwidth, highlightbackground=highlightbackground,highlightcolor=highlightcolor, highlightthickness=highlightthickness, relief=relief)

    return c  # Retourner le canvas


def placeCanvas(info, canvas, w, h):
    """Place un canvas a partir d'une ligne de la BDD"""
    # Selectionner les info de la recherche
    for row in info:
        row = row

    # Transformer les infos en variables
    (nomCanvas, root, borderwidth, background, height, highlightbackground, highlightcolor, highlightthickness, relief, width, x, y) = row

    canvas.place(x=x, y=y, width=w, height=h)  # Placement du canvas
