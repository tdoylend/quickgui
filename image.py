import pygame

from .obj import Obj

class Image(Obj):
    def __init__(self,url):
        self.image = pygame.image.load(url)

    def suggest_min_metrics(self):
        return self.image.get_rect()
    
    def draw(self,surface,rect):
        pass