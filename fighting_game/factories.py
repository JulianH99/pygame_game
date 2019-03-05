from typing import Dict

from fighting_game.accessories import Accessory
from fighting_game.character_builder import PowerUpBuilder, CharacterBuilder, CharacterDirector
from fighting_game.characters import Character
from fighting_game.powerups import CharacterPowerUp
from fighting_game.screen import Screen, ScreenManager


class CharacterFactory:
    character_director: CharacterDirector = None

    @staticmethod
    def __check_director():
        if CharacterFactory.character_director is None:
            CharacterFactory.character_director = CharacterDirector()

    @staticmethod
    def get_character(ch_class: type) -> Character:

        CharacterFactory.__check_director()

        builder = CharacterBuilder(ch_class)

        CharacterFactory.character_director.set_builder(builder)
        CharacterFactory.character_director.construct()

        return builder.character

    @staticmethod
    def get_decorator(decorator_class: type, character: Character, accessory: Accessory) -> CharacterPowerUp:
        CharacterFactory.__check_director()

        builder = PowerUpBuilder()

        builder.create_instance(decorator_class, character, accessory)

        CharacterFactory.character_director.set_builder(builder)

        CharacterFactory.character_director.construct()

        return builder.character


class AccessoryFactory:

    @staticmethod
    def get_accessory(accss_class: type) -> Accessory:
        if accss_class is None:
            raise ValueError('[AccessoryFactory] class cannot be none')

        return accss_class()


class ScreenManagerFactory:

    @staticmethod
    def get_screen_manager(screen, screens: Dict[str, Screen]):
        screen_manager = ScreenManager(screen)

        for screen in screens.keys():
            screen_manager.add_screen(screen, screens[screen])

        return screen_manager




