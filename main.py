import pygame
from . import constants as C, tools

def main():
    pygame.init()
    SCREEN = pygame.display.set_mode(C.SCREEN_SIZE)
    pygame.display.set_caption("Fallen")

    GRAPHICS = tools.load_graphics('resources/graphics')
    state_dict = {
        'main_menu': main_menu.MainMenu(),
        'load_screen': load_screen.LoadScreen(),
        'level': level.Level(),
        'game_over': load_screen.GameOver()
        
    } #字典控制阶段
    game = tools.Game(state_dict, 'main_menu')
    game.run()

main()