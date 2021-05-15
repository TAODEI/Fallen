from source import tools, setup
from source import main_menu


def main():

    game = tools.Game(main_menu.MainMenu())
    game.run()


main()
