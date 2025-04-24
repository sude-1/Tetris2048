import pygame
import sys
import time
from grid import Grid
from tetromino import Tetromino
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, TILE_SIZE, TILE_COLORS

background_image = pygame.image.load("imagee.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_tetromino(screen, tetromino):
    font = pygame.font.SysFont(None, 24)
    positions = tetromino.get_cell_positions()
    for i, (col, row) in enumerate(positions):
        if row < 0:
            continue
        value = tetromino.values[i]
        color = TILE_COLORS.get(value, (255, 255, 255))
        x = col * TILE_SIZE
        y = row * TILE_SIZE
        pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(screen, (255, 255, 255), (x, y, TILE_SIZE, TILE_SIZE), 1)



        # Sayıyı yaz:
        text = font.render(str(value), True, (0, 0, 0))  # daha yumuşak koyu gri
        text_rect = text.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
        screen.blit(text, text_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris 2048")
    clock = pygame.time.Clock()

    grid = Grid()
    current_tetromino = Tetromino()
    fall_time = 0
    fall_speed = 0.5  # saniye cinsinden

    running = True
    while running:
        screen.blit(background_image, (0, 0))

        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {grid.score}", True, (255, 128, 128))
        screen.blit(score_text, (10, 10))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if grid.is_valid_position(current_tetromino, dx=-1):
                        current_tetromino.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    if grid.is_valid_position(current_tetromino, dx=1):
                        current_tetromino.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    if grid.is_valid_position(current_tetromino, dy=1):
                        current_tetromino.move(0, 1)
                elif event.key == pygame.K_UP:
                    current_tetromino.rotate()
                    if not grid.is_valid_position(current_tetromino):
                        current_tetromino.rotate()
                        current_tetromino.rotate()
                        current_tetromino.rotate()  # 3 kere daha dönerek eski haline getir

        fall_time += clock.get_time() / 1000  # milisaniye → saniye

        if fall_time >= fall_speed:
            if grid.is_valid_position(current_tetromino, dy=1):
                current_tetromino.move(0, 1)
            else:
                grid.lock_tetromino(current_tetromino)
                grid.merge_tiles()
                grid.clear_full_rows()
                if grid.check_win():
                    print("Kazandın!")
                    game_over = True

                elif grid.check_game_over():
                    print("Oyun Bitti!")
                    game_over = True

                current_tetromino = Tetromino()
                if not grid.is_valid_position(current_tetromino):
                    print("Oyun bitti!")
                    running = False
            fall_time = 0

        grid.draw(screen)
        draw_tetromino(screen, current_tetromino)

        pygame.display.flip()
        clock.tick(60)

        # Oyun bittiğinde mesaj göster
    font = pygame.font.SysFont("arialblack", 40)  # Daha küçük, ama hâlâ güçlü bir yazı tipi
    if grid.check_win():
        message = "You Win!"
        color = (0, 200, 100)  # Yumuşak yeşil
    else:
        message = "Game Over!"
        color = (255, 128, 128)  # Orkide moru — pembe temaya çok yakışır

    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(3000)




    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


    
