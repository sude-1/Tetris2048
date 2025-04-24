import pygame
from settings import GRID_ROWS, GRID_COLS, TILE_SIZE, TILE_COLORS, GRID_LINE_COLOR

class Grid:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

    def draw(self, screen):
            font = pygame.font.SysFont(None, 24)
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    value = self.grid[row][col]
                    x = col * TILE_SIZE
                    y = row * TILE_SIZE

                    if value != 0:
                        color = TILE_COLORS.get(value, (220, 220, 180))
                        pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))
                        
                        # draw the number
                        text = font.render(str(value), True, (0, 0, 0))
                        text_rect = text.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
                        screen.blit(text, text_rect)

                    pygame.draw.rect(screen, GRID_LINE_COLOR, (x, y, TILE_SIZE, TILE_SIZE), 1)


    def is_valid_position(self, tetromino, dx=0, dy=0):
        for (x, y) in tetromino.get_cell_positions():
            x += dx
            y += dy
            if x < 0 or x >= GRID_COLS or y >= GRID_ROWS:
                return False
            if y >= 0 and self.grid[y][x] != 0:
                return False
        return True

    def lock_tetromino(self, tetromino):
        positions = tetromino.get_cell_positions()
        for i, (x, y) in enumerate(positions):
            if 0 <= y < GRID_ROWS and 0 <= x < GRID_COLS:
                self.grid[y][x] = tetromino.values[i]

    def merge_tiles(self):
        for col in range(GRID_COLS):
            row = GRID_ROWS - 1
            while row > 0:
                current = self.grid[row][col]
                above = self.grid[row - 1][col]
                if current != 0 and current == above:
                    merged_value = current * 2
                    self.grid[row][col] = merged_value
                    self.grid[row - 1][col] = 0
                    self.score += merged_value  # add point

                    for r in range(row - 1, 0, -1):
                        self.grid[r][col] = self.grid[r - 1][col]
                    self.grid[0][col] = 0

                    row += 1
                row -= 1



    def _collapse_column(self, col, start_row):
         for row in range(start_row, -1, -1):
            self.grid[row + 1][col] = self.grid[row][col]
            self.grid[row][col] = 0

    def clear_full_rows(self):
        new_grid = []
        cleared_rows = 0
        for row in self.grid:
            if 0 not in row:
                self.score += sum(row)  # row point
                cleared_rows += 1
            else:
                new_grid.append(row)

        for _ in range(cleared_rows):
            new_grid.insert(0, [0 for _ in range(GRID_COLS)])

        self.grid = new_grid
        return cleared_rows

    
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
        self.score = 0  # point


    def check_win(self):
        for row in self.grid:
            if 2048 in row:
                return True
        return False

    def check_game_over(self):
        for cell in self.grid[0]:  
            if cell != 0:
                return True
        return False
