import numpy as np

import cv2

from src.cell import Cell


class GameManager:
    def __init__(self, width=30, height=30):
        self.generation = 0
        self.width = width
        self.height = height
        self.cells = []
        self.init_cells()

    def init_cells(self):
        self.cells = []
        for y in range(self.height):
            self.cells.append([Cell(np.random.choice([0, 1], p=[0.3, 0.7])) for _ in range(self.width)])

        # set neighborhood cell
        for y in range(self.height):
            for x in range(self.width):
                if y - 1 > 0:
                    # 左上
                    if x - 1 >= 0:
                        self.cells[y][x].neighbor_cells.append(self.cells[y - 1][x - 1])
                    # 右上
                    if x + 1 < self.width:
                        self.cells[y][x].neighbor_cells.append(self.cells[y - 1][x + 1])
                    # 真上
                    self.cells[y][x].neighbor_cells.append(self.cells[y - 1][x])
                if y + 1 < self.height:
                    # 左下
                    if x - 1 >= 0:
                        self.cells[y][x].neighbor_cells.append(self.cells[y + 1][x - 1])
                    # 右下
                    if x + 1 < self.width:
                        self.cells[y][x].neighbor_cells.append(self.cells[y + 1][x + 1])
                    # 真下
                    self.cells[y][x].neighbor_cells.append(self.cells[y + 1][x])
                # 右
                if x + 1 < self.width:
                    self.cells[y][x].neighbor_cells.append(self.cells[y][x + 1])
                # 左
                if x - 1 >= 0:
                    self.cells[y][x].neighbor_cells.append(self.cells[y][x - 1])

    def next(self):
        for cells in self.cells:
            for cell in cells:
                    cell.check_cells()

        for cells in self.cells:
            for cell in cells:
                    cell.change_next_generation()

        self.generation += 1

    def to_image(self, scale=3.0):
        for_np_array = []
        for y in range(self.height):
            for_np_array.append([cell.isdying for cell in self.cells[y]])

        img = np.array(for_np_array, dtype=np.uint8) * 255
        wid = int(self.width * scale)
        hei = int(self.height * scale)
        img = cv2.resize(img, (wid, hei), interpolation=cv2.INTER_NEAREST)
        cv2.imshow("life-game", img)

    def end(self):
        cv2.destroyAllWindows()

    def restart(self):
        self.end()
        self.init_cells()
        self.start()

    def start(self):
        while True:
            key = cv2.waitKey(100)
            if key == ord('q'):
                self.end()
                return
            if key == ord('r'):
                self.restart()
            if key == ord('s'):
                cv2.waitKey(0)
            self.to_image(7)
            self.next()

            print('---- {} ----'.format(self.generation))

