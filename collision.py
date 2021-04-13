def game_over(snake, screen_w_h, cell_size):
    """
    Проверяем врезалась ли змеюка в саму себя или 'стену'.
    """
    if snake.snake_head_position in snake.snake_body_position or \
            snake.snake_head_position[0] < 0 or \
            snake.snake_head_position[1] < 0 or \
            snake.snake_head_position[0] > screen_w_h[0] - cell_size or \
            snake.snake_head_position[1] > screen_w_h[1] - cell_size:
        return True


def food_eaten(snake, food):
    """
    Проверяем достигнута ли змейкой клетка с едой.
    """
    if snake.snake_head_position == food.food_coordinate:
        return True
    return False


def poor_cooking(snake, food):
    """
    Следим что бы еда генерировалась на пустой клетке.
    """
    if food.food_coordinate == snake.snake_head_position or \
            food.food_coordinate in snake.snake_body_position:
        return True
    return False
