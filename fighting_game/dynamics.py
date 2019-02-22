from enum import Enum
from typing import List
from pygame import Surface
from fighting_game.helpers.image import Image
from fighting_game.helpers.colors import BLACK
import os


class MovingAnimation(Enum):
    """
    Animation types for making common strings to access moving sprite sheets
    """
    LEFT = 'left'
    RIGHT = 'right'
    JUMP = 'jump'

    def __str__(self):
        return self.value


class FightingAnimation(Enum):
    """
    Animation types for common access to fighting movements
    """
    FIST = 'fist'
    DEFENSE = 'defense'
    LARGE_ATTACK = 'large_attack'


class ProFightingAnimation(Enum):
    """
    Animation types for common access to pro fighting movements
    """
    PRO_FIST = 'pro_fist'
    PRO_DEFENSE = 'pro_defense'
    PRO_LARGE_ATTACK = 'pro_large_attack'


class SpriteSheet:
    """
    Represents a list of images or frames brought from a specific folder
    """

    def __init__(self, base_sprite_path: str, frames: int):
        """
        Initializes the SpriteSheet class, the **base_sprite_path** and **frames** params
        are required

        :param base_sprite_path: base folder path to load the sprites from
        :type base_sprite_path: str
        :param frames: number of frames or images to load
        :type frames: int
        """
        self.base_sprite_path: str = base_sprite_path
        self.frames: int = frames
        self.key_name: str = None
        self.base_file_name: str = None
        self.images: List[Surface] = []

    def load_images(self):
        """
        Loads the images according to the **base_sprite_path** and **frames**, and two
        properties that must be previously set (key_name and base_file_name) to load
        all the images
        :return:
        """
        if not (self.key_name and self.base_file_name):
            raise ValueError('key_name or base_file_name not set')

        if not self.images:
            self.images = []

        for frame in range(self.frames):
            file_format = "{} ({}).png".format(self.base_file_name, frame + 1)

            image = Image.load(os.path.join(self.base_sprite_path, file_format))
            image.set_colorkey(BLACK)
            self.images.append(image)
