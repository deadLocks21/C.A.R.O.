#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from MonApp.MonApp import *

APPLICATION_NAME = "CAA-createAnAlgorithm""CAA-createAnAlgorithm"  # Nom de l'application

CANVAS_INFO = {'options': ('root', 'borderwidth', 'background', 'height')}

root = Tk()  # Creation de la fenetre tkinter
w = getScreenWidth(root)  # Stockage de la largeur de l'ecran
h = getScreenHeight(root)  # Stockage de la hauteur de l'ecran

setFullScreen(root)  # Mettre l'application en plein ecran
setRootName(root, APPLICATION_NAME)  # Renommer le nom de la fenetre

Menu = createLayout(root, w, h)  # Creation d'un canvas
placeLayout(Menu, w, h)  # Placement de ce dernier

startApp(root)  # Lancement de l'application
