#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from tkinter import *


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


def createLayout(r, w, h):
    return Canvas(r, highlightthickness=0, width=w, height=h, background='#6746F4')


def placeLayout(l, w, h):
    l.place(x=0, y=0, width=w, height=h)
