import pygame

from .obj import SingleChildObj

class Window(SingleChildObj):
    def __init__(self,title,size,fullscreen=False):
        SingleChildObj.__init__(self)
        self.fix(size)
        self.fullscreen = fullscreen
        self.title = title

        self.surface = None

    def fix(self,size):
        self.size = size
        self.width,self.height = self.size

    def handle_motion(self,position):
        if self.child:
            self.child.handle_motion(position,self.surface.get_rect())

    def handle_click(self,position,button):
        if self.child:
            self.child.handle_click(position,self.surface.get_rect(),button)

    def construct(self):
        pygame.display.init()
        self.surface = pygame.display.set_mode(self.size,(pygame.FULLSCREEN&self.fullscreen)|pygame.RESIZABLE)
        pygame.display.set_caption(self.title)

    def redimension(self,size):
        self.size = size
        self.width,self.height = self.size
        self.surface = pygame.display.set_mode(self.size,(pygame.FULLSCREEN&self.fullscreen)|pygame.RESIZABLE)

    def deconstruct(self):
        pygame.display.quit()
        self.surface = None

    def draw(self):
        if self.child:
            self.child.draw(self.surface,self.surface.get_rect())

    def handle_text(self,text):
        if self.application.text_focus:
            self.application.text_focus.handle_text(text)
    
    def handle_key(self,key):
        if self.application.text_focus:
            self.application.text_focus.handle_key(key)