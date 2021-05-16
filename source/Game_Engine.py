import pygame
from . import setup


class GameEngine:

    # 初始化pygame
    def __init__(self, floors):
        self.floors = floors
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.mouse_keys = pygame.mouse.get_pressed()
        self.surface = pygame.display.set_mode((setup.WINDOW_WIDTH, setup.WINDOW_HEIGHT))
        self.i = 0
        self.x2 = 0
        self.y2 = 0

    def run(self):
        while True:
            
            # 检测是否点击关闭
            keys_dir = {'x2': self.x2, 'y2': self.y2}
            for event in pygame.event.get():
                # 点X
                if event.type is pygame.QUIT or (event.type is pygame.KEYDOWN and event.key is pygame.K_q):
                    pygame.display.quit()
                    quit()
                elif event.type is pygame.KEYDOWN:
                    keys_dir.update()
                    self.keys = pygame.key.get_pressed()
                elif event.type is pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    keys_dir['down'] = True
                    keys_dir['x'], keys_dir['y'] = event.pos
                elif event.type == pygame.MOUSEBUTTONUP:
                    keys_dir['up'] = True
                elif event.type == pygame.MOUSEMOTION:
                    keys_dir['motion'] = True
                    self.x2, self.y2 = keys_dir['x2'], keys_dir['y2'] = pygame.mouse.get_pos()
            # 调用floor刷新
            exit_s = self.floors[self.i].update(self.surface, self.keys, keys_dir)

            if exit_s:
                self.i = self.i + 1
                if self.i >= len(self.floors):
                    exit(0)


            # 刷新界面
            self.update()

            # 限制帧率
            self.clock.tick(80)

    def update(self):
        pygame.display.update()
