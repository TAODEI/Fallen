#import cv2
import cv2
import pygame
from pygame.surface import Surface, SurfaceType

from source import setup


class L0:
    def __init__(self):
        # 是否进入下一层
        self.next = False
        # 读取视频下一帧成功
        self.success = True
        # 视频源
        self.video_resource = cv2.VideoCapture("resources/Fallen/movie.mp4")
        # 视频宽
        self.width = int(self.video_resource.get(cv2.CAP_PROP_FRAME_WIDTH))
        # 视频高
        self.height = int(self.video_resource.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # 循环计数
        self.time_count = 0
        # 是否播放视频
        self.play_video = True
        self.title_has = False
        self.v = 10
        self.pos = 0
        # 标题初始不透明度
        self.alpha = 0
        # 标题不透明度每次增量
        self.add_alpha = 30
        self.title = setup.GRAPHICS['Title']

    def video2frame(self) -> [Surface, SurfaceType]:
        """将视频读取，返回值为当前帧"""
        # 按帧读取视频
        self.success, image = self.video_resource.read()
        if self.success:
            img = pygame.image.frombuffer(image.tostring(), (self.width, self.height), "RGB")
            self.success, image = self.video_resource.read()
            return img
        else:
            self.play_video = False
            return None

    def update(self, surface: Surface, keys, dir) -> object:

        self.time_count += 1
        # 播放视频
        if self.play_video:
            if self.time_count % 7 == 0:
                self.time_count = 0
                frame = self.video2frame()
                if frame is not None:
                    background = pygame.transform.scale(frame, (setup.WINDOW_WIDTH, setup.WINDOW_HEIGHT))
                    surface.blit(background, surface.get_rect())

        # 出现标题
        elif not self.title_has:
            if self.time_count % 7 == 0:
                self.title.set_alpha(self.alpha)
                self.alpha += self.add_alpha
                surface.blit(self.title, surface.get_rect())
                if self.title.get_alpha() >= 150:
                    self.time_count = 0
                    self.title_has = True

        elif self.time_count>100 and  self.time_count % 7 == 0:
            self.pos += self.v
            surface.blit(self.title, (0, self.pos))

        # 返回值判断（一个延时）
        if self.pos >= setup.WINDOW_HEIGHT and self.time_count > 300:
            return True
        else:
            return False
