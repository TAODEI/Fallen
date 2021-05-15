import pygame

from source import setup
from source.Game_Engine import GameEngine
from source import L2, L4, L7, L12
#from source.L2 import Level2
#from source.L0 import L0
from source.L3 import L3

floors = [L12.Level12()]

def main():
    game = GameEngine(floors)
    game.run()

main()
