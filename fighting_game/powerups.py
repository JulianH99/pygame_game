from fighting_game.characters import Character
from fighting_game.accessories import Accessory
from abc import ABCMeta, abstractmethod


class CharacterPowerUp(Character, metaclass=ABCMeta):
    def __init__(self, character, accessory):
        """

        :param character: character to be decorated
        :type character: Character

        :param accessory: Accessory that will be used to decorate the character
        :type accessory: Accessory
        """

        self.character = character
        self.accessory = accessory

        super().__init__(character.rect.centerx, character.rect.centery,
                         character.facing_right)

        self.name = self.character.name

        self.decorate()

    def decorate(self):
        self.attributes.speed += self.accessory.attributes.speed
        self.attributes.defense += self.accessory.attributes.defense
        self.attributes.attack += self.accessory.attributes.attack

        self.sprite_sheets[self.accessory.power_up['replace'].value] \
            = self.sprite_sheets[self.accessory.power_up['for'].value]

    def get_attributes(self):
        return self.character.get_attributes()

    def get_base_image(self):
        return self.character.get_base_image()

    def get_sprite_path(self):
        return self.character.get_sprite_path()





