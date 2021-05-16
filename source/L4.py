from . import setup
import pygame, time


# 写一个函数，判断一个点是否在某个范围内
# 点（x,y）
# 范围 rect(x,y,w,h)
def is_in_rect(x, y, rect):
    rx, ry, rw, rh = rect
    if (rx <= x <= rx + rw) and (ry <= y <= ry + rh):
        return True
    return False


class L4:
    def __init__(self):
        self.ok = True
        self.state = -1
        self.background = setup.GRAPHICS['black']
        self.b2 = setup.GRAPHICS['4.2']
        self.b3 = setup.GRAPHICS['4.3']
        self.b4 = setup.GRAPHICS['4.4']
        self.b5 = setup.GRAPHICS['4.5']
        self.b6 = setup.GRAPHICS['4.6']
        self.b7 = setup.GRAPHICS['4.7']
        self.b8 = setup.GRAPHICS['4.8']
        self.b9 = setup.GRAPHICS['4.9']
        self.b10 = setup.GRAPHICS['4.10']
        self.b11 = setup.GRAPHICS['4.11']
        self.b12 = setup.GRAPHICS['4.12']
        self.b13 = setup.GRAPHICS['4.13']
        self.b14 = setup.GRAPHICS['4.14']
        self.b15 = setup.GRAPHICS['4.15']
        self.b16 = setup.GRAPHICS['4.16']
        self.b17 = setup.GRAPHICS['4.17']
        self.b18 = setup.GRAPHICS['4.18']
        self.timer = 0
        self.cloud = pygame.sprite.Sprite()
        self.cloud.image = pygame.transform.scale(self.b2, (int(1536 / 2), int(2048 / 2)))
        rect = self.cloud.image.get_rect()
        rect.x, rect.y = -120, -120
        self.cloud.rect = rect
        self.is_move = False
        self.door = False
        self.dot = 0

    def update_cloud(self, dir):
        w, h = self.cloud.image.get_size()

        if is_in_rect(dir['x2'], dir['y2'], (self.cloud.rect.x, self.cloud.rect.y, w, h)):
            self.cloud.rect.x = dir['x2'] - w / 2 + 180
            self.cloud.rect.y = dir['x2'] - w / 2 + 180
            # self.cloud.rect.y = dir['y2'] - h/2
        # print(w, h, self.cloud.rect.x, self.cloud.rect.y)

    def update(self, surface, keys, dir):
        if self.dot > 0:
            if 'down' in dir:
                if 367 > dir['x'] > 321 and 185 < dir['y'] < 204 or self.dot >= 4:
                    self.dot += 1
            if self.dot == 1:
                surface.blit(self.b7, surface.get_rect())
            elif self.dot == 2:
                surface.blit(self.b8, surface.get_rect())
            elif self.dot == 3:
                surface.blit(self.b9, surface.get_rect())
            elif self.dot == 4:
                surface.blit(self.b10, surface.get_rect())
            elif self.dot == 5:
                surface.blit(self.b11, surface.get_rect())
            elif self.dot == 6:
                surface.blit(self.b12, surface.get_rect())
            elif self.dot == 7:
                surface.blit(self.b13, surface.get_rect())
            elif self.dot == 8:
                surface.blit(self.b14, surface.get_rect())
            elif self.dot == 9:
                surface.blit(self.b15, surface.get_rect())
            elif self.dot == 10:
                surface.blit(self.b16, surface.get_rect())
            elif self.dot == 11:
                surface.blit(self.b17, surface.get_rect())
            elif self.dot == 12:
                surface.blit(self.b18, surface.get_rect())
                return True
        elif self.door:
            if 2000 > pygame.time.get_ticks() - self.timer:
                surface.blit(self.b4, surface.get_rect())
            if 4000 > pygame.time.get_ticks() - self.timer > 2000:
                surface.blit(self.b5, surface.get_rect())
            if pygame.time.get_ticks() - self.timer > 4000:
                surface.blit(self.b6, surface.get_rect())
                if 'down' in dir:
                    print(dir['x'], dir['y'])
                    if 367 > dir['x'] > 321 and 185 < dir['y'] < 204:
                        self.dot = 1
                        # self.timer = pygame.time.get_ticks()
        elif self.cloud.rect.x > 305:
            if 'down' in dir:
                print(dir['x'], dir['y'])
                if 270 > dir['x'] > 206 and 282 > dir['y'] > 241:
                    self.door = True
                    self.timer = pygame.time.get_ticks()
        else:
            if 'down' in dir:
                self.is_move = True
            if 'up' in dir:
                self.is_move = False

            if self.state == -1:
                self.timer = pygame.time.get_ticks()
                self.state = 0
            if pygame.time.get_ticks() - self.timer < 1000:
                surface.blit(self.background, surface.get_rect())
            if 1000 < pygame.time.get_ticks() - self.timer < 2000:
                surface.blit(self.b2, surface.get_rect())
            if pygame.time.get_ticks() - self.timer > 2000:

                surface.blit(self.b3, surface.get_rect())
                surface.blit(self.cloud.image, self.cloud.rect)
                if self.is_move:
                    self.update_cloud(dir)
