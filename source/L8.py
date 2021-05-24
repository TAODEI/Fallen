import pygame
import time

from pygame.pixelcopy import surface_to_array
from . import tools, setup
from pygame.surface import Surface


class L8:
    def __init__(self):
        self.setup_background()
        self.next = 'load_screen'
        self.finished = False

    def setup_background(self):
        # 计时器
        self.timer = 0
        # 一个黑屏的开始图片
        self.background = setup.GRAPHICS['8.0']

        # 一个显示信封的图片
        self.Litter = setup.GRAPHICS['8.1']
        # 控制点击位置的坐标
        self.x = 0
        self.y = 0
        self.flag = False
        # 显示信纸的图片
        self.Litter_paper = setup.GRAPHICS['8.2']
        # 第二次判断点击的位置
        self.x1 = 0
        self.y1 = 0
        self.flag1 = False
        self.count = 0
        # 显示破碎的信纸
        self.Litter_Bad = setup.GRAPHICS['8.3']
        # 显示女孩背影的图片
        self.Girl = setup.GRAPHICS['8.4']
        # 黑板上的三块图层
        self.Picture1 = setup.GRAPHICS['8.5']
        self.Picture2 = setup.GRAPHICS['8.6']
        self.Picture3 = setup.GRAPHICS['8.7']
        self.is_move = False
        self.new_x = 0
        self.new_y = 0
        # 计数使用
        self.num = 0
        # 8.8以后的图片
        self.Paper1 = setup.GRAPHICS['8.8']
        self.Paper2 = setup.GRAPHICS['8.9']
        self.Paper3 = setup.GRAPHICS['8.10']
        self.Paper4 = setup.GRAPHICS['8.11']
        self.Paper5 = setup.GRAPHICS['8.12']
        self.Paper6 = setup.GRAPHICS['8.13']
        self.People = setup.GRAPHICS['8.14']
        self.Message1 = setup.GRAPHICS['8.15']
        self.Message2 = setup.GRAPHICS['8.16']
        self.Message3 = setup.GRAPHICS['8.17']
        self.Message4 = setup.GRAPHICS['8.18']
        self.Message5 = setup.GRAPHICS['8.19']
        self.Message6 = setup.GRAPHICS['8.20']
        self.Message7 = setup.GRAPHICS['8.21']
        self.End = setup.GRAPHICS['8.22']

    def u(self, surface: Surface, keys, dir):
        if pygame.time.get_ticks() - self.timer <= 500:
            surface.blit(self.background, surface.get_rect())
        if pygame.time.get_ticks() - self.timer > 500:
            if self.count == 0:
                surface.blit(self.Litter, surface.get_rect())
            if self.count == 1:
                if 'down' in dir:
                    self.x = dir['x']
                    self.y = dir['y']
                # y = surface.get_rect().height
                # x = surface.get_rect().width
                if (self.x > 76 and self.x < 280 and self.y > 200 and self.y < 400):
                    self.flag = True
                    self.count += 1
                if self.flag:
                    surface.blit(self.Litter_paper, surface.get_rect())
            if self.count == 3:
                if 'down' in dir:
                    self.x1 = dir['x']
                    self.y1 = dir['y']
                if (self.x1 > 128 and self.x1 < 400 and self.y1 > 128 and self.y1 < 480):
                    self.flag1 = True
                if self.flag1:
                    surface.blit(self.Litter_Bad, surface.get_rect())

    def update(self, surface: Surface, keys, dir):
        if pygame.time.get_ticks() - self.timer <= 500:
            surface.blit(self.background, surface.get_rect())
        if pygame.time.get_ticks() - self.timer > 500:
            if 'down' in dir:
                self.x = dir['x']
                self.y = dir['y']

                if (self.count == 0 and self.x > 76 and self.x < 280 and self.y > 200 and self.y < 400):
                    self.count += 1
                elif (self.count == 1 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 2 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 3 and self.flag1 == True):
                    self.count += 1
                elif (self.count == 4 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 5 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 6 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 7 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 8 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 9 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 10 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 11 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 12 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 13 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 14 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 15 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 16 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1
                elif (self.count == 17 and self.x > 128 and self.x < 400 and self.y > 128 and self.y < 480):
                    self.count += 1

            if self.count == 0:
                surface.blit(self.Litter, surface.get_rect())
            if self.count == 1:
                surface.blit(self.Litter_paper, surface.get_rect())
            if self.count == 2:
                surface.blit(self.Litter_Bad, surface.get_rect())

            # self.timer = pygame.time.get_ticks()
            # if pygame.time.get_ticks() - self.timer > 2000 and pygame.time.get_ticks() - self.timer <= 4000:
            if self.count == 3:
                surface.blit(self.Girl, surface.get_rect())
                if 'down' in dir:
                    self.is_move = True
                    self.x1 = dir['x']
                    self.y1 = dir['y']
                if 'up' in dir:
                    self.is_move = False
                if self.is_move == True:
                    self.new_x = dir['x2']
                    self.new_y = dir['y2']
                    if abs(self.new_x - self.x) > 100:
                        self.num += 1
                    self.x = self.new_x
                    self_y = self.new_y
                if self.num == 1:
                    surface.blit(self.Picture1, surface.get_rect())
                if self.num == 2:
                    surface.blit(self.Picture2, surface.get_rect())
                if self.num == 3:
                    surface.blit(self.Picture3, surface.get_rect())
                    self.flag1 = True
            if self.count == 4:
                surface.blit(self.Paper1, surface.get_rect())
            if self.count == 5:
                surface.blit(self.Paper2, surface.get_rect())
            if self.count == 6:
                surface.blit(self.Paper3, surface.get_rect())
            if self.count == 7:
                surface.blit(self.Paper4, surface.get_rect())
            if self.count == 8:
                surface.blit(self.Paper5, surface.get_rect())
            if self.count == 9:
                surface.blit(self.Paper6, surface.get_rect())
            if self.count == 10:
                surface.blit(self.People, surface.get_rect())
            if self.count == 11:
                surface.blit(self.Message1, surface.get_rect())
            if self.count == 12:
                surface.blit(self.Message2, surface.get_rect())
            if self.count == 13:
                surface.blit(self.Message3, surface.get_rect())
            if self.count == 14:
                surface.blit(self.Message4, surface.get_rect())
            if self.count == 15:
                surface.blit(self.Message5, surface.get_rect())
            if self.count == 16:
                surface.blit(self.Message6, surface.get_rect())
            if self.count == 17:
                surface.blit(self.Message7, surface.get_rect())
            if self.count == 18:
                surface.blit(self.End, surface.get_rect())
                return True
