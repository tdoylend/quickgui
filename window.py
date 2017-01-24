import pygame

from .obj import SingleChildObj

class Window(SingleChildObj):
    def __init__(self,title,size,fullscreen=False):
        SingleChildObj.__init__(self)
        self.size = size
        self.width,self.height = self.size
        self.fullscreen = fullscreen
        self.title = title

        self.surface = None

        self.text_focus = None

    def handle_motion(self,position):
        if self.child:
            self.child.handle_motion(position,)

    def set_text_focus(self,obj):
        self.text_focus = obj

    def construct(self):
        pygame.display.init()
        self.surface = pygame.display.set_mode(self.size,pygame.FULLSCREEN&self.fullscreen)
        pygame.display.set_caption(self.title)

    def deconstruct(self):
        pygame.display.quit()
        self.surface = None

    def draw(self):
        if self.child:
            self.child.draw(self.surface,self.surface.get_rect())