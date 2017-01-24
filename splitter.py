import pygame

from .obj import Obj

class ProportionalVerticalSplitter(Obj):
    def __init__(self,proportion):
        Obj.__init__(self)

        self.child_top = None
        self.child_bottom = None
        self.proportion = proportion
    
    def add_child_top(self,child):
        if self.child_top:
            self.child_top.detach()
        self.child_top = child
        self.child_top.connect(self)

    def add_child_bottom(self,child):
        if self.child_bottom:
            self.child_bottom.detach()
        self.child_bottom = child
        self.child_bottom.connect(self)

    def connect_application(self,application):
        Obj.connect_application(self,application)
        if self.child_top:
            self.child_top.connect_application(application)
        if self.child_bottom:
            self.child_bottom.connect_application(application)

    def draw(self,surface,rect):
        self.split_location = int(rect.height * self.proportion)
        self.remaining_space = rect.height - self.split_location

        if self.child_top:
            self.child_top.draw(surface,pygame.Rect(rect.x,rect.y,rect.width,self.split_location))
        
        if self.child_bottom:
            self.child_bottom.draw(surface,pygame.Rect(rect.x,rect.y+self.split_location,rect.width,self.remaining_space))
