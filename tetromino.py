import random
from settings import GRID_COLS, TILE_SIZE

# tetromino shapes (each includes 4 blocks)
SHAPES = {
    'I': [(0, 1), (1, 1), (2, 1), (3, 1)],
    'O': [(1, 0), (2, 0), (1, 1), (2, 1)],
    'T': [(1, 0), (0, 1), (1, 1), (2, 1)],
    'S': [(1, 1), (2, 1), (0, 2), (1, 2)],
    'Z': [(0, 1), (1, 1), (1, 2), (2, 2)],
    'J': [(0, 0), (0, 1), (1, 1), (2, 1)],
    'L': [(2, 0), (0, 1), (1, 1), (2, 1)]
}

class Tetromino:
    def __init__(self):
        self.shape_name = random.choice(list(SHAPES.keys()))
        self.blocks = SHAPES[self.shape_name]

        # put 2 or 4 for each block
        self.values = [random.choice([2, 4]) for _ in range(4)]

        
        self.x = GRID_COLS // 2 - 2
        self.y = 0  # starts from upside

    def get_cell_positions(self):
        
        return [(x + self.x, y + self.y) for (x, y) in self.blocks]

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        # rotate clockwise (x, y) -> (-y, x)
        self.blocks = [(-y, x) for (x, y) in self.blocks]
