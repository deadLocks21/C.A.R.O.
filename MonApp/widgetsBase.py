#! /usr/bin/env python374
# -*- encoding: utf-8 *-

import sqlite3

conn = sqlite3.connect('widgets.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS canvas(
     nomCanvas VARCHAR(43) NOT NULL,
     root VARCHAR(43) NOT NULL,
     borderwidth INTEGER DEFAULT 2,
     background VARCHAR(43) DEFAULT '#E4E4E4',
     height INTEGER NOT NULL,
     highlightbackground VARCHAR(43) DEFAULT 'none',
     highlightcolor VARCHAR(43) DEFAULT 'none',
     highlightthickness INTEGER DEFAULT 1,
     relief VARCHAR(43) DEFAULT 'flat',
     width INTEGER NOT NULL,
     x INTEGER DEFAULT 0,
     y INTEGER DEFAULT 0
);
""")



conn.close()