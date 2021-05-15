import pygame
import os
from . import setup


class GameEngine:

    # 初始化pygame
    def __init__(self, floors):
        pygame.init()
        self.floors = floors
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.surface = pygame.display.set_mode((setup.WINDOW_WIDTH, setup.WINDOW_HEIGHT))
        self.iter = floors[0]

    def run(self):
        while True:
            # 检测是否点击关闭
            for event in pygame.event.get():
                # 点X
                if event.type is pygame.QUIT or (event.type is pygame.KEYDOWN and event.key is pygame.K_q):
                    pygame.display.quit()
                    quit()
                elif event.type is pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type is pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            # 调用floor刷新
            state = self.iter.update(self.surface, self.keys)

            # 刷新界面
            self.update()

            # 限制帧率
            self.clock.tick(80)

    def update(self):
        pygame.display.update()
