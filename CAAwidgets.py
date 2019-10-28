#! /usr/bin/env python374
# -*- encoding: utf-8 *-

import sqlite3

conn = sqlite3.connect('widgets.db')
cursor = conn.cursor()

cursor.execute("""INSERT INTO canvas (nomCanvas, root, height, width, background) 
VALUES ('main', 'root', 0, 0, '#CC33FF');""")

conn.commit()

conn.close()