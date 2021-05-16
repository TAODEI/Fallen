from pygame import Surface

from source import setup


class Sruface:
    pass


class L9:
    def __init__(self):
        # 是否进入下一层
        self.next = False
        # 循环计数
        self.time_count = 0
        # 背景
        self.background = setup.GRAPHICS['9.1']
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
        self.pos = setup.WINDOW_HEIGHT
        self.step = -5
        self.boy = setup.GRAPHICS['3_5']
        self.buttondown = False
        self.oldx = 10000


    def update(self, surface: Surface, keys, dic) -> object:
        self.time_count += 1
        # 云和掉的人
        if not self.isOK[0]:
            if 'down' in dic:
                self.time_count = 0
                self.isOK[0] = True
                self.background = setup.GRAPHICS['9.2']
            surface.blit(self.background, surface.get_rect())

        elif not self.isOK[1]:
            if 'down' in dic:
                self.time_count = 0
                self.isOK[1] = True
                self.background = setup.GRAPHICS['9.3']
            surface.blit(self.background, surface.get_rect())
        # 变为指定图像
        elif not self.isOK[2]:
            if 'down' in dic:
                self.time_count = 0
                self.isOK[2] = True
                self.background = setup.GRAPHICS['9.4']
            surface.blit(self.background, surface.get_rect())
        # 消失两个人
        elif not self.isOK[3]:
            if 'down' in dic:
                self.time_count = 0
                self.isOK[3] = True
                self.background = setup.GRAPHICS['9.5']
            surface.blit(self.background, surface.get_rect())
        # 小男孩推出战场
        elif not self.isOK[4]:
            if 'down' in dic:
                self.time_count = 0
                self.isOK[4] = True
                self.background = setup.GRAPHICS['9.6']
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[5]:
            if 'down' in dic:
                self.time_count = 0
                self.isOK[5] = True
                self.background = setup.GRAPHICS['9.7']
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[6]:
            if 'down' in dic:
                self.time_count = 0
                self.isOK[6] = True
                self.background = setup.GRAPHICS['9.8']
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[7]:
            if 'down' in dic:
                self.time_count = 0
                self.isOK[7] = True
                self.background = setup.GRAPHICS['black']
            surface.blit(self.background, surface.get_rect())
        elif not self.isOK[8]:
            self.background = setup.GRAPHICS['9.10']
            self.boy = setup.GRAPHICS['9.11']
            if self.time_count > 200:
               self.pos += self.step
            surface.blit(self.background,(0,self.pos-setup.WINDOW_HEIGHT))
            surface.blit(self.boy,(0,self.pos))
            if self.pos <=0:
                self.step = 0
                if self.time_count >500:
                    self.background = setup.GRAPHICS['black']
                    self.isOK[8]= True
                    self.time_count = 0
        elif not self.isOK[9]:
            surface.blit(self.background, surface.get_rect())
            if self.time_count > 500:
                self.time_count = 0
                self.next = True
                self.isOK[9] = True

        return self.next
