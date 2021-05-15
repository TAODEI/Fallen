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
        self.girl_height = -setup.WINDOW_HEIGHT
        # 掉落速度
        self.fall_v = 15

    def update(self, surface: Surface, keys, dir) -> object:
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
            surface.blit(self.background, surface.get_rect())
            surface.blit(self.girl, (0, self.girl_height, surface.get_rect().width,  surface.get_rect().height))
            surface.blit(cloud, surface.get_rect())

            if self.time_count > 500:
                self.time_count = 0
