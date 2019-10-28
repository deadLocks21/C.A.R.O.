#! /usr/bin/env python374
# -*- encoding: utf-8 *-

import sqlite3

conn = sqlite3.connect('widgets.db')
cursor = conn.cursor()

try:
    cursor.execute("""INSERT INTO canvas (nomCanvas, root, height, width, background) 
VALUES ('main', 'root', 0, 0, '#CC33FF');""")
except sqlite3.IntegrityError:  # Erreur qui apparait en cas de doublon
    pass

conn.commit()

conn.close()