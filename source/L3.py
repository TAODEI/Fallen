from pygame import Surface

from source import setup


class Sruface:
    pass


class L3:
    def __init__(self):
        # 是否进入下一层
        self.next = False
        # 循环计数
        self.time_count = 0
        # 初始不透明度
        self.alpha = 0
        # 标题不透明度每次增量
        self.add_alpha = 15
        # 三个云
        self.clouds = [setup.GRAPHICS['cloud.1'],
                       setup.GRAPHICS['cloud.2'],
                       setup.GRAPHICS['cloud.3']]
        # 掉的人
        self.girl = setup.GRAPHICS['girl']
        # 背景
        self.background = setup.GRAPHICS['3_1']
        # 掉落人的高度
        self.girl_height = -setup.WINDOW_HEIGHT
        # 掉落速度
        self.fall_v = 15
        # 各阶段结束控制
        self.isOK = [False, False,False,False]
        # 云的不透明度
        self.cloud_index = 0
        self.cloud_alpha = 255
        self.add_cloud_alpha = -8

    def update(self, surface: Surface, keys, dir) -> object:
        self.time_count += 1
        # 云和掉的人
        if not self.isOK[0]:
            if self.time_count % 7 == 0:

                self.girl_height += self.fall_v

                self.cloud_alpha += self.add_cloud_alpha
                cloud_now = self.clouds[self.cloud_index]
                cloud_next = self.clouds[(self.cloud_index+1)%3]
                cloud_now.set_alpha(int(self.alpha * self.cloud_alpha/255))
                cloud_next.set_alpha(int(self.alpha * (1-self.cloud_alpha/255)))

                self.background.set_alpha(self.alpha * 2)
                self.alpha += self.add_alpha
                if self.alpha > 255:
                    self.add_alpha = 0

                surface.blit(self.background, surface.get_rect())
                surface.blit(self.girl, (0, self.girl_height, surface.get_rect().width, surface.get_rect().height))
                surface.blit(cloud_next, surface.get_rect())
                surface.blit(cloud_now, surface.get_rect())

                if self.girl_height > setup.WINDOW_HEIGHT :
                    self.isOK[0] = True
                    self.time_count = 0
                if self.time_count > 1000:
                    self.time_count = 0
                if self.cloud_alpha < 0 :
                    self.cloud_alpha =255
                    self.cloud_index = (self.cloud_index+1)%3

        # 缩放图像到指定位置
        elif not self.isOK[1]:
            self.time_count += 1
            if self.time_count % 7 == 0:

                self.background = setup.GRAPHICS['3_2']
                cloud_now = self.clouds[self.cloud_index]
                cloud_next = self.clouds[(self.cloud_index + 1) % 3]
                cloud_now.set_alpha(int(self.alpha * self.cloud_alpha / 255))
                cloud_next.set_alpha(int(self.alpha * (1 - self.cloud_alpha / 255)))

                surface.blit(self.background, surface.get_rect())
                surface.blit(cloud_next, surface.get_rect())
                surface.blit(cloud_now, surface.get_rect())

                if self.cloud_alpha < 0:
                    self.cloud_alpha = 255
                    self.cloud_index = (self.cloud_index + 1) % 3
                self.cloud_alpha += self.add_cloud_alpha
                if self.time_count > 500:
                    self.time_count = 0
                    self.isOK[1] = True
        # 变为指定图像
        elif not self.isOK[2]:
            if self.time_count > 700:
                self.time_count = 0
                self.isOK[2] = True
                self.background = setup.GRAPHICS['3_3']
                surface.blit(self.background, surface.get_rect())
        # 变为好几个人
        elif not self.isOK[3]:
            if self.time_count > 300:
                self.time_count = 0
                self.isOK[3] = True
                self.background = setup.GRAPHICS['3_4']
                surface.blit(self.background, surface.get_rect())
        elif not self.isOK[4]:
            pass

        return None
