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

    def derive_top_rect(self,rect):
        self.split_location = int(rect.height * self.proportion)
        self.remaining_space = rect.height - self.split_location
        return pygame.Rect(rect.x,rect.y,rect.width,self.split_location)

    def derive_bottom_rect(self,rect):
        self.split_location = int(rect.height * self.proportion)
        self.remaining_space = rect.height - self.split_location
        return pygame.Rect(rect.x,rect.y+self.split_location,rect.width,self.remaining_space)

    def draw(self,surface,rect):
        if self.child_top:
            self.child_top.draw(surface,self.derive_top_rect(rect))
        
        if self.child_bottom:
            self.child_bottom.draw(surface,self.derive_bottom_rect(rect))

    def handle_motion(self,position,rect):
        if self.derive_top_rect(rect).collidepoint(position):
            if self.child_top: self.child_top.handle_motion(position,self.derive_top_rect(rect))
            if self.child_bottom: self.child_bottom.handle_leave()
        if self.derive_bottom_rect(rect).collidepoint(position):
            if self.child_bottom: self.child_bottom.handle_motion(position,self.derive_bottom_rect(rect))
            if self.child_top: self.child_top.handle_leave()

    def handle_click(self,position,rect,button):
        if self.derive_top_rect(rect).collidepoint(position):
            if self.child_top: self.child_top.handle_click(position,self.derive_top_rect(rect),button)
            if self.child_bottom: self.child_bottom.handle_leave()
        if self.derive_bottom_rect(rect).collidepoint(position):
            if self.child_bottom: self.child_bottom.handle_click(position,self.derive_bottom_rect(rect),button)
            if self.child_top: self.child_top.handle_leave()

    def handle_leave(self):
        if self.child_top: self.child_top.handle_leave()
        if self.child_bottom: self.child_bottom.handle_leave()

class ProportionalHorizontalSplitter(Obj):
    def __init__(self,proportion):
        Obj.__init__(self)

        self.child_right = None
        self.child_left = None
        self.proportion = proportion
    
    def add_child_right(self,child):
        if self.child_right:
            self.child_right.detach()
        self.child_right = child
        self.child_right.connect(self)

    def add_child_left(self,child):
        if self.child_left:
            self.child_left.detach()
        self.child_left = child
        self.child_left.connect(self)

    def connect_application(self,application):
        Obj.connect_application(self,application)
        if self.child_right:
            self.child_right.connect_application(application)
        if self.child_left:
            self.child_left.connect_application(application)

    def derive_left_rect(self,rect):
        self.split_location = int(rect.width * self.proportion)
        self.remaining_space = rect.width - self.split_location
        return pygame.Rect(rect.x,rect.y,self.split_location,rect.height)

    def derive_right_rect(self,rect):
        self.split_location = int(rect.width * self.proportion)
        self.remaining_space = rect.width - self.split_location
        return pygame.Rect(rect.x+self.split_location,rect.y,self.remaining_space,rect.height)

    def draw(self,surface,rect):
        self.split_location = int(rect.height * self.proportion)
        self.remaining_space = rect.height - self.split_location

        if self.child_right:
            self.child_right.draw(surface,self.derive_right_rect(rect))
        
        if self.child_left:
            self.child_left.draw(surface,self.derive_left_rect(rect))

    def handle_motion(self,position,rect):
        if self.derive_right_rect(rect).collidepoint(position):
            if self.child_right: self.child_right.handle_motion(position,self.derive_right_rect(rect))
            if self.child_left: self.child_left.handle_leave()
        if self.derive_left_rect(rect).collidepoint(position):
            if self.child_left: self.child_left.handle_motion(position,self.derive_left_rect(rect))
            if self.child_right: self.child_right.handle_leave()

    def handle_click(self,position,rect,button):
        if self.derive_right_rect(rect).collidepoint(position):
            if self.child_right: self.child_right.handle_click(position,self.derive_right_rect(rect),button)
            if self.child_left: self.child_left.handle_leave()
        if self.derive_left_rect(rect).collidepoint(position):
            if self.child_left: self.child_left.handle_click(position,self.derive_left_rect(rect),button)
            if self.child_right: self.child_right.handle_leave()

    def handle_leave(self):
        if self.child_right: self.child_right.handle_leave()
        if self.child_left: self.child_left.handle_leave()