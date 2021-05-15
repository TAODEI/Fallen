import pygame

from source import setup
from source.Game_Engine import GameEngine
from source import L2, L4
#from source.L2 import Level2
from source.L0 import L0
from source.L3 import L3

<<<<<<< HEAD
floors = [L3()]
=======
floors = [L4.Level4()]
>>>>>>> e5b4ac3f7212079a6f970c3513c0c96b867e40b6


def main():
    game = GameEngine(floors)
    game.run()

main()
