#! /usr/bin/env python374
# -*- encoding: utf-8 *-

import sqlite3

conn = sqlite3.connect('widgets.db')
cursor = conn.cursor()


def selectCanvasByName(nameI):
    c = conn.execute("SELECT * from canvas WHERE nomCanvas = '" + nameI + "';")
    print("[DATABASE] Selection du canvas qui se nomme %s"%nameI)

    return c


def dernierResultat(c):
    for row in c:
        row = row

    return row
