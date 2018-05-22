import time

from src.gamemanager import GameManager

if __name__ == '__main__':
    game_manager = GameManager()

    for _ in range(20):
        game_manager.start()
        time.sleep(0.5)

    game_manager.end()