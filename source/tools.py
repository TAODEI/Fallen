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

# '''应该用不上'''

#
# def get_image(sheet, x, y, width, height, colorkey, scale):
#     '''从图片(sheet)获取部分'''
#     image = pygame.Surface((width, height))
#     image.blit(sheet, (0, 0), (x, y, width, height))  # (0, 0)代表画的位置，(x,y,w,h)代表sheet里的哪个区域
#     image.set_colorkey(colorkey)
#     # 放大
#     image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
#     return image
