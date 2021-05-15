import pygame
import moviepy.editor
class MainMenu:
    def __init__(self):

        self.setup_background()
        self.next = 'load_screen'
        self.finished = False

    def setup_background(self):
        self.background = setup.GRAPHICS['19']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(self.background_rect.width / 3),
                                                                    int(self.background_rect.height / 3)))
        self.viewport = setup.SCREEN.get_rect()

        # # http://www.fileformat.info/format/mpeg/sample/index.dir
        # FPS = 60
        #
        # pygame.init()
        # clock = pygame.time.Clock()
        # movie = pygame.movie.Movie('movie.mp4')
        # screen = pygame.display.set_mode(movie.get_size())
        # movie_screen = pygame.Surface(movie.get_size()).convert()
        #
        # movie.set_display(movie_screen)
        # movie.play()
        #
        # playing = True
        # while playing:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             movie.stop()
        #             playing = False
        #
        #     screen.blit(movie_screen, (0, 0))
        #     pygame.display.update()
        #     clock.tick(FPS)

        pygame.quit()



    def update(self, surface, keys):
  
        #self.update_cursor(keys)

        surface.blit(self.background, self.viewport)
        #surface.blit(self.caption, (170, 100))
        #surface.blit(self.player_image, (110, 490))
        #surface.blit(self.cursor.image, self.cursor.rect)

        #self.info.update()
        #self.info.draw(surface)