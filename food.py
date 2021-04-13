import pygame
from random import randint

from game_settings import SCREEN_WIDTH_AND_HEIGHT, CELL_SIZE


class Food:
    """
    Класс генерируемой еды для змейки.
    """
    def __init__(self):
        self.food_color = (214, 27, 24)
        self.food_coordinate = [0, 0]
        self.create_new_food()

    def draw_food(self, screen):
        pygame.draw.rect(screen, self.food_color,
                         (self.food_coordinate[0], self.food_coordinate[1],
                          CELL_SIZE, CELL_SIZE))

    def create_new_food(self):
        self.food_coordinate = [
            randint(0, SCREEN_WIDTH_AND_HEIGHT[0] / CELL_SIZE - 1) * CELL_SIZE,
            randint(0, SCREEN_WIDTH_AND_HEIGHT[1] / CELL_SIZE - 1) * CELL_SIZE
        ]
