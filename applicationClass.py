#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from tkinter import *


class monApp:
    def __init__(self):
        self.root = Tk()

    def setFullScreen(self):
        self.root.attributes("-fullscreen", 1)

    def setRootName(self, nomF):
        self.root.title(nomF)

    def getScreenWidth(self):
        return self.root.winfo_screenwidth()

    def getScreenHeight(self):
        return self.root.winfo_screenheight()

    def resizeScreen(self, x, y):
        self.root.geometry("%s*%s+800+450"%(str(x), str(y)))

    def startApp(self):
        self.root.mainloop()
