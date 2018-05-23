class Cell:
    def __init__(self, is_dying):
        # 0: dead 1: alive
        self.is_dying = is_dying
        self.next_generation = self.is_dying
        self.neighbor_cells = []

    def check_cells(self):
        alive_count = 0
        for cell in self.neighbor_cells:
            if not cell.is_dying:
                alive_count += 1

        if (alive_count <= 1 or 4 <= alive_count) and not self.is_dying:
            self.next_generation = 1
        elif alive_count == 3 and self.is_dying:
            self.next_generation = 0
        elif 2 <= self.next_generation <= 3 and not self.is_dying:
            self.next_generation = 0

    def change_next_generation(self):
        self.is_dying = self.next_generation
