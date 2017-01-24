import pygame

def relative_rect(position,rect):
    return position[0]-rect.x,position[1]-rect.y