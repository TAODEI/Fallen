from .import setup
import pygame

class L7:
    def __init__(self):
        self.background = setup.GRAPHICS['7.1']
        self.b2 = setup.GRAPHICS['7.2']
        self.b3 = setup.GRAPHICS['7.3']
        self.b4 = setup.GRAPHICS['7.4']
        self.b5 = setup.GRAPHICS['7.5']
        self.b6 = setup.GRAPHICS['7.6']
        self.b7 = setup.GRAPHICS['7.7']
        self.b8 = setup.GRAPHICS['7.8']
        self.b9 = setup.GRAPHICS['7.9']
        self.b10 = setup.GRAPHICS['7.10']
        self.b11 = setup.GRAPHICS['7.11']
        self.b12 = setup.GRAPHICS['7.12']
        self.b13 = setup.GRAPHICS['7.13']
        self.b14 = setup.GRAPHICS['7.14']
        self.b15 = setup.GRAPHICS['7.15']
        self.b16 = setup.GRAPHICS['7.16']
        self.b17 = setup.GRAPHICS['7.17']

        self.c1 = pygame.sprite.Sprite()
        self.c1.image = pygame.transform.scale(self.b2, (int(1537 / 2), int(2048 / 2)))
        rect = self.c1.image.get_rect()
        rect.x, rect.y = -120, -20
        self.c1.rect = rect
        self.c2 = pygame.sprite.Sprite()
        self.c2.image = pygame.transform.scale(self.b3, (int(1537 / 2), int(2048 / 2)))
        rect2 = self.c2.image.get_rect()
        rect2.x, rect2.y = -90, -90
        self.c2.rect = rect2
        self.c3 = pygame.sprite.Sprite()
        self.c3.image = self.b5
        rect3 = self.c3.image.get_rect()
        rect3.x, rect3.y = 0, 0
        self.c3.rect = rect3
        self.c4 = pygame.sprite.Sprite()
        self.c4.image = self.b6
        rect4 = self.c4.image.get_rect()
        rect4.x, rect4.y = 0, 0
        self.c4.rect = rect4
        self.c5 = pygame.sprite.Sprite()
        self.c5.image = self.b7
        rect5 = self.c5.image.get_rect()
        rect5.x, rect5.y = 0, 0
        self.c5.rect = rect5

        self.timer = 0
        self.is_move = False
        self.ok = False
        self.state = 1

    def update_c(self, dir, n=1):
        w,h = self.c1.image.get_size()
        if n == 1:
            self.c1.rect.x = dir['x2'] - 500
        elif n == 2:
            self.c2.rect.x = dir['x2'] - w/2 + 180
        elif n == 3 and dir['x2'] < 100 and 460 > dir['y2'] > 236:
            self.c3.rect.x = dir['x2'] - 120
        elif n == 4 and dir['x2'] < 240 and 330 > dir['y2']:
            self.c4.rect.x = dir['x2'] - 220
        elif n == 5 and dir['x2'] > 200 and 560 > dir['y2'] > 130:
            self.c5.rect.x = dir['x2'] - w/2 + 180
            #self.c.rect.y = dir['y2'] - h/2
    def update(self, surface, keys, dir):
        if self.ok:
            if 2000 < pygame.time.get_ticks() - self.timer and self.timer != 0:
                self.state += 1
                self.timer = 0
            if 'down' in dir and self.state != 2:
                self.state += 1
            if self.state == 1:
                surface.blit(self.b8, surface.get_rect())
                self.timer = pygame.time.get_ticks()
            elif self.state == 2:
                surface.blit(self.b17, surface.get_rect())
                self.state += 1
            elif self.state == 4:
                surface.blit(self.b16, surface.get_rect())
            elif self.state == 5:
                surface.blit(self.b9, surface.get_rect())
            elif self.state == 6:
                surface.blit(self.b10, surface.get_rect())
            elif self.state == 7:
                surface.blit(self.b11, surface.get_rect())
            elif self.state == 8:
                surface.blit(self.b12, surface.get_rect())
            elif self.state == 9:
                surface.blit(self.b13, surface.get_rect())
            elif self.state == 10:
                surface.blit(self.b14, surface.get_rect())
            elif self.state == 11:
                surface.blit(self.b15, surface.get_rect())
            elif self.state == 12:
                surface.blit(self.b16, surface.get_rect())
                return True
        else:
            if 'down' in dir:
                self.is_move = True
            if 'up' in dir:
                self.is_move = False
            if self.c5.rect.x >= 300:
                self.ok = True
            elif self.c4.rect.x <= -220:
                if self.is_move:
                    print(self.c4.rect, 555)
                    print(dir['x2'], dir['y2'])
                    self.update_c(dir, 5)
                surface.blit(self.b4, surface.get_rect())
                surface.blit(self.c5.image, self.c5.rect)
            elif self.c3.rect.x <= -120:
                if self.is_move:
                    self.update_c(dir, 4)
                surface.blit(self.b4, surface.get_rect())
                surface.blit(self.b7, surface.get_rect())
                surface.blit(self.c4.image, self.c4.rect)
            elif self.c2.rect.x > 250:
                if self.is_move:
                    self.update_c(dir, 3)
                surface.blit(self.b4, surface.get_rect())
                surface.blit(self.b7, surface.get_rect())
                surface.blit(self.b6, surface.get_rect())
                surface.blit(self.c3.image, self.c3.rect)
            elif self.c1.rect.x <= -500:
                surface.blit(self.b4, surface.get_rect())
                surface.blit(self.b7, surface.get_rect())
                surface.blit(self.b6, surface.get_rect())
                surface.blit(self.b5, surface.get_rect())
                if self.is_move:
                    self.update_c(dir, 2)
                surface.blit(self.c2.image, self.c2.rect)
            else:
                surface.blit(self.background, surface.get_rect())
                surface.blit(self.c1.image, self.c1.rect)
                if self.is_move:
                    self.update_c(dir)