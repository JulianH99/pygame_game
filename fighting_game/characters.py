import pygame
import os
from abc import abstractmethod
from typing import Dict
from fighting_game.helpers.colors import BLACK, WHITE
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path
from fighting_game.dynamics import SpriteSheet, MovingAnimation, FightingAnimation, ProFightingAnimation
from fighting_game.helpers.screen import SCREEN_WIDTH, SCREEN_HEIGHT
from typing import Tuple


class Character(pygame.sprite.Sprite):
    """
    Represents the basic character that the user will see in screen
    """
    width = 64
    height = 64

    card_size = (150, 300)
  
    def __init__(self, x=0, y=0, *groups, facing_right=True):
        super().__init__(*groups)

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

        self.facing_right = True
        self.flipped = False

        self.playing_animation: SpriteSheet = None
        self.animation_step = 0
        self.current_index = 0

        self.is_collision = False
        # Creation of the Hitbox
        self.hitbox = (self.x + 20, self.y, 28, 60)
        win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        background = Image.load(Path.path_to("backgrounds", "BackgroundFairyTail.png"))
        scaled_background = Image.scale_to_window(background)
        win.blit(scaled_background, (0, 0))

        self.win = win

    @abstractmethod
    def get_base_image(self):
        pass

    @abstractmethod
    def get_sprite_path(self):
        pass

    @staticmethod
    def get_card_image(name: str):
        image = Image.load(Path.path_to("profile", "{}_character.png".format(name.lower())))

        return pygame.transform.scale(image, Character.card_size)

    def set_x_y(self, x_y):
        """
        Sets the position of the character in screen
        :param x_y: Tuple with two integers, representing the position in two axes
        :type x_y: Tuple[int, int]
        """

        self.rect.centery = x_y[1]
        self.rect.centerx = x_y[0]

    def change_direction(self, direction):
        """
        Changes the direction of the sprite
        :param direction:
        :return:
        """

        self.facing_right = direction

        if self.facing_right and self.flipped:
            self.unflip()
        elif not self.facing_right and not self.flipped:
            self.flip()

    def __perform_flip(self):
        for sprite_sheet in self.sprite_sheets.values():
            sprite_sheet.perform_flip()

    def flip(self):
        print("flipping")
        self.__perform_flip()
        self.flipped = True

    def unflip(self):
        print("unflipping")
        self.__perform_flip()
        self.flipped = False

    def add_sprite_sheet(self, key: str, sprite_sheet: SpriteSheet):
        if key in self.sprite_sheets:
            raise KeyError("{} is already defined".format(key))
        self.sprite_sheets[key] = sprite_sheet

    def trigger_animation(self, animation):
        """
        Triggers an animation in the character
        :param animation: animation to be triggered
        :raises: KeyError

        """
        if isinstance(animation, MovingAnimation) or \
                isinstance(animation, FightingAnimation) or \
                isinstance(animation, ProFightingAnimation):

            try:
                self.playing_animation = self.sprite_sheets[animation.value]

                if animation == MovingAnimation.WALK:
                    if not self.facing_right:
                        self.trigger_left()
                    else:
                        self.trigger_right()

            except KeyError:
                print("The requested animation {} does not exists".format(animation.value))
        else:
            raise ValueError('animation should be a valid Animation type')

    def trigger_left(self):
        if self.rect.left > 0:
            self.rect.centerx -= self.speed

    def trigger_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.centerx += self.speed

    def update(self, *args):

        if self.playing_animation:

            if self.current_index < len(self.playing_animation.images):
                self.image = self.playing_animation.images[self.current_index]
                self.current_index += 1

            else:
                self.current_index = 0
                self.playing_animation = None

    def collision_with_char(self, character):
        """
        Checks if there's a collision between characters
        :param character: character to check collision on
        :type character: Character
        """
        collision = pygame.sprite.collide_rect(self, character)

        if collision:
            print("collided")
        self.is_collision = collision


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


class Miia(Character):

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.name = 'Miia'

    def get_base_image(self):
        return Image.load(os.path.join(self.path, "MiiaBasicModel.png"))

    def get_sprite_path(self):
        return Path.path_to("sprite_sheets", "Miia")


class Ryyuko(Character):

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.name = 'Ryuuko'

    def get_base_image(self):
        return Image.load(os.path.join(self.path, "RyuukoBasicModel.png"))

    def get_sprite_path(self):
        return Path.path_to("sprite_sheets", "Ryuuko")


class Saber(Character):

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.name = 'Saber'

    def get_base_image(self):
        return Image.load(os.path.join(self.path, "SaberBasicModel.png"))

    def get_sprite_path(self):
        return Path.path_to("sprite_sheets", "Saber")


class Sailor(Character):

    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.name = 'Sailor'

    def get_base_image(self):
        return Image.load(os.path.join(self.path, "SailorBasicModel.png"))

    def get_sprite_path(self):
        return Path.path_to("sprite_sheets", "Sailor")


class Sakura(Character):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.name = 'Sakura'

    def get_base_image(self):
        return Image.load(os.path.join(self.path, "SakuraBasicModel.png"))

    def get_sprite_path(self):
        return Path.path_to("sprite_sheets", "Sakura")


class Virgo(Character):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.name = 'Virgo'

    def get_base_image(self):
        return Image.load(os.path.join(self.path, "VirgoBasicModel.png"))

    def get_sprite_path(self):
        return Path.path_to("sprite_sheets", "Virgo")
