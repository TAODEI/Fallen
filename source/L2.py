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

    def update(self, surface, keys):
        for event in pygame.event.get():
            print(2222222)
            if event.type is pygame.KEYDOWN:
               
                if event.key is pygame.K_a:
                    self.down = True
        if self.down:
            surface.blit(self.background2, surface.get_rect())
        else:
            surface.blit(self.background, surface.get_rect())
