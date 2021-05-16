from . import setup
import pygame, time


class L2:
    def __init__(self):
        self.ok = True
        # 循环计数
        self.time_count = 0
        # 初始不透明度
        self.alpha = 0
        # 标题不透明度每次增量
        self.add_alpha = 8
        # 三个云
        self.clouds = [setup.GRAPHICS['cloud.1'],
                       setup.GRAPHICS['cloud.2'],
                       setup.GRAPHICS['cloud.3']]
        # 掉的人
        self.girl = setup.GRAPHICS['girl']
        # 背景
        self.background = setup.GRAPHICS['3_1']
        # 掉落人的高度
        self.girl_height = -setup.WINDOW_HEIGHT + 200
        # 掉落速度
        self.fall_v = 15
        # self.timer = pygame.
        self.state = 2
        self.background = setup.GRAPHICS['2_1']
        self.b2 = setup.GRAPHICS['2_2']
        self.b3 = setup.GRAPHICS['2_3']
        self.b4 = setup.GRAPHICS['2_4']
        self.b5 = setup.GRAPHICS['2_5']
        self.b6 = setup.GRAPHICS['2_6']
        self.b7 = setup.GRAPHICS['2_7']
        self.b8 = setup.GRAPHICS['2_8']
        self.b9 = setup.GRAPHICS['black']
        self.current_time = pygame.time.get_ticks()
        self.timer = 0

    def update_cloud_and_girl(self, surface: pygame.Surface):
        self.time_count += 1

        # 云和掉的人
        if self.time_count % 7 == 0:
            # 换云,掉人
            self.girl_height += self.fall_v
            cloud = self.clouds[int(self.time_count / 150) % 3]
            cloud.set_alpha(self.alpha)
            self.background.set_alpha(self.alpha * 2)
            self.alpha += self.add_alpha
            if self.alpha == 200:
                self.add_alpha = 0
            if self.ok:
                surface.blit(self.background, surface.get_rect())
            else:
                surface.blit(self.b2, surface.get_rect())

            surface.blit(self.girl, (0, self.girl_height, surface.get_rect().width, surface.get_rect().height))
            surface.blit(cloud, surface.get_rect())

            if self.time_count > 500:
                self.time_count = 0
            if self.girl_height > setup.WINDOW_HEIGHT * 0.6:
                self.ok = False

    def update(self, surface, keys, dir):
        if self.state < 3:
            self.update_cloud_and_girl(surface)
        if 'down' in dir and self.ok == False:
            print(self.state)

            print(dir['x'], dir['y'])

            if self.state == 2:
                surface.blit(self.b3, surface.get_rect())
                self.state += 1
            elif self.state == 3 and dir['x'] < 280 and 340 > dir['y'] > 100:
                surface.blit(self.b4, surface.get_rect())
                self.state += 1
            elif self.state == 4:
                surface.blit(self.b5, surface.get_rect())
                self.state += 1
            elif self.state == 5 and 200 > dir['x'] > 80 and 400 > dir['y'] > 200:
                surface.blit(self.b6, surface.get_rect())
                self.state += 1
            elif self.state == 6:
                surface.blit(self.b7, surface.get_rect())
                self.state += 1
                self.timer = pygame.time.get_ticks()
        if self.state == 7:
            if 4000 > pygame.time.get_ticks() - self.timer > 2000:
                surface.blit(self.b8, surface.get_rect())
            if 6000 > pygame.time.get_ticks() - self.timer > 4000:
                surface.blit(self.b9, surface.get_rect())
                return True
        return False
