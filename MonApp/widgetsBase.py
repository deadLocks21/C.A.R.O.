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
     highlightbackground VARCHAR(43) DEFAULT 'None',
     highlightcolor VARCHAR(43) DEFAULT 'None',
     highlightthickness INTEGER DEFAULT 1,
     relief VARCHAR(43) DEFAULT 'flat',
     width INTEGER NOT NULL,
     x INTEGER DEFAULT 0,
     y INTEGER DEFAULT 0
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS button(
    nomButton VARCHAR(43) NOT NULL,
    root VARCHAR(43) NOT NULL,
    text TEXT DEFAULT '',
    textvariable VARCHAR(43) DEFAULT 'None',
    relief VARCHAR(43) DEFAULT 'flat',
    bg VARCHAR(43) DEFAULT '#AAAAAA',
    fg VARCHAR(43) DEFAULT '#000000',
    font VARCHAR(43) DEFAULT 'myFont',
    image VARCHAR(43) DEFAULT 'None',
    borderwidth INTEGER DEFAULT 2,
    x INTEGER DEFAULT 0,
     y INTEGER DEFAULT 0,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL,
    command VARCHAR(43) DEFAULT 'None'
    );
""")

conn.commit()

conn.close()
