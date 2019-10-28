#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from MonApp.MonApp import *
import sqlite3

APPLICATION_NAME = "CAA-createAnAlgorithm""CAA-createAnAlgorithm"  # Nom de l'application
conn = sqlite3.connect('widgets.db')
cursor = conn.cursor()


root = Tk()  # Creation de la fenetre tkinter
w = getScreenWidth(root)  # Stockage de la largeur de l'ecran
h = getScreenHeight(root)  # Stockage de la hauteur de l'ecran

setFullScreen(root)  # Mettre l'application en plein ecran
setRootName(root, APPLICATION_NAME)  # Renommer le nom de la fenetre

Menu = createCanvas(selectCanvasByName("main"), root)
placeCanvas(selectCanvasByName("main"), Menu, w, h)


startApp(root)  # Lancement de l'application
