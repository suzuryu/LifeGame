class Cell:
    def __init__(self, isdying):
        self.isdying = isdying
        self.next_generation = self.isdying
        self.neighbor_cells = []

    def check_cells(self):
        alive_count = 0
        for cell in self.neighbor_cells:
            if not cell.isdying:
                alive_count += 1

        if (alive_count <= 1 or 4 <= alive_count) and self.isdying == 0:
            self.next_generation = 1
        elif alive_count == 3 and self.isdying == 1:
            self.next_generation = 0
        elif 2 <= self.next_generation <= 3 and self.isdying == 0:
            self.next_generation = 0

    def change_next_generation(self):
        self.isdying = self.next_generation
