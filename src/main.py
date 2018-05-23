from msvcrt import getch

from src.gamemanager import GameManager

if __name__ == '__main__':
    game_manager = GameManager(100, 100)
    game_manager.start()
