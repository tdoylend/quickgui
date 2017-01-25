import pygame
import time

from .text import BasicText

class ListBox(BasicText):
    def __init__(self,options,*args,**kwargs):
        BasicText.__init__(self,*args,**kwargs)
        
        self.options = options

        self.scroll_y = 0

        self.selection = None

        self.handler = None

        self.double_click_timeout = time.time() - 5 #TODO: Fix this awful hack too
    
    def set_handler(self,handler):
        self.handler = handler

    def suggest_min_metrics(self):
        return pygame.Rect(0,0,640,self.font.get_linesize()*len(self.options))

    def draw(self,surface,rect):
        pygame.draw.rect(surface,self.bg_raw,rect)
        blit_x = rect.x + 2
        blit_y = rect.y + 2

        for item in self.options:
            surface.blit(self.font.render(item,1,self.fg_raw),(blit_x,blit_y))
            blit_y += self.font.get_linesize()

        if self.selection is not None:
            pygame.draw.rect(surface,self.fg_raw,(rect.x+2,rect.y+2+(self.selection*self.font.get_linesize()),rect.width-4,self.font.get_linesize()),1)
        
    def handle_click(self,position,rect,button):

        absolute_y = position[1] - rect.y

        item = absolute_y // self.font.get_linesize()

        if (item < len(self.options)) and (item>=0):
            self.selection = item
        else:
            self.selection = None

        if (time.time() - self.double_click_timeout) < .3:
            self.handler(self.selection) 
        
        self.double_click_timeout = time.time()

    def handle_key(self,key):
        if key == pygame.K_UP:
            if self.selection is None:
                self.selection = len(self.options) - 1
            elif self.selection == 0:
                self.selection = len(self.options) - 1
            else:
                self.selection -= 1
        elif key == pygame.K_DOWN:
            if self.selection is None:
                self.selection = 0
            elif self.selection == (len(self.options)-1):
                self.selection = 0
            else:
                self.selection += 1
        elif key == pygame.K_RETURN:
            self.handler(self.selection)