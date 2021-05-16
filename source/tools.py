import pygame
import os

from source import setup

def load_graphics(path, accept=('.jpg', '.png', '.bmp', '.gif', '.jpeg')):
    # 加载图片
    pygame.display.set_mode((setup.WINDOW_WIDTH, setup.WINDOW_HEIGHT))
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
            graphics[name] = pygame.transform.scale(img, (setup.WINDOW_WIDTH, setup.WINDOW_HEIGHT))

    return graphics
