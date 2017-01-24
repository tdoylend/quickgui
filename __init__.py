#Quick GUI
#(C) 2017 Thomas Doylend
#
#This software is released under the terms of the MIT License.


#TODO: Make suggest_min_metrics consider children's min metrics.
#TODO: Add text selection, copy/paste, etc.


import pygame

pygame.init()

import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

import raw_color
import obj
import themes
import app
import splitter
import text
import window

from easygui_emulation import * #Comment out this line if you're building custom GUIs.

