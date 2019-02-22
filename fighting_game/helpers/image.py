import pygame


class Image:

    @staticmethod
    def load(image_path: str):
        try:
            return pygame.image.load(image_path).convert()
        except Exception as e:
            # implement logger
            print(e)
            return ""
