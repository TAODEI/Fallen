import pygame
from . import tools, setup
class MainMenu:
    def __init__(self):

        self.setup_background()
        self.next = 'load_screen'
        self.finished = False

    def setup_background(self):
        self.background = setup.GRAPHICS['19']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(self.background_rect.width / 3),
                                                                    int(self.background_rect.height / 3)))
        self.viewport = setup.SCREEN.get_rect()



    def update(self, surface, keys):
  
        #self.update_cursor(keys)

        surface.blit(self.background, self.viewport)
        #surface.blit(self.caption, (170, 100))
        #surface.blit(self.player_image, (110, 490))
        #surface.blit(self.cursor.image, self.cursor.rect)

        #self.info.update()
        #self.info.draw(surface)