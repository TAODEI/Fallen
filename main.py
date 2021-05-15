import pygame

from source import setup
from source.Game_Engine import GameEngine
from source.L0 import L0

floors = [L0()]


def main():
    game = GameEngine(floors)
    game.run()

main()
