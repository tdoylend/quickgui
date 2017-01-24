import pygame

from .text import BasicText

class ListBox(BasicText):
    def __init__(self,options,*args,**kwargs):
        BasicText.__init__(self,*args,**kwargs)
        
        self.options = options

        self.scroll_y = 0
        