#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from MonApp.MonApp import *
import sqlite3

APPLICATION_NAME = "CAA-createAnAlgorithm""CAA-createAnAlgorithm"  # Nom de l'application
conn = sqlite3.connect('widgets.db')
cursor = conn.cursor()


root = createRoot()  # Creation de la fenetre tkinter
w = getScreenWidth(root)  # Stockage de la largeur de l'ecran
h = getScreenHeight(root)  # Stockage de la hauteur de l'ecran

setFullScreen(root)  # Mettre l'application en plein ecran
setRootName(root, APPLICATION_NAME)  # Renommer le nom de la fenetre

main = CPcanvas("main", root)  # Création et affichage du canvas main

bt2 = CPbutton("bt1", root)


startApp(root)  # Lancement de l'application
