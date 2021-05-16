from .import setup
import pygame, time

# 写一个函数，判断一个点是否在某个范围内
# 点（x,y）
# 范围 rect(x,y,w,h)
def is_in_rect(x, y, rect):
    rx, ry, rw, rh = rect
    if (rx <= x <= rx+rw) and (ry <= y <= ry+rh):
        return True
    return False

class Level4:
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
        self.current_time = pygame.time.get_ticks()
        self.timer = 0
        self.cloud = pygame.sprite.Sprite()
        self.cloud.image = pygame.transform.scale(self.b2, (int(1536 / 2), int(2048 / 2)))
        rect = self.cloud.image.get_rect()
        rect.x, rect.y = -120, -120
        self.cloud.rect = rect
        self.is_move = False
        self.door = False
    def update_cloud(self, dir):
        w,h = self.cloud.image.get_size()
        
        #if is_in_rect(dir['x2'], dir['y2'], (self.cloud.rect.x, self.cloud.rect.y, w, h)):
        self.cloud.rect.x = dir['x2'] - w/2 + 180
        self.cloud.rect.y = dir['x2'] - w/2 + 180
            #self.cloud.rect.y = dir['y2'] - h/2
        print(w, h, self.cloud.rect.x, self.cloud.rect.y)
    def update(self, surface, keys, dir):
        if self.door:
            if 2000 > pygame.time.get_ticks() - self.timer:
                surface.blit(self.b4, surface.get_rect())
            if 4000 > pygame.time.get_ticks() - self.timer > 2000:
                surface.blit(self.b5, surface.get_rect())
        elif self.cloud.rect.x > 305:
            if 'down' in dir:
                print(dir['x'], dir['y'])
                if 260 > dir['x'] > 216 and 272 > dir['y'] > 251:
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
        
            #if self.state < 3:
                #self.update_cloud_and_girl(surface)
            '''
            if 'down' in dir and self.ok == False:
                print(self.state)

                print(dir['x'], dir['y'])

                if self.state == 2:
                    surface.blit(self.b3, surface.get_rect())
                    self.state += 1
                elif self.state == 3 and dir['x'] < 280 and dir['y'] > 100 and dir['y'] < 340:
                    surface.blit(self.b4, surface.get_rect())
                    self.state += 1
                elif self.state == 4:
                    surface.blit(self.b5, surface.get_rect())
                    self.state += 1
                elif self.state == 5 and dir['x'] > 80 and dir['x'] < 200 and dir['y'] > 200 and dir['y'] < 400:
                    surface.blit(self.b6, surface.get_rect())
                    self.state += 1
                elif self.state == 6:
                    surface.blit(self.b7, surface.get_rect())
                    self.state += 1
                    self.timer = pygame.time.get_ticks()
            if self.state == 7:
                
                    surface.blit(self.b9, surface.get_rect())
                    return True
            return False
            '''