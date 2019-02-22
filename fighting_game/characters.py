import pygame
import os
from abc import abstractmethod
import time
from typing import Dict
from fighting_game.helpers.colors import *
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path
from fighting_game.sprite_sheet import SpriteSheet
from fighting_game.helpers.screen import SCREEN_WIDTH

screen = pygame.display.set_mode([800, 400])
background = pygame.image.load('./assets/sprites/Backgrounds/BackgroundFairyTail.png').convert()


class Character(pygame.sprite.Sprite):
    width = 64
    height = 64

    def __init__(self, x=0, y=0):
        super().__init__()

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

    def draw(self):
        pygame.draw.rect(self.image, WHITE, [100, 100, self.width, self.height])

    def add_sprite_sheet(self, key: str, sprite_sheet: SpriteSheet):
        if key in self.sprite_sheets:
            raise KeyError("{} is already defined".format(key))
        self.sprite_sheets[key] = sprite_sheet

    def handle_keydown(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.rect.centerx >= 0:
            self.rect.centerx -= self.speed
            self.playing_animation = self.sprite_sheets['left']

        elif key[pygame.K_RIGHT] and self.rect.centerx <= SCREEN_WIDTH:
            self.rect.centerx += self.speed
            self.playing_animation = self.sprite_sheets['right']

        elif key[pygame.K_DOWN]:
            self.playing_animation = self.sprite_sheets['defense']

        if key[pygame.K_UP]:
            self.states['jump'] = True

    def update(self, *args):
        if self.playing_animation:
            if self.current_index < len(self.playing_animation.images):
                self.image = self.playing_animation.images[self.current_index]
                self.current_index += 1
            else:
                self.current_index = 0
                self.playing_animation = None




        # if self.jumping:
        #     if self.force > 0:
        #         F = (0.4 * self.mass * (self.force*self.force))
        #     else:
        #         F = -(0.4 * self.mass * (self.force*self.force))
        #
        #     self.rect.centery = self.rect.centery - F
        #
        #     self.force -= 1
        #
        # if self.rect.centery >= 360:
        #     self.rect.centery = 360
        #     self.jumping = False
        #     self.force = 8
        pass


class Maid(Character):

    def __init__(self, x, y):
        super().__init__(x, y)

    def get_base_image(self):
        return Image.load(os.path.join(self.path, "MaidBasicModel.png"))

    def get_sprite_path(self):
        return Path.path_to("sprite_sheets", "RealMaid")
