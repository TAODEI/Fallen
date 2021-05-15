import pygame
from pygame.surface import Surface

from source import setup


class L0:
    def __init__(self):
        self.a = 0

    def abaaab(surface):
        FPS = 60
        clock = pygame.time.Clock()
        movie = pygame.movie.Movie('resources/Fallen/movie.mp4')
        screen = pygame.display.set_mode(movie.get_size())
        movie_screen = pygame.Surface(movie.get_size()).convert()

        movie.set_display(movie_screen)
        movie.play()

        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    movie.stop()
                    playing = False

            screen.blit(movie_screen, (0, 0))
            pygame.display.update()
            clock.tick(FPS)

        pygame.quit()

    def refresh(self, surface: Surface) -> object:
        background = setup.GRAPHICS['18']
        background = pygame.transform.scale(background, (setup.WINDOW_WIDTH, setup.WINDOW_HEIGHT))
        surface.blit(background, surface.get_rect())

        return None
