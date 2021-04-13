import pygame

import game_settings
from keyboard import check_events


pygame.init()
screen = pygame.display.set_mode(game_settings.SCREEN_WIDTH_AND_HEIGHT)
pygame.display.set_caption('Snake')


def run_game():
    """
    Основной цикл игры.
    """

    while True:
        # Закрашиваем экран.
        screen.fill(game_settings.BACKGROUND_COLOR)

        # Проверяем нажатие клавиш.
        check_events()

        # Обновляем экран.
        pygame.display.update()


if __name__ == '__main__':
    run_game()
