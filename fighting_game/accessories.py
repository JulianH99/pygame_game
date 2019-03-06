import pygame
from abc import abstractmethod, ABCMeta
from fighting_game.helpers.path import Path
from fighting_game.helpers.image import Image
from fighting_game.dynamics import Attributes
from fighting_game.helpers.colors import *
from fighting_game.helpers.screen import GROUND_AREA_Y
from fighting_game.dynamics import ProFightingAnimation, FightingAnimation
from typing import Dict
import enum

class Accessory(pygame.sprite.Sprite, metaclass=ABCMeta):


    def __init__(self):
        super().__init__()
        self.attributes = self.build_attributes()
        self.image = self.get_sprite()
        self.image.set_colorkey(BLACK)
        self.power_up = self.get_power_up()

        self.rect = self.image.get_rect()
        self.rect.centery = GROUND_AREA_Y

    @abstractmethod
    def build_attributes(self):
        """
        Builds the attributes for the accessory
        :return: attributes_list
        :rtype: Attributes
        """
        pass

    @abstractmethod
    def get_sprite(self):
        """
        Returns the sprite image of the accessory
        :return: Image for the accessory sprite
        :rtype: Surface
        """
        pass

    @abstractmethod
    def get_power_up(self) -> Dict:
        pass


    def set_x(self, x: int):
        self.rect.centerx = x

    def draw(self, screen, position):
        """
        Draws the accessory to the screen

        :param screen: Screen object
        :type screen: Surface

        :param position: Position of the accessories
        :type position: (int, int)
        """
        pass


class Slopes(Accessory):

    def __init__(self):
        super().__init__()

    def get_sprite(self):
        return Image.load(Path.path_to("accessories", "Slopes.png"))

    def build_attributes(self):
        return Attributes(
            speed=10,
            defense=0,
            attack=3
        )

    def get_power_up(self) -> Dict:
        return {
            "replace": FightingAnimation.LARGE_ATTACK,
            "for": ProFightingAnimation.PRO_LARGE_ATTACK
        }


class Toast(Accessory):
    def __init__(self):
        super().__init__()

    def get_sprite(self):
        return Image.load(Path.path_to("accessories", "Toast.png"))

    def build_attributes(self):
        return Attributes(
            speed=5,
            defense=10,
            attack=-3
        )

    def get_power_up(self) -> Dict:
        return {
            "replace": FightingAnimation.DEFENSE,
            "for": ProFightingAnimation.PRO_DEFENSE
        }


class TransmutationCircle(Accessory):

    def __init__(self):
        super().__init__()

    def get_sprite(self):
        return Image.load(Path.path_to("accessories", "TransmutationCircle.png"))

    def build_attributes(self):
        return Attributes(
            speed=10,
            defense=10,
            attack=-10
        )

    def get_power_up(self) -> Dict:
        return {
            "replace": FightingAnimation.FIST,
            "for": ProFightingAnimation.PRO_FIST
        }


class Accessories(enum.Enum):
    slopes = Slopes
    toast = Toast
    transmutation_circle = TransmutationCircle


class AccessoryFactory:

    @staticmethod
    def get_accessory(accessory_name: Accessories):
        return accessory_name.value()


class AccessoryFlyweight:

    def __init__(self):
        self.accessories = {}

    def get_accessory(self, accessory_name: Accessories):
        try:
            return self.accessories[accessory_name]
        except KeyError:
            accessory = AccessoryFactory.get_accessory(accessory_name)

            self.accessories[accessory_name] = accessory

            return accessory

