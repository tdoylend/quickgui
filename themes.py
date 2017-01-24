import pygame

from .raw_color import compute_raw_color

class Theme:
    def __init__(self,**kwargs):
        self.__dict__ = kwargs

class TwoColorThematics:
    def __init__(self,bg_color,fg_color):
        self.set_bg(bg_color)
        self.set_fg(fg_color)

    def set_bg(self,color):
        self.bg = color
        if self.application:
            self.rebuild_colors()

    def set_fg(self,color):
        self.fg = color
        if self.application:
            self.rebuild_colors()

    def rebuild_colors(self):
        #NOTE: Call only after calling connect_application.
        self.bg_raw = compute_raw_color(self.application,self.bg)
        self.fg_raw = compute_raw_color(self.application,self.fg)

    #NOTE: Always call rebuild_colors in connect_application