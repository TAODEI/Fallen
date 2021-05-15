import pygame

from source import setup
from source.Game_Engine import GameEngine
from source import L2, L4
#from source.L2 import Level2
#from source.L0 import L0
from source.L3 import L3

floors = [L4.Level4()]

def main():
    game = GameEngine(floors)
    game.run()

main()
