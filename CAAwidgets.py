#! /usr/bin/env python374
# -*- encoding: utf-8 *-

import sqlite3

conn = sqlite3.connect('widgets.db')
cursor = conn.cursor()


# Canvas
try:
    cursor.execute("""INSERT INTO canvas (nomCanvas, root, height, width, background) VALUES ('main', 'root', 0, 0, '#CC33FF');""")
    print("[DATABASE] Insertion des canvas dans la base de donnée")

except sqlite3.IntegrityError:  # Erreur qui apparait en cas de doublon
    pass


# Button
try:
    cursor.execute("""INSERT INTO button (nomButton, root, text) VALUES ('bt', 'root', 'Salut');""")
    print("[DATABASE] Insertion des boutons dans la base de donnée")

except sqlite3.IntegrityError:  # Erreur qui apparait en cas de doublon
    pass

conn.commit()

conn.close()
