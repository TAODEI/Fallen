# import cv2
import cv2
import pygame
from moviepy.video.fx.resize import resize
from pygame.surface import Surface, SurfaceType
from source.editor import *
from moviepy import decorators
from source import setup


class L0:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("resources/bgm.mp3")
        pygame.mixer.music.set_volume(9)
        # 是否进入下一层
        self.next = False
        # 读取视频下一帧成功
        self.success = True
        # 视频源
        self.video_resource = "resources/Fallen/movie.mp4"
        # 循环计数
        self.time_count = 0
        # 是否播放视频
        self.play_video = True
        self.title_has = False
        self.a = 3
        self.v = 0
        self.pos = 0
        # 标题初始不透明度
        self.alpha = 0
        # 标题不透明度每次增量
        self.add_alpha = 5
        self.title = setup.GRAPHICS['Title']
        self.clock = pygame.time.Clock()
        self.FPS = 30
        video = VideoFileClip(self.video_resource)

        self.clip = resize(video, width=setup.WINDOW_WIDTH).subclip().without_audio()

    def update(self, surface: Surface, keys, dir) -> object:
        self.clock.tick(self.FPS)
        # if not pygame.mixer.music.get_busy():
        #     pygame.mixer.music.play()
        # 声音听不到，下课再说
        self.time_count += 1
        # 播放视频
        if self.play_video:
            pygame.mixer.music.load('resources/bgm.mp3')
            pygame.mixer.music.play(0)
            self.clip.preview()
            self.play_video = False

        # 出现标题
        elif not self.title_has:
            self.title.set_alpha(self.alpha)
            self.alpha += self.add_alpha
            surface.blit(setup.GRAPHICS['14.4'],surface.get_rect())
            surface.blit(self.title, surface.get_rect())
            if self.title.get_alpha() >= 200:
                self.time_count = 0
                self.title_has = True

        # 标题掉
        elif self.time_count > 100:
                #搞成加速度
            if self.v < self.a:
                self.v += 0.1
            self.pos += self.v
        surface.blit(setup.GRAPHICS['14.4'], surface.get_rect())

        surface.blit(self.title, (0, self.pos))

        # 返回值判断（一个延时）
        if self.pos >= setup.WINDOW_HEIGHT and self.time_count > 300:
            return True
        else:
            return False
