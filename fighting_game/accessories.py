import pygame
from abc import abstractmethod, ABCMeta
from fighting_game.helpers.path import Path
from fighting_game.dynamics import Attributes


class Accessory(pygame.sprite.Sprite, metaclass=ABCMeta):
    def __init__(self):
        super().__init__(self)
        self.attributes = self.build_attributes
        self.sprite = self.get_sprite()

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

    def get_sprite(self):
        return Path.path_to("accessories", "Slopes.png")

    def build_attributes(self):
        return Attributes(
            speed=10,
            defense=0,
            attack=3
        )


class Toast(Accessory):

    def get_sprite(self):
        return Path.path_to("accessories", "Toast.png")

    def build_attributes(self):
        return Attributes(
            speed=5,
            defense=10,
            attack=-3
        )


class TransmutationCircle(Accessory):

    def get_sprite(self):
        return Path.path_to("accessories", "TransmutationCircle.png")

    def build_attributes(self):
        return Attributes(
            speed=10,
            defense=10,
            attack=-10
        )

