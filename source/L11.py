from pygame import Surface

from source import setup


class L11:
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
        self.background = setup.GRAPHICS['11.1']
        # 掉落人的高度
        self.girl_height = -setup.WINDOW_HEIGHT
        # 掉落速度
        self.fall_v = 15
        # 各阶段结束控制
        self.isOK = [False, False, False, False, False,
                     False, False, False, False, False,
                     False, False, False, False, False,
                     False, False, False, False, False]
        # 云的不透明度
        self.cloud_index = 0
        self.boy_left = 4.1 / 31 * setup.WINDOW_WIDTH
        self.cloud_alpha = 255
        self.add_cloud_alpha = -8
        self.pos = 200
        self.boy = setup.GRAPHICS['3_5']
        self.buttondown = False
        self.oldx = 10000
        self.v = -5

    def update(self, surface: Surface, keys, dic) -> object:
        self.time_count += 1
        # 云和掉的人
        if not self.isOK[0]:
            if self.time_count % 7 == 0:

                self.girl_height += self.fall_v
                self.hand = setup.GRAPHICS['11.12']
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

                self.background = setup.GRAPHICS['11.2']
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
                    self.background = setup.GRAPHICS['11.13']
                    self.isOK[1] = True

        # 变为指定图像 + 伸手
        elif not self.isOK[2]:
            if self.time_count % 7 == 0:
                self.pos += self.v

                if self.pos < 0:
                    self.pos = 0
                    self.time_count = 0
                    self.isOK[2] = True
                    self.background = setup.GRAPHICS['11.4']
                surface.blit(self.background, surface.get_rect())
                surface.blit(self.hand, (self.pos, 0))
        # 点击打手
        elif not self.isOK[3]:
            left = 4.9 / 31 * setup.WINDOW_WIDTH
            right = 17.6 / 31 * setup.WINDOW_WIDTH
            top = 9.1 / 41.5 * setup.WINDOW_HEIGHT
            bottom = 31.9 / 41.5 * setup.WINDOW_HEIGHT
            if 'down' in dic and left < dic['x'] < right and top < dic['y'] < bottom:
                self.time_count = 0
                self.isOK[3] = True
                self.background = setup.GRAPHICS['11.5']
            surface.blit(self.background, surface.get_rect())
        # 干饭
        elif not self.isOK[17]:
            if self.time_count > 150:
                self.isOK[17] = True
                self.background = setup.GRAPHICS['11.6']

        elif not self.isOK[4]:
            left = 10.8 / 31 * setup.WINDOW_WIDTH
            right = 21.5 / 31 * setup.WINDOW_WIDTH
            top = 28.5 / 41.5 * setup.WINDOW_HEIGHT
            bottom = 35.5 / 41.5 * setup.WINDOW_HEIGHT
            if 'down' in dic and left < dic['x'] < right and bottom > dic['y'] > top:
                    self.isOK[4] = True
                    self.background = setup.GRAPHICS['11.7']
                    self.time_count = 0

            surface.blit(self.background, surface.get_rect())
        # 变身
        elif not self.isOK[5]:
            if 'down' in dic:
                left = 10.8 / 31 * setup.WINDOW_WIDTH
                right = 21.5 / 31 * setup.WINDOW_WIDTH
                top = 28.5 / 41.5 * setup.WINDOW_HEIGHT
                bottom = 35.5 / 41.5 * setup.WINDOW_HEIGHT
                if 'down' in dic and left < dic['x'] < right and bottom > dic['y'] > top:
                    self.isOK[5] = True
                    self.background = setup.GRAPHICS['11.8']
                    self.time_count = 0
            surface.blit(self.background, surface.get_rect())
        # 倒了
        elif not self.isOK[6]:
            surface.blit(self.background, surface.get_rect())
            if 'down' in dic:
                self.time_count = 0
                self.isOK[6] = True
                self.background = setup.GRAPHICS['11.9']
        elif not self.isOK[7]:
            surface.blit(self.background, surface.get_rect())
            if 'down' in dic:
                self.time_count = 0
                self.isOK[7] = True
                self.background = setup.GRAPHICS['11.10']
        elif not self.isOK[8]:
            surface.blit(self.background, surface.get_rect())
            if 'down' in dic:
                self.time_count = 0
                self.isOK[8] = True
                self.background = setup.GRAPHICS['11.11']
        elif not self.isOK[9]:
            surface.blit(self.background, surface.get_rect())
            if 'down' in dic:
                self.time_count = 0
                self.isOK[9] = True
                self.background = setup.GRAPHICS['11.14']
        elif not self.isOK[9]:
            surface.blit(self.background, surface.get_rect())
            if 'down' in dic:
                self.time_count = 0
                self.isOK[9] = True
                self.background = setup.GRAPHICS['11.15']
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[10]:
            if self.time_count > 150:
                self.time_count = 0
                self.isOK[10] = True
                self.background = setup.GRAPHICS['11.16']
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[11]:
            if self.time_count > 150:
                self.time_count = 0
                self.isOK[11] = True
                self.background = setup.GRAPHICS['11.17']
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[12]:
            if self.time_count > 150:
                self.time_count = 0
                self.isOK[12] = True
                self.background = setup.GRAPHICS['11.18']
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[13]:
            if self.time_count > 150:
                self.time_count = 0
                self.isOK[13] = True
                self.background = setup.GRAPHICS['11.19']
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[14]:
            if self.time_count > 150:
                self.time_count = 0
                self.isOK[14] = True
                self.background = setup.GRAPHICS['11.20']
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[15]:
            if 'down' in dic:
                left = 3.75 / 31 * setup.WINDOW_WIDTH
                right = 5.1 / 31 * setup.WINDOW_WIDTH
                top = 35.3 / 41.5 * setup.WINDOW_HEIGHT
                bottom = 41.56 / 41.5 * setup.WINDOW_HEIGHT
                if 'down' in dic and left < dic['x'] < right and bottom > dic['y'] > top:
                    self.isOK[15] = True
                    self.background = setup.GRAPHICS['11.21']
                    self.time_count = 0
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[16]:
            if self.time_count > 150:
                self.time_count = 0
                self.isOK[16] = True
                self.background = setup.GRAPHICS['11.22']
            surface.blit(self.background, surface.get_rect())
        else:
            if self.time_count > 150:
                self.time_count = 0
                surface.blit(setup.GRAPHICS['black'], surface.get_rect())
                self.next = True
            surface.blit(self.background, surface.get_rect())

        return self.next
