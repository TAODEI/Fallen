import pygame
import time
from . import tools, setup
from pygame.surface import Surface


class L1:
    def __init__(self):
        self.setup_background()
        self.next = 'load_screen'
        self.finished = False


    def setup_background(self):
        # 初始的背景图
        self.picture = setup.GRAPHICS['1.7']
        self.picture = pygame.transform.scale(self.picture, (int(1536 / 3), int(2048 / 3)))
        # 女孩落下的背景图
        self.Picture2 = setup.GRAPHICS['1.8']
        self.Picture2 = pygame.transform.scale(self.Picture2, (int(1536 / 3), int(2048 / 3)))
        # 女孩的图片
        self.Girl = setup.GRAPHICS['girl']
        # 三组云的图片
        self.clouds = [setup.GRAPHICS['cloud.1'],
                       setup.GRAPHICS['cloud.2'],
                       setup.GRAPHICS['cloud.3']]
        # 大人抓住小孩的手的画面
        self.Picture3 = setup.GRAPHICS['17']
        self.Picture3 = pygame.transform.scale(self.Picture3, (int(1536 / 3), int(2048 / 3)))
        # self.Girl = pygame.transform.scale(self.Girl,(100,200))
        self.Girl_height = 0
        self.Girl_x = 0
        # 初始的比较时间
        self.timer = 0
        # self.location = setup.surface.get_rect()
        self.speed = 2
        self.alpha = 0
        # 云的不透明度
        self.cloud_index = 0
        self.cloud_alpha = 255
        self.add_cloud_alpha = -8
        self.add_alpha = 15
        # 云的计数令牌
        self.count = 0
        # 手开始画画的背景
        self.HandBack = setup.GRAPHICS['18']
        self.Picture2 = pygame.transform.scale(self.Picture2, (int(1536 / 3), int(2048 / 3)))
        # 一个可以移动的手的画面
        self.Hand = setup.GRAPHICS['1.10']
        # self.Hand = pygame.transform.scale(self.Hand,(200,400))
        self.Hand_y = 400
        self.Hand_x = 120
        # 手的移动速度
        self.Hand_speed = 3
        # 判断while监听进行的标志
        self.is_move = False
        self.old_x = 0
        self.old_y = 0
        self.new_x = 0
        self.old_y = 0
        self.Paper = setup.GRAPHICS['1.4']
        # 画笔
        self.Hand2 = setup.GRAPHICS['1.5']
        self.Hand2_x = 0
        self.Hand2_y = 0
        self.old1_x = 0
        self.old1_y = 0
        self.new1_x = 0
        self.new1_y = 0

        # four picture
        self.Picture_1 = setup.GRAPHICS['1.0']
        # self.Picture_2 = setup.GRAPHICS['1.1']
        self.Picture_3 = setup.GRAPHICS['1.2']
        self.Picture_4 = setup.GRAPHICS['1.3']
        self.num = 0

        self.inited = False
        self.flag = False

    def update(self, surface: Surface, keys, dir):
        if not self.inited:
            self.timer = pygame.time.get_ticks()
            self.inited = True

        if pygame.time.get_ticks() - self.timer < 2000:
            surface.blit(self.picture, surface.get_rect())
        if pygame.time.get_ticks() - self.timer >= 2000 and pygame.time.get_ticks() - self.timer <= 4500:
            # self.cloud_alpha += self.add_cloud_alpha
            cloud_now = self.clouds[self.cloud_index % 3]
            cloud_next = self.clouds[(self.cloud_index + 1) % 3]
            # cloud_now.set_alpha(int(self.cloud_alpha/255)                cloud_next.set_alpha(int(self.alpha * (1-self.cloud_alpha/255)))
            # self.background.set_alpha(self.alpha * 2)
            # self.alpha += self.add_alpha
            # if self.alpha > 255:
            #    self.add_alpha = 0
            surface.blit(self.picture, surface.get_rect())
            surface.blit(self.Girl, (0, self.Girl_height, surface.get_rect().width, surface.get_rect().height))
            # print(self.Girl_height)
            surface.blit(cloud_now, surface.get_rect())
            surface.blit(cloud_next, surface.get_rect())
            self.Girl_height += self.speed
            self.count += 1
            if self.count % 50 == 0:
                self.cloud_index += 1

        if pygame.time.get_ticks() - self.timer > 4000 and pygame.time.get_ticks() - self.timer < 6000:
            cloud_now = self.clouds[self.cloud_index % 3]
            cloud_next = self.clouds[(self.cloud_index + 1) % 3]
            surface.blit(self.Picture2, surface.get_rect())
            surface.blit(cloud_now, surface.get_rect())
            surface.blit(cloud_next, surface.get_rect())
            self.count += 1
            # 关于云的变换的计数
            if self.count % 50 == 0:
                self.cloud_index += 1

        # 大人抓住小孩手的画面
        # if pygame.time.get_ticks() - self.timer > 6000 and pygame.time.get_ticks() - self.timer <= 8000:
        #    surface.blit(self.Picture3,surface.get_rect())
        # 手移动的画面
        # if pygame.time.get_ticks() - self.timer >= 6000 and pygame.time.get_ticks() - self.timer <= 8000:
        #    surface.blit(self.HandBack,surface.get_rect())
        # print(self.Hand_y)

        #    self.Hand_y -= self.Hand_speed
        if pygame.time.get_ticks() - self.timer >= 6000:
            surface.blit(self.HandBack, surface.get_rect())
            surface.blit(self.Hand, (self.Hand_x, self.Hand_y))
            if 'down' in dir:
                self.is_move = True
                self.old_x = dir['x']
                self.old_y = dir['y']
            if 'up' in dir:
                self.is_move = False
            if self.is_move == True:
                self.new_x = dir['x2']
                self.new_y = dir['y2']
                self.Hand_x += (self.new_x - self.old_x)
                self.Hand_y += (self.new_y - self.old_y)
                # print(self.old_y)
                # print(self.new_y)
                # print(self.new_x - self.old_x)
                # print(self.new_y - self.old_y)
                self.old_x = self.new_x
                self.old_y = self.new_y
            surface.blit(self.Hand, (self.Hand_x, self.Hand_y))
            if (self.Hand_x <= 100 and self.Hand_y <= 100):
                self.flag = True

        if self.flag:
            surface.blit(self.Paper, surface.get_rect())
            surface.blit(self.Hand2, (self.Hand2_x, self.Hand2_y))
            if 'down' in dir:
                self.is_move = True
                self.old1_x = dir['x']
                self.old1_y = dir['y']
            if 'up' in dir:
                self.is_move = False
            if self.is_move == True:
                self.new1_x = dir['x2']
                self.new1_y = dir['y2']
                self.Hand2_x += (self.new1_x - self.old1_x)
                self.Hand2_y += (self.new1_y - self.old1_y)
                if abs(self.new1_x - self.old1_x) > 100:
                    self.num += 1
                self.old1_x = self.new1_x
                self.old1_y = self.new1_y
            if self.num == 0:
                surface.blit(self.Paper, surface.get_rect())
                surface.blit(self.Hand2, (self.Hand2_x, self.Hand2_y))
            if self.num == 1:
                surface.blit(self.Picture_1, surface.get_rect())
                surface.blit(self.Hand2, (self.Hand2_x, self.Hand2_y))
                # if self.num == 2:
                #    surface.blit(self.Picture_2, surface.get_rect())
                #    surface.blit(self.Hand2,(self.Hand2_x,self.Hand2_y))
            if self.num == 2:
                surface.blit(self.Picture_3, surface.get_rect())
                surface.blit(self.Hand2, (self.Hand2_x, self.Hand2_y))
            if self.num >= 3:
                surface.blit(self.Picture_4, surface.get_rect())
                surface.blit(self.Hand2, (self.Hand2_x, self.Hand2_y))
                return True
