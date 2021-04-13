import pygame
import sys


def check_events(snake=None):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Выход из игры нажатием на крестик в углу окна.
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and snake:
            if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT,
                             pygame.K_RIGHT):
                # Движение змейки.
                snake.snake_change_direction(event.key)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Выход из игры в конце "заезда".
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                # Старт новой игры после "смерти" змейки.
                return True
