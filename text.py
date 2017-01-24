import pygame

from .obj import Obj
from .themes import TwoColorThematics

class BasicText(Obj,TwoColorThematics):
    def __init__(self,text='',font='Helvetica,Arial',font_size=26,bg_color='default_bg',fg_color='default_fg'):
        Obj.__init__(self)
        TwoColorThematics.__init__(self,bg_color,fg_color)
        self.font_size = font_size
        self.set_font(font)
        self.set_text(text)


    def set_font(self,font):
        if font is None:
            self.font = pygame.font.Font(None,self.font_size)
        elif isinstance(font,str):
            self.font = pygame.font.SysFont(font,self.font_size)
        elif isinstance(font,pygame.font.Font):
            self.font = font
        else:
            raise TypeError('Bad font identifier')

    def set_text(self,text):
        self.text = text
        if self.application:
            self.rebuild_text_surface()

    def rebuild_text_surface(self):
        self.text_surface = self.font.render(self.text,1,self.fg_raw)

    def suggest_min_metrics(self):
        return pygame.Rect(0,0,*self.font.size(self.text))

    def connect_application(self,application):
        Obj.connect_application(self,application)
        self.rebuild_colors()
        self.rebuild_text_surface()

class SimpleText(BasicText):
    
    def draw(self,surface,rect):
        pygame.draw.rect(surface,self.bg_raw,rect)

        blit_x = rect.centerx - (self.text_surface.get_width()//2)
        blit_y = rect.centery - (self.text_surface.get_height()//2)

        surface.blit(self.text_surface,(blit_x,blit_y))

class MultilineText(BasicText):
    def suggest_min_metrics(self):
        return pygame.Rect(0,0,self.font.size(self.text)[0],self.font.get_linesize()*len(self.text.split('\n')))

    def draw(self,surface,rect):
        pygame.draw.rect(surface,self.bg_raw,rect)
        blit_y = rect.centery - ((self.font.get_linesize()*len(self.text.split('\n')))//2)
        step_y = self.font.get_linesize()

        for line in self.text.split('\n'):
            text_surface = self.font.render(line,1,self.fg_raw)
            blit_x = rect.centerx - (text_surface.get_width()//2)
            blit_y += step_y
            surface.blit(text_surface,(blit_x,blit_y))