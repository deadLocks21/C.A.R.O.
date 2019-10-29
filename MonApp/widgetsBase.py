#! /usr/bin/env python374
# -*- encoding: utf-8 *-

import sqlite3

conn = sqlite3.connect('widgets.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS canvas(
     nomCanvas VARCHAR(43) UNIQUE NOT NULL,
     root VARCHAR(43) NOT NULL,
     borderwidth INTEGER DEFAULT 2,
     background VARCHAR(43) DEFAULT '#E4E4E4',
     height INTEGER NOT NULL,
     highlightbackground VARCHAR(43) DEFAULT NULL,
     highlightcolor VARCHAR(43) DEFAULT NULL,
     highlightthickness INTEGER DEFAULT 1,
     relief VARCHAR(43) DEFAULT 'flat',
     width INTEGER NOT NULL,
     x INTEGER DEFAULT 0,
     y INTEGER DEFAULT 0
);
""")
print("[DATABASE] Création de la table canvas.")

cursor.execute("""
CREATE TABLE IF NOT EXISTS button(
    nomButton VARCHAR(43) UNIQUE NOT NULL,
    root VARCHAR(43) NOT NULL,
    text TEXT DEFAULT '',
    textvariable VARCHAR(43) DEFAULT NULL,
    relief VARCHAR(43) DEFAULT 'flat',
    bg VARCHAR(43) DEFAULT '#AAAAAA',
    fg VARCHAR(43) DEFAULT '#000000',
    font VARCHAR(43) DEFAULT 'myFont',
    image VARCHAR(43) DEFAULT NULL,
    borderwidth INTEGER DEFAULT 2,
    x INTEGER DEFAULT 0,
     y INTEGER DEFAULT 0,
    width INTEGER,
    height INTEGER,
    command VARCHAR(43) DEFAULT NULL
    );
""")
print("[DATABASE] Création de la table button.")

cursor.execute("""
CREATE TABLE IF NOT EXISTS label(
    nomLabel VARCHAR(43) UNIQUE NOT NULL,
    root VARCHAR(43) NOT NULL,
    text TEXT DEFAULT NULL,
    textvariable VARCHAR(43) DEFAULT NULL,
    bg VARCHAR(43) DEFAULT '#AAAAAA',
    font VARCHAR(43) DEFAULT 'myFont',
    x INTEGER DEFAULT 0,
    y INTEGER DEFAULT 0,
    width INTEGER,
    height INTEGER
    );
""")
print("[DATABASE] Création de la table label.")

conn.commit()

from CAAwidgets import *

conn.close()
