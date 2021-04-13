import pygame

import game_settings
import collision
from snake import Snake
from food import Food
from keyboard import check_events


pygame.init()
screen = pygame.display.set_mode(game_settings.SCREEN_WIDTH_AND_HEIGHT)
pygame.display.set_caption('Snake')

score = 0


def play_again():
    """
    Конец игры (змейка врезалась в стену или свой хвост).
    """
    end_the_game = False
    text = f'ОГО! У вас {score * 10} баллов). Esc: выход, Space: еще попытка.'
    font = pygame.font.SysFont('Verdana', size=20)
    result = font.render(text, True, (40, 40, 40))
    screen.blit(result, (15, 15))
    pygame.display.update()
    while not end_the_game:
        if check_events():
            run_game()


def run_game():
    """
    Основной цикл игры.
    """
    global score
    score = 0
    player = Snake()
    food = Food()

    # Цикл игры.
    while True:
        # Закрашиваем экран.
        screen.fill(game_settings.BACKGROUND_COLOR)

        # Проверяем нажатие клавиш.
        check_events(player)

        # Двигаем змейку.
        player.snake_moving()

        # Отрисовываем змейку на актуальных координатах.
        player.draw_snake(screen)

        # Отрисовываем еду.
        food.draw_food(screen)

        # Если есть столкновение головы с телом\краем игрового окна - конец.
        if collision.game_over(player, game_settings.SCREEN_WIDTH_AND_HEIGHT,
                               game_settings.CELL_SIZE):
            break

        # Если змейка поела - растёт и получает баллы.
        if collision.food_eaten(player, food):
            player.add_new_segment()
            food.create_new_food()
            score += 1

            # Не создаем еду поверх змейки.
            while collision.poor_cooking(player, food):
                food.create_new_food()

        # Обновляем экран.
        pygame.display.update()

    play_again()


if __name__ == '__main__':
    run_game()
