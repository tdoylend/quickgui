#Quick GUI
#(C) 2017 Thomas Doylend
#
#This software is released under the terms of the MIT License.


#TODO: Make suggest_min_metrics consider children's min metrics.
#TODO: Add text selection, copy/paste, etc.
#TODO: Fix bugs in MultilineText

#NOTE: When using things like transitions, remember to detach before reconnecting.


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
import button
import relation

from easygui_emulation import * #Comment out this line if you're building custom GUIs.

