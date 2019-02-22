import abc
import copy
import os
from fighting_game.characters import Character
from fighting_game.dynamics import SpriteSheet, MovingAnimation, FightingAnimation


class CharacterDirector:
    def __init__(self, character_builder):
        """
        Initializes the CharacterDirector to use a specific CharacterBuilder
        :param character_builder: The character builder to use in construction process
        :type character_builder: CharacterBuilder
        """
        self.character_builder = character_builder

    def construct(self):
        self.character_builder.build_right_animation()
        self.character_builder.build_left_animation()


class AbstractCharacterBuilder(abc.ABC):

    def __init__(self, ch_class):
        self._character = None
        self.ch_class = ch_class

    @property
    def character(self):
        return self._character

    @abc.abstractmethod
    def build_right_animation(self):
        """
        Builds the right running animation for the character
        """
        pass

    @abc.abstractmethod
    def build_left_animation(self):
        """
        Build the left running animation for the character
        :return:
        """
        pass

    @abc.abstractmethod
    def build_jump_animation(self):
        """
        Builds the jump animation for the character
        :return:
        """
        pass

    @abc.abstractmethod
    def build_fist_animation(self):
        """
        Builds the fist animation for the character
        :return:
        """
        pass

    @abc.abstractmethod
    def build_large_attack_animation(self):
        """
        Builds the large attack animation for the character
        :return:
        """
        pass

    @abc.abstractmethod
    def build_defense_animation(self):
        """
        Builds the defense animation for the character
        :return:
        """
        pass


class CharacterBuilder(AbstractCharacterBuilder):

    def __init__(self, ch_class):
        super().__init__(ch_class)

        self._character: Character = ch_class()

    def build_right_animation(self):

        base_name = self._character.name + 'Right'

        right_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        right_animation.base_file_name = base_name
        right_animation.key_name = self._character.name.lower() + '_right'

        right_animation.load_images()

        self._character.add_sprite_sheet(MovingAnimation.RIGHT.value, right_animation)

    def build_left_animation(self):
        base_name = self._character.name + 'Left'

        left_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        left_animation.base_file_name = base_name
        left_animation.key_name = self._character.name.lower() + '_left'

        left_animation.load_images()

        self._character.add_sprite_sheet(MovingAnimation.LEFT.value, left_animation)

    def build_jump_animation(self):
        pass

    def build_fist_animation(self):
        pass

    def build_large_attack_animation(self):
        pass

    def build_defense_animation(self):
        pass

