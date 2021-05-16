import pygame.transform
from pygame import Surface

from source import setup


class Sruface:
    pass


class L5:
    def __init__(self):
        # 是否进入下一层
        self.next = False
        # 循环计数
        self.time_count = 0
        # 各阶段结束控制
        self.isOK = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.background = setup.GRAPHICS['5.1']
        self.cloud = setup.GRAPHICS['5.2']
        self.buttondown = False
        self.oldx = -10000
        self.oldy = -10000
        self.cloud_pos = 0
        self.length = setup.WINDOW_HEIGHT * 0.65
        self.cloudsource = self.cloud

    def update(self, surface: Surface, keys, dic) -> object:
        self.time_count += 1
        # 拨开云见人
        if not self.isOK[0]:
            if 'down' in dic:
                self.buttondown = True
                self.oldx = dic['x']
                self.oldy = dic['y']
            if 'up' in dic:
                self.buttondown = False
            if self.buttondown:
                if 'motion' in dic:
                    mov = max((self.oldx - dic['x2']), (dic['y2'] - self.oldy))
                    self.cloud_pos -= mov * 2
                    self.oldx = dic['x2']
                    self.oldy = dic['y2']
            if self.cloud_pos < -setup.WINDOW_HEIGHT:
                self.isOK[0] = True
                self.time_count = 0
            self.cloud = pygame.transform.scale(self.cloudsource, (surface.get_rect().width - self.cloud_pos, surface.get_rect().height-self.cloud_pos))
            surface.blit(self.background, surface.get_rect())
            surface.blit(self.cloud,(self.cloud_pos * 2, -self.cloud_pos))
        # 人 + 1
        elif not self.isOK[1]:
            if 'down' in dic:
                self.isOK[1] = True
                self.background = setup.GRAPHICS['5.3']
                surface.blit(self.background, surface.get_rect())
                self.time_count = 0
        # 人 + 1
        elif not self.isOK[2]:
            if 'down' in dic:
                self.isOK[2] = True
                self.background = setup.GRAPHICS['5.4']
                self.cloud = setup.GRAPHICS['5.10']
                self.cloud_pos = 0
                surface.blit(self.background, surface.get_rect())
                self.time_count = 0
        # 上划
        elif not self.isOK[3]:
            if 'down' in dic:
                self.buttondown = True
                self.oldy = dic['y']
            if 'up' in dic:
                self.buttondown = False
            if self.buttondown:
                if 'motion' in dic:
                    self.cloud_pos -= dic['y2'] - self.oldy
                    self.oldy = dic['y2']
            if self.length - self.cloud_pos < 0:
                self.isOK[3] = True
                self.time_count = 0

            surface.blit(self.cloud,
                         (0, self.length - self.cloud_pos, surface.get_rect().width, surface.get_rect().height))
            surface.blit(self.background, (0, -self.cloud_pos, surface.get_rect().width, surface.get_rect().height))

        # 拍手
        elif not self.isOK[4]:
            left = 5.2 / 13.72 * setup.WINDOW_WIDTH
            right = 8.3 / 13.72 * setup.WINDOW_WIDTH
            top = 14.5 / 18.29 * setup.WINDOW_HEIGHT
            if 'down' in dic and left < dic['x'] < right and top < dic['y'] < setup.WINDOW_HEIGHT:
                self.isOK[4] = True
                self.cloud = setup.GRAPHICS['5.9']
                surface.blit(self.cloud,
                             (0, self.length - self.cloud_pos, surface.get_rect().width, surface.get_rect().height))
                surface.blit(self.background, (0, -self.cloud_pos, surface.get_rect().width, surface.get_rect().height))
                self.time_count = 0
        elif not self.isOK[5]:
            left = 5.2 / 13.72 * setup.WINDOW_WIDTH
            right = 8.3 / 13.72 * setup.WINDOW_WIDTH
            top = 14.5 / 18.29 * setup.WINDOW_HEIGHT
            if 'down' in dic and left < dic['x'] < right and top < dic['y'] < setup.WINDOW_HEIGHT:
                self.isOK[5] = True
                self.cloud = setup.GRAPHICS['5.10']
                surface.blit(self.cloud,
                             (0, self.length - self.cloud_pos, surface.get_rect().width, surface.get_rect().height))
                surface.blit(self.background,
                             (0, -self.cloud_pos, surface.get_rect().width, surface.get_rect().height))
                self.time_count = 0
        elif not self.isOK[6]:
            if 'down' in dic:
                self.isOK[6] = True
                self.next = True
                self.background = setup.GRAPHICS['5.8']
                surface.blit(self.background,surface.get_rect())
                self.time_count = 0

        return self.next
