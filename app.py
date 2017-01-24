import pygame

class Application:
    def __init__(self,window,theme=None):
        self.window = window
        self.theme = theme

    def run(self):
        self.window.connect_application(self)
        self.window.construct()
        self.running = True
        while self.running:
            self.window.draw()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.suggest_quit()
                if event.type == pygame.MOUSEMOTION:
                    p = event.pos
                    self.window.handle_motion(p)
        self.window.deconstruct()
    
    def suggest_quit(self,*args,**kwargs):
        self.running = False