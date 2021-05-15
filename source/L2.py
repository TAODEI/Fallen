from .import setup
import pygame

class Level2:
    def __init__(self):
        #self.timer = pygame.
        self.background = setup.GRAPHICS['2_1']
        self.background_rect = self.background.get_rect()
        self.state = 0
        
        self.background2 = setup.GRAPHICS['2_2']
        # self.current_time = pygame.time.get_ticks()
    def update(self, surface, keys, dir):
        if 'down' in dir:
            self.state += 1
            print(self.state)
        if keys[pygame.K_RIGHT]:
            self.state += 1
        if self.state:
            surface.blit(self.background2, surface.get_rect())
        else:
            surface.blit(self.background, surface.get_rect())
