from .import setup
import pygame

class Level12:
    def __init__(self):
        self.ok = True
        self.state = -1
        self.background = setup.GRAPHICS['black']
        self.b1 = setup.GRAPHICS['12.1']
        self.b2 = setup.GRAPHICS['12.2']
        self.b3 = setup.GRAPHICS['12.3']
        self.b4 = setup.GRAPHICS['12.4']
        self.b5 = setup.GRAPHICS['12.5']
        self.b6 = setup.GRAPHICS['12.6']
        self.b7 = setup.GRAPHICS['12.7']
        self.b8 = setup.GRAPHICS['12.8']
        self.b9 = setup.GRAPHICS['12.9']
        self.b10 = setup.GRAPHICS['12.10']
        self.b11 = setup.GRAPHICS['12.11']
        self.b12 = setup.GRAPHICS['12.12']
        self.b13 = setup.GRAPHICS['12.13']
        self.b14 = setup.GRAPHICS['12.14']
        self.b15 = setup.GRAPHICS['12.15']
        self.b16 = setup.GRAPHICS['12.16']
        
        self.timer = 0
    def update(self, surface, keys, dir):
        surface.blit(self.background, surface.get_rect())
