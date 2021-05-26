import pygame
from pygame import Surface

from source import setup


class Sruface:
    pass


class Last:
    def __init__(self):
        # 是否进入下一层
        self.next = False
        # 各阶段结束控制
        self.isOK = [False, False, False, False,  False, False, False, False, False, False, False]
        self.v = 8
        self.add = self.v
        self.alpha = 0
        self.count = 0
        self.stay = 100
        self.background = setup.GRAPHICS['15.1']
        self.clock = pygame.time.Clock()
        self.pos = 0
        self.drop = 5

    def update(self, surface: Surface, keys, dic) -> object:
        self.clock.tick(30)
        self.count += 1
        if not self.isOK[0]:
            surface.blit(self.background, surface.get_rect())
            if self.count > self.stay:
                self.isOK[0] = True
                self.count = 0
                self.background = setup.GRAPHICS['15.2']
        elif not self.isOK[1]:

            if self.alpha < 250:
                self.alpha += self.add
                self.count = 0
            elif self.count > self.stay:
                self.add = -self.v
                self.alpha += self.add

            if self.add == -self.v and self.alpha <= 0:
                self.add = self.v
                self.count = 0
                self.isOK[1] = True
                self.background = setup.GRAPHICS['15.3']

            self.background.set_alpha(self.alpha)
            surface.blit(setup.GRAPHICS['black'], surface.get_rect())
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[2]:

            if self.alpha < 250:
                self.alpha += self.add
                self.count = 0
            elif self.count > self.stay:
                self.add = -self.v
                self.alpha += self.add

            if self.add == -self.v and self.alpha <= 0:
                self.add = self.v
                self.count = 0
                self.isOK[2] = True
                self.background = setup.GRAPHICS['15.4']

            self.background.set_alpha(self.alpha)
            surface.blit(setup.GRAPHICS['black'], surface.get_rect())
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[3]:

            if self.alpha < 250:
                self.alpha += self.add
                self.count = 0
            elif self.count > self.stay:
                self.add = -self.v
                self.alpha += self.add

            if self.add == -self.v and self.alpha <= 0:
                self.add = self.v
                self.count = 0
                self.isOK[3] = True
                self.background = setup.GRAPHICS['15.5']

            self.background.set_alpha(self.alpha)
            surface.blit(setup.GRAPHICS['black'], surface.get_rect())
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[4]:

            if self.alpha < 250:
                self.alpha += self.add
                self.count = 0
            elif self.count > self.stay:
                self.add = -self.v
                self.alpha += self.add

            if self.add == -self.v and self.alpha <= 0:
                self.add = self.v
                self.count = 0
                self.isOK[4] = True
                self.background = setup.GRAPHICS['15.6']

            self.background.set_alpha(self.alpha)
            surface.blit(setup.GRAPHICS['black'], surface.get_rect())
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[5]:

            if self.alpha < 250:
                self.alpha += self.add
                self.count = 0
            elif self.count > self.stay:
                self.add = -self.v
                self.alpha += self.add

            if self.add == -self.v and self.alpha <= 0:
                self.add = self.v
                self.count = 0
                self.isOK[5] = True
                self.background = setup.GRAPHICS['15.8']

            self.background.set_alpha(self.alpha)
            surface.blit(setup.GRAPHICS['black'], surface.get_rect())
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[6]:

            if self.alpha < 250:
                self.alpha += self.add
                self.count = 0
            elif self.count > self.stay * 2:
                self.add = -self.v
                self.alpha += self.add

            if self.add == -self.v and self.alpha <= 0:
                self.add = self.v
                self.count = 0
                self.isOK[6] = True
                self.background = setup.GRAPHICS['15.9']

            self.background.set_alpha(self.alpha)
            surface.blit(setup.GRAPHICS['black'], surface.get_rect())
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[7]:

            if self.alpha < 250:
                self.alpha += self.add
                self.count = 0

            self.background.set_alpha(self.alpha)
            surface.blit(setup.GRAPHICS['black'], surface.get_rect())
            surface.blit(self.background, surface.get_rect())
        return False
