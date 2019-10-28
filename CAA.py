#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from MonApp.MonApp import *

APPLICATION_NAME = "CAA-createAnAlgorithm""CAA-createAnAlgorithm"

CANVAS_INFO = {'options': ('root', 'borderwidth', 'background', 'height')}

root = Tk()
w = getScreenWidth(root)
h = getScreenHeight(root)

setFullScreen(root)
setRootName(root, APPLICATION_NAME)

Menu = createLayout(root, w, h)
placeLayout(Menu, w, h)

startApp(root)
