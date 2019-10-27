#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from tkinter import *

def setFullScreen(r):
    r.attributes("-fullscreen", 1)


def setRootName(r, nomF):
    r.title(nomF)


def getScreenWidth(r):
    return r.winfo_screenwidth()


def getScreenHeight(r):
    return r.winfo_screenheight()


def resizeScreen(r, x, y):
    r.geometry("%s*%s+800+450" % (str(x), str(y)))


def startApp(r):
    r.mainloop()


def createLayout(r, w, h):
    return Canvas(r, highlightthickness=0, width=w, height=h, background='#6746F4')


def placeLayout(l, w, h):
    l.place(x=0, y=0, width=w, height=h)
