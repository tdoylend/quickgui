import pygame

import time

from .obj import Obj
from .themes import TwoColorThematics
from .text import BasicText

class TextEntry(BasicText):
    def set_entry_handler(self,handler):
        self.handler = handler

    def handle_text(self,text):
        if text in ('\n','\r'):
            self.handler()
        else:
            self.text += text
    
    def handle_key(self,key):
        if key == pygame.K_BACKSPACE:
            if self.text:
                self.text = self.text[:-2]

    def handle_click(self,position,rect,button):
        self.application.set_text_focus(self)

    def draw(self,surface,rect):
        pygame.draw.rect(surface,self.bg_raw,rect)

        show_caret = ((time.time()-int(time.time())) > 0.5) and (self.application.text_focus is self)

        text_to_render = self.text + ('_' if show_caret else ' ')

        blit_y = rect.centery - (self.font.get_linesize()//2)
        blit_x = rect.x + 2

        font_surf = self.font.render(text_to_render,1,self.fg_raw)

        surface.blit(font_surf,(blit_x,blit_y))
        