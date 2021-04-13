import pygame
import sys


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Выход из игры нажатием на крестик в углу окна.
            pygame.quit()
            sys.exit()
