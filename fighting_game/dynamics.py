import pygame
from enum import Enum
from typing import List
from fighting_game.helpers.image import Image
from fighting_game.helpers.colors import BLACK, GREEN, WHITE, BLUE
from fighting_game.helpers import font
from abc import ABC, abstractmethod
import os
from fighting_game.helpers.screen import SCREEN_WIDTH
import math


class MovingAnimation(Enum):
    """
    Animation types for making common strings to access moving sprite sheets
    """
    WALK = 'walk'
    JUMP = 'jump'
    STATIC = 'static'

    def __str__(self):
        return self.value


class FightingAnimation(Enum):
    """
    Animation types for common access to fighting movements
    """
    FIST = 'fist'
    DEFENSE = 'defense'
    LARGE_ATTACK = 'large_attack'
    DIE = 'die'


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
        self.images: List[pygame.Surface] = []

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

    def perform_flip(self):
        animation = self.images[:]

        animation.clear()

        for image in self.images:
            animation.append(
                pygame.transform.flip(image, True, False)
            )

        self.images = animation


class Attributes:
    """
    Class used to manage character attributes
    :version: 1
    """
    def __init__(self, attack, speed, defense):

        attributes = [attack, speed, defense]

        for attr in attributes:
            if attr < 0 or attr > 100:
                raise ValueError('Any of the attributes can be less than 0 or greater than 100')

        self.speed = speed
        self.defense = defense
        self.attack = attack


class AIWrapper:
    def __init__(self):
        self.char_around = None
        self.char_to = None

    def wrap_around(self, character):
        """
        Sets the character that's going to be handled by the AI
        :param character: Character to be wrapped
        :type character: Character
        """
        self.char_around = character

    def follow(self, character):
        """
        Sets the character that will be taken as reference to perform actions in the AI
        :param character:
        :type character: Character
        """
        self.char_to = character


class LifeBar:
    def __init__(self, screen, character, index=1):
        """
        Initializes the life bar
        :param screen: pygame Screen surface
        :type screen: Surface
        :param character: Character that will be used to display the life bar
        :type character: Character
        """

        self.character = character
        self.screen = screen
        self.width = math.floor((SCREEN_WIDTH / 2) - 50)
        self.inner_width = self.width - 5
        self.life_points = character.life_points
        self.name = font.render(character.name, False, WHITE)

        if index == 1:
            rect_positions = (20, 20)
            inner_rect_positions = (25, 25)
        else:
            rect_positions = (SCREEN_WIDTH - self.inner_width - 25, 20)
            inner_rect_positions = (SCREEN_WIDTH - self.inner_width - 20, 25)

        self.inner_rect_positions = inner_rect_positions

        self.outer_rect = pygame.Rect(rect_positions[0], rect_positions[1], self.width + 5, 30)
        self.inner_rect = self.build_life_bar_rect()

    def draw(self):
        self.calculate()
        pygame.draw.rect(self.screen, BLUE, self.outer_rect)
        if self.inner_width > 0:
            pygame.draw.rect(self.screen, GREEN, self.inner_rect)
        self.screen.blit(self.name, self.inner_rect_positions)

    def calculate(self):

        if self.character.life_points <= 0:
            self.inner_width = 0
        else:
            self.inner_width = math.floor((self.character.life_points * (self.width - 5)) / 100)
        self.inner_rect = self.build_life_bar_rect()

    def build_life_bar_rect(self):
        return pygame.Rect(self.inner_rect_positions[0], self.inner_rect_positions[1],
                           self.inner_width, 20)


class ScreenSwitcherSubject(ABC):
    @abstractmethod
    def on_switch(self, screen_key: str):
        pass


class ScreenSwitcher:
    """
    Mediator class to communicate the screens with the screen manager
    """

    __instance = None

    def __init__(self):
        self.observers: List[ScreenSwitcherSubject] = []

    def attach(self, observer: ScreenSwitcherSubject):
        self.observers.append(observer)

    def switch(self, screen_key: str):
        for observer in self.observers:
            observer.on_switch(screen_key)

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = ScreenSwitcher()
        return cls.__instance


class Player:

    def __init__(self):
        self.player = None

    def setPlayer(self, player):
        self.player = player

    def getPlayer(self):
        print(self.player)
        return self.player


class UsePlayer:
    player1 = None
    player2 = None

    class __UsePlayer:
        def __init__(self):
            self.player1 = None
            self.player2 = None

        def setPlayer1(self, player1):
            self.player1 = player1

        def setPlayer2(self, player2):
            self.player2 = player2

    instance = None

    def __new__(self):
        UsePlayer.instance = UsePlayer.__UsePlayer()
        return UsePlayer.instance

    def setPlayer1(self,player1):
        self.instance.player1 = player1

    def setPlayer2(self,player2):
        self.instance.player2 = player2
