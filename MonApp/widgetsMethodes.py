#! /usr/bin/env python374
# -*- encoding: utf-8 *-

import sqlite3

conn = sqlite3.connect('widgets.db')
cursor = conn.cursor()


def selectItemByName(nameI, quoi):
    """Méthode permettant de selectionner un canvas en fonction de son nom"""
    SELECT = "SELECT * from %s WHERE %s = '" % (quoi, "nom" + quoi) + nameI + "';"
    i = conn.execute(SELECT)
    print("[DATABASE] Selection du canvas qui se nomme %s" % nameI)

    return i


def dernierResultat(c):
    """Méthode qui permet de récuperer le contenu d'un curseur (ici sa dernière valeur)"""
    for row in c:
        row = row

    return row
