import pygame

from source import setup
from source.Game_Engine import GameEngine
from source import L2
#from source.L2 import Level2

floors = [L2.Level2()]


def main():
    game = GameEngine(floors)
    game.run()

main()
