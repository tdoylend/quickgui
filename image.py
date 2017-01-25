import pygame

from .obj import Obj

class Image(Obj):
    def __init__(self,url):
        self.image = pygame.image.load(url)

    def suggest_min_metrics(self):
        return self.image.get_rect()
    
    def draw(self,surface,rect):
        r = self.image.get_rect()

        blit_x = surface.centerx - r.centerx
        blit_y = surface.centery - r.centery

        surface.blit(self.image,(blit_x,blit_y))