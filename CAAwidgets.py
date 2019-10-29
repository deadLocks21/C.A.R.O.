#! /usr/bin/env python374
# -*- encoding: utf-8 *-

import sqlite3

conn = sqlite3.connect('widgets.db')
cursor = conn.cursor()


# Canvas
try:
    cursor.execute("""INSERT INTO canvas (nomCanvas, root, height, width, background) VALUES ('main', 'root', 0, 0, '#CC33FF');""")

except sqlite3.IntegrityError:  # Erreur qui apparait en cas de doublon
    pass
print("[DATABASE] Insertion des canvas dans la base de donnée")


# Button
try:
    cursor.execute("""INSERT INTO button (nomButton, root, width, height) VALUES ('bt2', 'root', 1000, 1000);""")

except sqlite3.IntegrityError:  # Erreur qui apparait en cas de doublon
    pass
print("[DATABASE] Insertion des boutons dans la base de donnée")

conn.commit()

conn.close()