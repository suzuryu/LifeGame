class Cell:
    def __init__(self, isaliving):
        self.isaliving = isaliving
        self.neighbor_cells = []

    def check_cells(self):
        alive_count = 0
        for cell in self.neighbor_cells:
            if cell.isaliving:
                alive_count += 1

        if alive_count <= 1 or 4 <= alive_count:
            self.isaliving = 1
        else:
            self.isaliving = 0

