import pygame

from .themes import TwoColorThematics

class Obj:
    def __init__(self):
        self.parent = None
        self.application = None

    def draw(self,surface,rect):
        pass

    def suggest_min_metrics(self):
        return pygame.Rect(0,0,0,0)

    def suggest_max_metrics(self):
        return None

    def connect(self,parent):
        self.parent = parent

    def detach(self):
        self.parent = None
    
    def connect_application(self,application):
        self.application = application

    def handle_motion(self,position,rect):
        pass

    def handle_leave(self):
        pass

    def handle_click(self,position,rect,button):
        pass

    def handle_text(self,text):
        pass

    def handle_key(self,key):
        pass

class SingleChildObj(Obj):
    def __init__(self):
        Obj.__init__(self)
        self.child = None

    def add_child(self,child):
        if self.child:
            self.child.detach()
        self.child = child
        self.child.connect(self)

    def connect_application(self,application):
        Obj.connect_application(self,application)
        if self.child: self.child.connect_application(application)

class TestPanel(Obj):
    def draw(self,surface,rect):
        pygame.draw.rect(surface,(128,0,128),rect)

class BorderPanel(SingleChildObj,TwoColorThematics):
    def __init__(self,bg_color='default_bg',fg_color='default_fg',in_padding=1,out_padding=2,border=1):
        SingleChildObj.__init__(self)
        TwoColorThematics.__init__(self,bg_color,fg_color)
        self.in_padding = in_padding
        self.out_padding = out_padding
        self.total_padding = self.in_padding+self.out_padding
        self.border = border

    def connect_application(self,application):
        SingleChildObj.connect_application(self,application)
        self.rebuild_colors()

    def handle_motion(self,position,rect):
        if self.child:
            if self.derivative_rect(rect).collidepoint(position):
                self.child.handle_motion(position,self.derivative_rect(rect))
            else:
                self.child.handle_leave()

    def handle_click(self,position,rect,button):
        if self.child:
            if self.derivative_rect(rect).collidepoint(position):
                self.child.handle_click(position,self.derivative_rect(rect),button)
            else:
                self.child.handle_leave()
    
    def handle_leave(self):
        if self.child: self.child.handle_leave()    

    def derivative_rect(self,rect):
        return pygame.Rect(
            rect.left+self.total_padding,
            rect.top+self.total_padding,
            rect.width-self.total_padding*2,
            rect.height-self.total_padding*2
        )


    def suggest_min_metrics(self):
        if self.child:
            m = self.child.suggest_min_metrics()
            return pygame.Rect(0,0,m.width+self.total_padding*2,m.height+self.total_padding*2)
        else:
            return pygame.Rect(0,0,self.total_padding*2,self.total_padding*2)

    def draw(self,surface,rect):
        pygame.draw.rect(surface,self.bg_raw,rect)

        #margin = self.padding / 2
        if self.border:
            pygame.draw.line(
                surface,
                self.fg_raw,
                (rect.left+self.out_padding-1,rect.top+self.out_padding-1),
                (rect.right-self.out_padding,rect.top+self.out_padding-1),
                self.border
            )

            pygame.draw.line(
                surface,
                self.fg_raw,
                (rect.right-self.out_padding,rect.bottom-self.out_padding),
                (rect.left+self.out_padding,rect.bottom-self.out_padding),
                self.border
            )

            pygame.draw.line(
                surface,
                self.fg_raw,
                (rect.right-self.out_padding,rect.bottom-self.out_padding),
                (rect.right-self.out_padding,rect.top+self.out_padding),
                self.border
            )

            pygame.draw.line(
                surface,
                self.fg_raw,
                (rect.left+self.out_padding-1,rect.top+self.out_padding),
                (rect.left+self.out_padding-1,rect.bottom-self.out_padding),
                self.border
            )

        if self.child:
            self.child.draw(
                surface,
                self.derivative_rect(rect)
            )