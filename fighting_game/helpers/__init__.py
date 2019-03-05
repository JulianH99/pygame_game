import pygame
from fighting_game.helpers.image import Image
from fighting_game.helpers import colors, screen
from fighting_game.helpers.path import Path


pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 16)


class HelpersFacade:
    """
    Helpers Facade

    :version: 1
    """
    image = Image

    colors = colors

    path = Path

    screen = screen

    font = font
