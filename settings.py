# Grid ayarları
GRID_ROWS = 20
GRID_COLS = 10
TILE_SIZE = 30  # Her karenin piksel boyutu

# Ekran boyutu
SCREEN_WIDTH = GRID_COLS * TILE_SIZE
SCREEN_HEIGHT = GRID_ROWS * TILE_SIZE

# Renkler (R, G, B)
BACKGROUND_COLOR = (0, 0, 0)
GRID_LINE_COLOR = (255, 255, 255)

# Tile renkleri – değerine göre
TILE_COLORS = {
   
    2: (255, 255, 204),     # Açık sarı
    4: (255, 230, 128),     # Sarı-turuncu
    8: (255, 179, 102),     # Açık turuncu
    16: (255, 128, 128),    # Mercan kırmızı
    32: (255, 77, 77),      # Kırmızı
    64: (204, 0, 0),        # Bordo
    128: (153, 204, 255),   # Açık mavi
    256: (102, 178, 255),   # Mavi
    512: (51, 153, 255),    # Canlı mavi
    1024: (0, 102, 204),    # Koyu mavi
    2048: (0, 76, 153),     # Lacivert
}


