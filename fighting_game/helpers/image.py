import pygame
from fighting_game.helpers.screen import SCREEN_HEIGHT, SCREEN_WIDTH


class Image:

    @staticmethod
    def load(image_path: str):
        """
        Loads an image base on its path
        :param image_path: path of image to load
        :type image_path: str
        :return: Image if load was successful. Empty string if error occurred
        :rtype: Surface
        """
        try:
            return pygame.image.load(image_path).convert()
        except Exception as e:
            # implement logger
            print(e)
            return ""

    @staticmethod
    def scale_to_window(image):
        return pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
