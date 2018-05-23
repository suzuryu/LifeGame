import time

from src.gamemanager import GameManager

if __name__ == '__main__':
    game_manager = GameManager(100, 100)

    while True:
        game_manager.start()

    game_manager.end()