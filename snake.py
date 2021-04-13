import pygame

from game_settings import SCREEN_WIDTH_AND_HEIGHT, CELL_SIZE


class Snake:
    """
    Класс змейки. Цвет головы, тела, начальные координаты,
    координаты головы, тела, направление движения, скорость движения.
    """

    def __init__(self):
        self.snake_head_color = (34, 99, 61)
        self.snake_body_color = (50, 175, 100)
        self.snake_start_position = (
            SCREEN_WIDTH_AND_HEIGHT[0] // 2, SCREEN_WIDTH_AND_HEIGHT[1] // 2)
        self.snake_head_position = [self.snake_start_position[0],
                                    self.snake_start_position[1]]
        self.snake_body_position = [
            [self.snake_head_position[0],
             self.snake_head_position[1] + CELL_SIZE],
            [self.snake_head_position[0],
             self.snake_head_position[1] + CELL_SIZE * 2],
        ]
        # direction: {8: up, 6: right, 2: down, 4: left}
        self.snake_moving_direction = 8
        # Чем выше значение в snake_speed, тем медленней змейка двигается.
        self.snake_speed = 105
        # В SNAKE_SPEED_COUNTER будем считать когда смещать змейку на экране.
        self.SNAKE_SPEED_COUNTER = 0

    def draw_snake(self, screen):
        """
        Отрисовка змейки на экране.
        """
        # Тело
        for i in self.snake_body_position:
            pygame.draw.rect(screen, self.snake_body_color, (
                i[0], i[1], CELL_SIZE, CELL_SIZE
            ))
        # Голова
        pygame.draw.rect(screen, self.snake_head_color, (
            self.snake_head_position[0], self.snake_head_position[1],
            CELL_SIZE, CELL_SIZE
        ))

    def snake_moving(self):
        """
        Меняем координаты головы и тела в зависимости от
        выбранного направления движения.
        """
        self.SNAKE_SPEED_COUNTER += 1
        if self.SNAKE_SPEED_COUNTER > self.snake_speed:
            self.SNAKE_SPEED_COUNTER = 0
            self.snake_body_position.insert(0, self.snake_head_position.copy())
            self.snake_body_position.pop()
            if self.snake_moving_direction == 8:
                self.snake_head_position[1] -= CELL_SIZE
            elif self.snake_moving_direction == 2:
                self.snake_head_position[1] += CELL_SIZE
            elif self.snake_moving_direction == 6:
                self.snake_head_position[0] += CELL_SIZE
            elif self.snake_moving_direction == 4:
                self.snake_head_position[0] -= CELL_SIZE

    def snake_change_direction(self, key):
        """
        Меняем направление движения змейки.
        """
        if key == pygame.K_UP and self.snake_moving_direction != 2:
            self.snake_moving_direction = 8
        elif key == pygame.K_DOWN and self.snake_moving_direction != 8:
            self.snake_moving_direction = 2
        elif key == pygame.K_LEFT and self.snake_moving_direction != 6:
            self.snake_moving_direction = 4
        elif key == pygame.K_RIGHT and self.snake_moving_direction != 4:
            self.snake_moving_direction = 6

    def add_new_segment(self):
        """
        Увеличиваем длину змейки когда она съедает единицу пищи.
        """
        new_segment = self.snake_body_position[-1].copy()
        if self.snake_moving_direction == 2:
            new_segment[1] -= CELL_SIZE
        elif self.snake_moving_direction == 8:
            new_segment[1] += CELL_SIZE
        elif self.snake_moving_direction == 4:
            new_segment[0] += CELL_SIZE
        elif self.snake_moving_direction == 6:
            new_segment[0] -= CELL_SIZE
        self.snake_body_position.append(new_segment)
        self.level_up()

    def level_up(self):
        """
        По мере роста змеюки, будем повышать ее скорость!
        """
        if self.snake_speed >= 25:
            self.snake_speed -= 2
