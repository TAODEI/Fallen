from pygame import Surface

from source import setup


class Sruface:
    pass


class L6:
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
        self.background = setup.GRAPHICS['6.1']
        # 掉落人的高度
        self.girl_height = -setup.WINDOW_HEIGHT
        # 掉落速度
        self.fall_v = 15
        # 各阶段结束控制
        self.isOK = [False, False, False, False, False, False, False, False, False, False, False, False]
        # 云的不透明度
        self.cloud_index = 0
        self.boy_left = 4.1 / 31 * setup.WINDOW_WIDTH
        self.cloud_alpha = 255
        self.add_cloud_alpha = -8
        self.boy_pos = self.boy_left
        self.boy = setup.GRAPHICS['3_5']
        self.buttondown = False
        self.oldx = 10000


    def update(self, surface: Surface, keys, dic) -> object:
        self.time_count += 1
        # 云和掉的人
        if not self.isOK[0]:
            if self.time_count % 7 == 0:

                self.girl_height += self.fall_v

                self.cloud_alpha += self.add_cloud_alpha
                cloud_now = self.clouds[self.cloud_index]
                cloud_next = self.clouds[(self.cloud_index + 1) % 3]
                cloud_now.set_alpha(int(self.alpha * self.cloud_alpha / 255))
                cloud_next.set_alpha(int(self.alpha * (1 - self.cloud_alpha / 255)))

                self.background.set_alpha(self.alpha * 2)
                self.alpha += self.add_alpha
                if self.alpha > 255:
                    self.add_alpha = 0

                surface.blit(self.background, surface.get_rect())
                surface.blit(self.girl, (0, self.girl_height, surface.get_rect().width, surface.get_rect().height))
                surface.blit(cloud_next, surface.get_rect())
                surface.blit(cloud_now, surface.get_rect())

                if self.girl_height > setup.WINDOW_HEIGHT * 0.6:
                    self.isOK[0] = True
                    self.time_count = 0
                if self.time_count > 1000:
                    self.time_count = 0
                if self.cloud_alpha < 0:
                    self.cloud_alpha = 255
                    self.cloud_index = (self.cloud_index + 1) % 3

        # 缩放图像到指定位置
        elif not self.isOK[1]:
            self.time_count += 1
            if self.time_count % 7 == 0:

                self.background = setup.GRAPHICS['6.2']
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
                if self.time_count > 200:
                    self.time_count = 0
                    self.isOK[1] = True
        # 变为指定图像
        elif not self.isOK[2]:
            if self.time_count > 200:
                self.time_count = 0
                self.isOK[2] = True
                self.background = setup.GRAPHICS['3_4']
                surface.blit(self.background, surface.get_rect())
                surface.blit(self.boy, (self.boy_left, 0))
        # 消失两个人
        elif not self.isOK[3]:
            if self.time_count > 200 and 'down' in dic:
                self.time_count = 0
                self.isOK[3] = True
                self.background = setup.GRAPHICS['6.4']
                surface.blit(self.background, surface.get_rect())
                surface.blit(self.boy, (self.boy_left, 0))
        # 小男孩推出战场
        elif not self.isOK[4]:
            left = 5.2 / 31 * setup.WINDOW_WIDTH
            right = 9.7 / 31 * setup.WINDOW_WIDTH
            top = 14.3 / 41.5 * setup.WINDOW_HEIGHT
            bottom = 27.2 / 41.5 * setup.WINDOW_HEIGHT
            target = setup.WINDOW_WIDTH
            if 'down' in dic and self.boy_pos + left < dic['x'] < right + self.boy_pos and bottom > dic['y'] > top:
                self.buttondown = True
                self.oldx = dic['x']
            if 'up' in dic:
                self.buttondown = False
            if self.buttondown:
                if 'motion' in dic and dic['x2'] > self.oldx:
                    self.boy_pos += (dic['x2'] - self.oldx) * 2
                    self.oldx = dic['x2']
            if self.boy_pos > target:
                self.boy_pos = target
                self.isOK[4] = True
                self.background = setup.GRAPHICS['6.5']
                self.time_count = 0

            surface.blit(self.background, surface.get_rect())
            surface.blit(self.boy, (self.boy_pos, 0, surface.get_rect().width, surface.get_rect().height))
        elif not self.isOK[5]:
            surface.blit(self.background, surface.get_rect())
            if self.time_count > 200:
                self.time_count = 0
                self.isOK[5] = True
                self.background = setup.GRAPHICS['6.6']
        elif not self.isOK[6]:
            surface.blit(self.background, surface.get_rect())
            if self.time_count > 200:
                self.time_count = 0
                self.isOK[6] = True
                self.background = setup.GRAPHICS['6.7']
        elif not self.isOK[7]:
            surface.blit(self.background, surface.get_rect())
            if self.time_count > 200:
                self.time_count = 0
                self.isOK[7] = True
                self.background = setup.GRAPHICS['6.8']
        elif not self.isOK[8]:
            surface.blit(self.background, surface.get_rect())
            if self.time_count > 200:
                self.time_count = 0
                self.isOK[8] = True
                self.background = setup.GRAPHICS['6.9']
        elif not self.isOK[9]:
            surface.blit(self.background, surface.get_rect())
            if self.time_count > 200:
                self.time_count = 0
                self.isOK[9] = True
                self.background = setup.GRAPHICS['3.11']
        elif not self.isOK[10]:
            surface.blit(self.background, surface.get_rect())
            if self.time_count > 200:
                self.time_count = 0
                self.next = True
                self.isOK[10] = True

        return self.next
