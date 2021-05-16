import pygame

from source import setup
from source.Game_Engine import GameEngine
from source import L2, L4, L7, L12
#from source.L2 import Level2
#from source.L0 import L0
from source.L3 import L3
from source.L1 import L1

floors = [L12.Level12()]

def main():
    pygame.mixer.init()
    pygame.mixer.music.load("resources/lace.mp3")
    pygame.mixer.music.set_volume(9)

    pygame.mixer.music.play()
    game = GameEngine(floors)
    game.run()

main()
