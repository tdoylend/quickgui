import pygame

from .obj import Obj
from .themes import TwoColorThematics

class SimpleText(Obj,TwoColorThematics):
    def __init__(self,text,font=None,bg_color='default_bg',fg_color='default_fg'):
        Obj.__init__(self)
        TwoColorThematics.__init__(self,bg_color,fg_color)
        self.set_font(font)
        self.set_text(text)

    def set_font(self,font):
        if font is None:
            self.font = pygame.font.Font(None,26)

    def set_text(self,text):
        self.text = text
        if self.application:
            self.rebuild_text_surface()

    def rebuild_text_surface(self):
        self.text_surface = self.font.render(self.text,1,self.fg_raw)

    def connect_application(self,application):
        Obj.connect_application(self,application)
        self.rebuild_colors()
        self.rebuild_text_surface()
    
    def draw(self,surface,rect):
        pygame.draw.rect(surface,self.bg_raw,rect)

        blit_x = rect.centerx - (self.text_surface.get_width()//2)
        blit_y = rect.centery - (self.text_surface.get_height()//2)

        surface.blit(self.text_surface,(blit_x,blit_y))