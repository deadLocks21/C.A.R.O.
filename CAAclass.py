#! /usr/bin/env python374
# -*- encoding: utf-8 *-

from applicationClass import *

class CAA:
    APPLICATION_NAME = "CAA-createAnAlgorithm""CAA-createAnAlgorithm"

    def __init__(self):
        root = monApp()
        root.setRootName(self.APPLICATION_NAME)
        root.setFullScreen()
        root.startApp()