import pygame
import os


class Game:
    def __init__(self, start_state):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.state = start_state

    def update(self):
        if self.state.finished:  # 当前阶段是否完结
            game_info = self.state.game_info
            self.state.finished = False
            self.state.start(game_info)
        self.state.update(self.screen, self.keys)

    def run(self):
        while True:
            for event in pygame.event.get():
                # 点X
                if event.type is pygame.QUIT:
                    pygame.display.quit()
                    quit()
                # 侦测键盘事件
                elif event.type is pygame.KEYDOWN:
                    if event.key is pygame.K_q:
                        pygame.display.quit()
                        quit()
                    self.keys = pygame.key.get_pressed()
                elif event.type is pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()



            self.update()

            pygame.display.update()
            # 帧率
            self.clock.tick(80)


def load_graphics(path, accept=('.jpg', '.png', '.bmp', '.gif')):
    '''加载图片'''
    graphics = {}
    for pic in os.listdir(path):
        # 拆分文件名 判断是否合法
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            if img.get_alpha():
                # 透明图像
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img

    return graphics


'''应该用不上'''


def get_image(sheet, x, y, width, height, colorkey, scale):
    '''从图片(sheet)获取部分'''
    image = pygame.Surface((width, height))
    image.blit(sheet, (0, 0), (x, y, width, height))  # (0, 0)代表画的位置，(x,y,w,h)代表sheet里的哪个区域
    image.set_colorkey(colorkey)
    # 放大
    image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    return image
