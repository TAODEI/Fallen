import pygame

from source import setup, tools
from source.Game_Engine import GameEngine
from source.L0 import L0
from source.L1 import L1
from source.L10 import L10
from source.L11 import L11
from source.L12 import L12
from source.L2 import L2
from source.L3 import L3
from source.L4 import L4
from source.L5 import L5
from source.L6 import L6
from source.L7 import L7
from source.L8 import L8
from source.L9 import L9


def main():
    pygame.display.set_icon(pygame.image.load('resources/Fallen/icon.png'))
    pygame.display.set_caption('Fallen')

    pygame.init()
    setup.GRAPHICS = tools.load_graphics('resources/Fallen')

    floors = [
        L0(),
        L1(),
        L2(),
        L3(),
        L4(),
        L5(),
        L6(),
        L7(),
        L8(),
        L9(),
        L10(),
        L11(),
        L12()
    ]

    game = GameEngine(floors)
    game.run()


main()
