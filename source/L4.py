from .import setup
import pygame, time

class Level4:
    def __init__(self):
        self.ok = True
        self.state = 2
        self.background = setup.GRAPHICS['2_1']
        self.b2 = setup.GRAPHICS['2_2']
        self.b3 = setup.GRAPHICS['2_3']
        self.b4 = setup.GRAPHICS['2_4']
        self.b5 = setup.GRAPHICS['2_5']
        self.b6 = setup.GRAPHICS['2_6']
        self.b7 = setup.GRAPHICS['2_7']
        self.b8 = setup.GRAPHICS['2_8']
        self.b9 = setup.GRAPHICS['2.9']
        self.current_time = pygame.time.get_ticks()
        self.timer = 0

def update(self, surface, keys, dir):
        if self.state < 3:
            self.update_cloud_and_girl(surface)
        if 'down' in dir and self.ok == False:
            print(self.state)

            print(dir['x'], dir['y'])

            if self.state == 2:
                surface.blit(self.b3, surface.get_rect())
                self.state += 1
            elif self.state == 3 and dir['x'] < 280 and dir['y'] > 100 and dir['y'] < 340:
                surface.blit(self.b4, surface.get_rect())
                self.state += 1
            elif self.state == 4:
                surface.blit(self.b5, surface.get_rect())
                self.state += 1
            elif self.state == 5 and dir['x'] > 80 and dir['x'] < 200 and dir['y'] > 200 and dir['y'] < 400:
                surface.blit(self.b6, surface.get_rect())
                self.state += 1
            elif self.state == 6:
                surface.blit(self.b7, surface.get_rect())
                self.state += 1
                self.timer = pygame.time.get_ticks()
        if self.state == 7:
            if pygame.time.get_ticks() - self.timer > 2000 and pygame.time.get_ticks() - self.timer < 4000:
                surface.blit(self.b8, surface.get_rect())
            if pygame.time.get_ticks() - self.timer > 4000 and pygame.time.get_ticks() - self.timer < 6000:
                surface.blit(self.b9, surface.get_rect())
                return True
        return False