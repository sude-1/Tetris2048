import random
from settings import GRID_COLS, TILE_SIZE

# Tetromino şekilleri (her biri 4 kare içeriyor)
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

        # Her kareye 2 veya 4 değerini ata
        self.values = [random.choice([2, 4]) for _ in range(4)]

        # Konum (grid üstünde), sola ortalanmış şekilde başla
        self.x = GRID_COLS // 2 - 2
        self.y = 0  # Yukarıdan başlar

    def get_cell_positions(self):
        """Tetromino'nun grid üzerindeki gerçek hücre pozisyonları."""
        return [(x + self.x, y + self.y) for (x, y) in self.blocks]

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        # Saat yönünde döndür (x, y) -> (-y, x)
        self.blocks = [(-y, x) for (x, y) in self.blocks]
