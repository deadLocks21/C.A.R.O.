#! /usr/bin/env python374
# -*- encoding: utf-8 *-

import sqlite3

conn = sqlite3.connect('widgets.db')
cursor = conn.cursor()


def selectCanvasByName(nameI):
    c = conn.execute("SELECT * from canvas WHERE nomCanvas = '" + nameI + "';")

    return c
