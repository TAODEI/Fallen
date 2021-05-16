from .import setup
import pygame, time

class L12:
    def __init__(self):
        self.ok = True
        self.state = 0
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
        self.b17 = setup.GRAPHICS['12.17']
        self.b18 = setup.GRAPHICS['12.18']
        self.b19 = setup.GRAPHICS['12.19']
        self.b20 = setup.GRAPHICS['12.20']
        self.b21 = setup.GRAPHICS['12.21']
        self.b22 = setup.GRAPHICS['12.22']
        self.b23 = setup.GRAPHICS['12.23']
        self.b24 = setup.GRAPHICS['12.24']
        self.b25 = setup.GRAPHICS['12.25']
        self.b26 = setup.GRAPHICS['12.26']
        self.b27 = setup.GRAPHICS['12.27']
        self.b28 = setup.GRAPHICS['12.28']
        self.b29 = setup.GRAPHICS['12.29']
        self.b30 = setup.GRAPHICS['12.30']
        self.b31 = setup.GRAPHICS['12.31']
        self.b32 = setup.GRAPHICS['12.32']
        self.b33 = setup.GRAPHICS['12.33']
        self.b34 = setup.GRAPHICS['12.34']

        self.a1 = setup.GRAPHICS['13.1']
        self.a2 = setup.GRAPHICS['13.2']
        self.a3 = setup.GRAPHICS['13.3']
        self.a4 = setup.GRAPHICS['13.4']
        self.a5 = setup.GRAPHICS['13.5']
        self.a6 = setup.GRAPHICS['13.6']
        self.a7 = setup.GRAPHICS['13.7']
        self.a8 = setup.GRAPHICS['13.8']
        self.a9 = setup.GRAPHICS['13.9']
        self.a10 = setup.GRAPHICS['13.10']
        self.a11 = setup.GRAPHICS['13.11']
        self.a12 = setup.GRAPHICS['13.12']

        self.c1 = setup.GRAPHICS['14.1']
        self.c2 = setup.GRAPHICS['14.2']
        self.c3 = setup.GRAPHICS['14.3']
        self.c4 = setup.GRAPHICS['14.4']
        self.c5 = setup.GRAPHICS['14.5']
        self.c6 = setup.GRAPHICS['14.6']
        self.c7 = setup.GRAPHICS['14.7']
        self.c8 = setup.GRAPHICS['14.8']

        self.timer = 0
        self.ok = True
        self.choice = 0
    def update(self, surface, keys, dir):
     #   print(self.state)
        if self.state == 0:
            surface.blit(self.background, surface.get_rect())
        if 'down' in dir and self.ok:
            print(dir['x'], dir['y'])

            if 220 > dir['x'] > 160 and 600 > dir['y'] > 530 and self.state >= 27:
                self.choice = 1
                self.timer = pygame.time.get_ticks()
            if 360 > dir['x'] > 300 and 600 > dir['y'] > 530 and self.state >= 27:
                self.choice = 2
                self.timer = pygame.time.get_ticks()
            if not(40 < dir['x'] < 260 and 480 > dir['y'] > 330) and self.state == 3:
                return
            if not(480 > dir['x'] > 240 and 500 > dir['y'] > 220) and self.state == 8:
                return
            if self.choice != 0:
                print(self.choice)
            self.state += 1
        if self.state == 1:
            surface.blit(self.b1, surface.get_rect())
        elif self.state == 2:
            surface.blit(self.b2, surface.get_rect())
        elif self.state == 3:
            surface.blit(self.b3, surface.get_rect())
        elif self.state == 4:
            surface.blit(self.b32, surface.get_rect())
        elif self.state == 5:
            surface.blit(self.b33, surface.get_rect())
        elif self.state == 6:
            self.timer = pygame.time.get_ticks()
            surface.blit(self.b34, surface.get_rect())
        elif pygame.time.get_ticks() - self.timer < 2000 and self.timer and self.state == 7:
            self.ok = False
            surface.blit(self.b4, surface.get_rect())
        elif 2000 < pygame.time.get_ticks() - self.timer < 4000 and self.timer and self.state == 7:
            surface.blit(self.b5, surface.get_rect())
        elif 4000 < pygame.time.get_ticks() - self.timer < 6000 and self.timer and self.state == 7:
            surface.blit(self.b6, surface.get_rect())
        elif self.state == 7:
            surface.blit(self.b7, surface.get_rect())
            self.ok = True
        elif self.state == 8:
            self.timer = pygame.time.get_ticks()
            surface.blit(self.b8, surface.get_rect())
        elif pygame.time.get_ticks() - self.timer < 2000 and self.state == 9:
            self.ok = False
            surface.blit(self.b9, surface.get_rect())
        elif 2000 < pygame.time.get_ticks() - self.timer < 4000 and self.state == 9:
            surface.blit(self.b10, surface.get_rect())
        elif 4000 < pygame.time.get_ticks() - self.timer < 6000 and self.state == 9:
            surface.blit(self.b11, surface.get_rect())
        elif 6000 < pygame.time.get_ticks() - self.timer < 8000 and self.state == 9:
            surface.blit(self.b12, surface.get_rect())
        elif self.state == 9:
            surface.blit(self.b13, surface.get_rect())
            self.ok = True
        elif self.state == 10:
            surface.blit(self.b14, surface.get_rect())
        elif self.state == 11:
            surface.blit(self.b15, surface.get_rect())
        elif self.state == 12:
            surface.blit(self.b16, surface.get_rect())
        elif self.state == 13:
            surface.blit(self.b17, surface.get_rect())
        elif self.state == 14:
            surface.blit(self.b18, surface.get_rect())
        elif self.state == 15:
            surface.blit(self.b19, surface.get_rect())
        elif self.state == 16:
            surface.blit(self.b20, surface.get_rect())
        elif self.state == 17:
            surface.blit(self.b21, surface.get_rect())
        elif self.state == 18:
            surface.blit(self.b22, surface.get_rect())
        elif self.state == 19:
            surface.blit(self.b23, surface.get_rect())
        elif self.state == 20:
            surface.blit(self.b24, surface.get_rect())
        elif self.state == 21:
            surface.blit(self.b25, surface.get_rect())
        elif self.state == 22:
            surface.blit(self.b26, surface.get_rect())
        elif self.state == 23:
            surface.blit(self.b27, surface.get_rect())
        elif self.state == 24:
            surface.blit(self.b28, surface.get_rect())
        elif self.state == 25:
            surface.blit(self.b29, surface.get_rect())
        elif self.state == 26:
            surface.blit(self.b30, surface.get_rect())
        elif self.state == 27:
            surface.blit(self.b31, surface.get_rect())
        # 好
        if self.state >= 27 and self.choice == 2:
            if pygame.time.get_ticks() - self.timer < 2000:
                surface.blit(self.a1, surface.get_rect())
            elif 2000 < pygame.time.get_ticks() - self.timer < 4000:
                surface.blit(self.a2, surface.get_rect())
            elif 4000 < pygame.time.get_ticks() - self.timer < 6000:
                surface.blit(self.a3, surface.get_rect())
            elif 6000 < pygame.time.get_ticks() - self.timer < 8000:
                surface.blit(self.a4, surface.get_rect())
            elif 8000 < pygame.time.get_ticks() - self.timer < 10000:
                surface.blit(self.a5, surface.get_rect())
            elif 10000 < pygame.time.get_ticks() - self.timer < 12000:
                surface.blit(self.a6, surface.get_rect())
            elif 12000 < pygame.time.get_ticks() - self.timer < 14000:
                surface.blit(self.a7, surface.get_rect())
            elif 14000 < pygame.time.get_ticks() - self.timer < 16000:
                surface.blit(self.a8, surface.get_rect())
            elif 16000 < pygame.time.get_ticks() - self.timer < 18000:
                surface.blit(self.a9, surface.get_rect())
            elif 18000 < pygame.time.get_ticks() - self.timer < 20000:
                surface.blit(self.a10, surface.get_rect())
            elif 20000 < pygame.time.get_ticks() - self.timer < 22000:
                surface.blit(self.a11, surface.get_rect())
            elif 22000 < pygame.time.get_ticks() - self.timer < 24000:
                surface.blit(self.a12, surface.get_rect())
        # 坏
        if self.state >= 27 and self.choice == 1:
            if pygame.time.get_ticks() - self.timer < 2000:
                surface.blit(self.c1, surface.get_rect())
            elif 2000 < pygame.time.get_ticks() - self.timer < 4000:
                surface.blit(self.c2, surface.get_rect())
            elif 4000 < pygame.time.get_ticks() - self.timer < 6000:
                surface.blit(self.c3, surface.get_rect())
            elif 6000 < pygame.time.get_ticks() - self.timer < 8000:
                surface.blit(self.c4, surface.get_rect())
            elif 8000 < pygame.time.get_ticks() - self.timer < 10000:
                surface.blit(self.c5, surface.get_rect())
            elif 10000 < pygame.time.get_ticks() - self.timer < 12000:
                surface.blit(self.c6, surface.get_rect())
            elif 12000 < pygame.time.get_ticks() - self.timer < 14000:
                surface.blit(self.c7, surface.get_rect())
            elif 14000 < pygame.time.get_ticks() - self.timer < 16000:
                surface.blit(self.c8, surface.get_rect())
            
            
