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
