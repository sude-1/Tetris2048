# Grid settings
GRID_ROWS = 20
GRID_COLS = 10
TILE_SIZE = 30  # pixel size of each square

# screen size
SCREEN_WIDTH = GRID_COLS * TILE_SIZE
SCREEN_HEIGHT = GRID_ROWS * TILE_SIZE

# colors (R, G, B)
BACKGROUND_COLOR = (0, 0, 0)
GRID_LINE_COLOR = (255, 255, 255)

# tile colors 
TILE_COLORS = {
   
    2: (255, 255, 204),     # light yellow
    4: (255, 230, 128),     # yellow-orange
    8: (255, 179, 102),     # light orange
    16: (255, 128, 128),    # pinky red
    32: (255, 77, 77),      # red
    64: (204, 0, 0),        # Beardeu
    128: (153, 204, 255),   # light blue
    256: (102, 178, 255),   # blue
    512: (51, 153, 255),    # cyan
    1024: (0, 102, 204),    # dark blue
    2048: (0, 76, 153),     # navy blue
}


