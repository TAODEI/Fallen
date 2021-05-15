from source import tools, setup
from source import main_menu

def main():
    state_dict = {
        'main_menu': main_menu.MainMenu(),
        #'load_screen': load_screen.LoadScreen(),
        #'level': level.Level(),
        #'game_over': load_screen.GameOver()
        
    } #字典控制阶段
    game = tools.Game(state_dict, 'main_menu')
    game.run()

main()