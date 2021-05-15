import pygame

from source import setup
from source.Game_Engine import GameEngine
from source import L2
#from source.L2 import Level2
from source.L0 import L0
from source.L3 import L3
from source.L5 import L5
from source.L6 import L6

floors = [L6()]


def main():
    game = GameEngine(floors)
    game.run()

main()
