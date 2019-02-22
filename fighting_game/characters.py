import pygame
import os
from abc import abstractmethod
from typing import Dict
from fighting_game.helpers.colors import *
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path
from fighting_game.dynamics import SpriteSheet, MovingAnimation, FightingAnimation, ProFightingAnimation
from fighting_game.helpers.screen import SCREEN_WIDTH
from typing import Tuple


class Character(pygame.sprite.Sprite):
    """
    Represents the basic character that the user will see in screen
    """
    width = 64
    height = 64

    def __init__(self, x=0, y=0):
        super().__init__()

        self.name = None
        # Path to sprite images
        self.path = self.get_sprite_path()

        # Position initializing and loading basic image
        self.image = self.get_base_image()
        self.image.set_colorkey(BLACK)
        self.x = x
        self.y = y

        self.rect = self.image.get_rect()

        # repositioning
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 3

        # jumping base variables
        self.force = 8
        self.mass = 2

        self.sprite_sheets: Dict[str, SpriteSheet] = {}

        self.states = {
            "right": False,
            "left": False,
            "attack": False,
            "large_attack": False
        }

        self.playing_animation: SpriteSheet = None
        self.animation_step = 0
        self.current_index = 0

    @abstractmethod
    def get_base_image(self):
        pass

    @abstractmethod
    def get_sprite_path(self):
        pass

    def set_x_y(self, x_y):
        """
        Sets the position of the character in screen
        :param x_y: Tuple with two integers, representing the position in two axes
        :type x_y: Tuple[int, int]
        """

        self.rect.centery = x_y[1]
        self.rect.centerx = x_y[0]

    def add_sprite_sheet(self, key: str, sprite_sheet: SpriteSheet):
        if key in self.sprite_sheets:
            raise KeyError("{} is already defined".format(key))
        self.sprite_sheets[key] = sprite_sheet

    def trigger_animation(self, animation):
        if isinstance(animation, MovingAnimation) or \
                isinstance(animation, FightingAnimation) or \
                isinstance(animation, ProFightingAnimation):
            self.playing_animation = self.sprite_sheets[animation.value]

            if animation == MovingAnimation.LEFT:
                self.trigger_left()

            if animation == MovingAnimation.RIGHT:
                self.trigger_right()

        else:
            raise ValueError('animation should be a valid Animation type')

    def trigger_left(self):
        self.rect.centerx -= self.speed

    def trigger_right(self):
        self.rect.centerx += self.speed

    def update(self, *args):
        if self.playing_animation:
            if self.current_index < len(self.playing_animation.images):
                self.image = self.playing_animation.images[self.current_index]
                self.current_index += 1
            else:
                self.current_index = 0
                self.playing_animation = None


class Maid(Character):

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.name = 'Maid'

    def get_base_image(self):
        return Image.load(os.path.join(self.path, "MaidBasicModel.png"))

    def get_sprite_path(self):
        return Path.path_to("sprite_sheets", "Maid")


class Bowsette(Character):

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.name = 'Bowsette'

    def get_base_image(self):
        return Image.load(os.path.join(self.path, "BowsetteBasicModel.png"))

    def get_sprite_path(self):
        return Path.path_to("sprite_sheets", "Bowsette")
