import cv2
import pygame
from pygame.surface import Surface

from source import setup


class L0:
    def __init__(self):
        self.next = False
        self.success = True
        self.video_resource = cv2.VideoCapture("resources/Fallen/movie.mp4")
        self.count = 0
        self.width = int(self.video_resource.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.video_resource.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.time_count = 0
        self.play_video = True
        self.alpha = 0
        self.add_alpha = 1
        self.title = setup.GRAPHICS['Title']

    def video2frame(self):

        # 按帧读取视频
        self.success, image = self.video_resource.read()
        self.count += 1
        if self.success:
            img = pygame.image.frombuffer(image.tostring(), (self.width, self.height), "RGB")
            self.success, image = self.video_resource.read()
            return img
        else:
            self.play_video = False
            return None

    def update(self, surface: Surface) -> object:
        self.time_count += 1
        if self.play_video:
            if self.time_count % 7 == 0:
                self.time_count = 0
                frame = self.video2frame()
                if frame is not None:
                    background = pygame.transform.scale(frame, (setup.WINDOW_WIDTH, setup.WINDOW_HEIGHT))
                    surface.blit(background, surface.get_rect())
        elif self.time_count % 7 == 0:
            self.title.set_alpha(self.alpha)
            self.alpha += self.add_alpha
            surface.blit(self.title, surface.get_rect())
        return None
