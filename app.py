import pygame

import themes

class Application:
    def __init__(self,window,theme=None):
        self.window = window
        if theme: self.theme = theme
        else: self.theme = themes.default_theme

        self.text_focus = None

    def set_text_focus(self,obj):
        self.text_focus = obj

    def run(self):
        self.window.connect_application(self)
        self.window.construct()
        pygame.key.set_repeat(500,50)
        self.running = True
        self.return_value = None
        while self.running:
            self.window.draw()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.suggest_quit()
                if event.type == pygame.MOUSEMOTION:
                    p = event.pos
                    self.window.handle_motion(p)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    p = event.pos
                    b = event.button

                    self.window.handle_click(p,b)
                if event.type == pygame.VIDEORESIZE:
                    self.window.redimension(event.size)
                if event.type == pygame.KEYDOWN:
                    self.window.handle_text(event.unicode)
                    self.window.handle_key(event.key)
        self.window.deconstruct()
        return self.return_value
    

    def suggest_quit(self,*args,**kwargs):
        self.running = False
        if 'return_value' in kwargs:
            self.return_value = kwargs['return_value']