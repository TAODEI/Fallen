from .import setup
import pygame

class Level2:
    def __init__(self):
        #self.timer = pygame.
        self.background = setup.GRAPHICS['20']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (setup.WINDOW_WIDTH, setup.WINDOW_HEIGHT))
        self.down = False
        
        self.background2 = setup.GRAPHICS['21']
        self.background2 = pygame.transform.scale(self.background2, (setup.WINDOW_WIDTH, setup.WINDOW_HEIGHT))
        # self.current_time = pygame.time.get_ticks()
    def update(self, surface, keys):
        if keys[pygame.K_RIGHT]:
            self.down = True
        if self.down:
            surface.blit(self.background2, surface.get_rect())
        else:
            surface.blit(self.background, surface.get_rect())
