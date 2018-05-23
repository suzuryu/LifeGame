class Cell:
    def __init__(self, isaliving):
        self.isaliving = isaliving
        self.next_generation = 0
        self.neighbor_cells = []

    def check_cells(self):
        alive_count = 0
        for cell in self.neighbor_cells:
            if not cell.isaliving:
                alive_count += 1

        if alive_count <= 1 or 4 <= alive_count:
            self.next_generation = 1
        else:
            self.next_generation = 0

    def change_next_generation(self):
        self.isaliving = self.next_generation
