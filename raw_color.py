import pygame

def compute_raw_color(application,color):
    if isinstance(color,tuple):
        return pygame.Color(*color)
    elif isinstance(color,pygame.Color):
        return color
    elif isinstance(color,str):
        if not application.theme:
            raise ValueError('Widget demands color theme but application non-themed')
        return pygame.Color(application.theme[color])
    else:
        raise TypeError('Unsupported color declaration')