import pygame

from .raw_color import compute_raw_color

class Theme:
    def __init__(self,**kwargs):
        self.__dict__ = kwargs

    def __getitem__(self,item):
        return self.__dict__[item]

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

default_theme = Theme(
    default_bg = (240,240,240),
    default_fg = (0,0,0),

    default_button_bg = (160,160,160),
    default_button_fg = (0,0,0),
    default_button_border = (0,0,0),

    default_button_hi_bg = (96,96,96),
    default_button_hi_fg = (240,240,240),
    default_button_hi_border = (0,0,0),
)