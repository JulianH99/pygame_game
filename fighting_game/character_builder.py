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
        :type character_builder: AbstractCharacterBuilder
        """
        self.character_builder = character_builder

    def construct(self):
        self.character_builder.build_right_animation()
        self.character_builder.build_left_animation()
        self.character_builder.build_defense_animation()
        self.character_builder.build_fist_animation()
        self.character_builder.build_large_attack_animation()

    def set_builder(self, character_builder):
        """
        Changes the base builder of the director
        :param character_builder: builder to be used
        :type character_builder: AbstractCharacterBuilder
        """
        self.character_builder = character_builder


class AbstractCharacterBuilder(abc.ABC):

    def __init__(self, ch_class):
        self._character = None
        self.ch_class = ch_class

    @property
    def character(self):
        return self._character

    def change_class(self, ch_class):
        self.ch_class = ch_class
        self._character = ch_class()

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
        base_name = self._character.name + 'Fist'

        fist_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        fist_animation.base_file_name = base_name
        fist_animation.key_name = self._character.name.lower() + '_fist'

        fist_animation.load_images()

        self._character.add_sprite_sheet(FightingAnimation.FIST.value, fist_animation)
        pass

    def build_large_attack_animation(self):
        base_name = self._character.name + 'LargeAttack'

        largeAttack_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        largeAttack_animation.base_file_name = base_name
        largeAttack_animation.key_name = self._character.name.lower() + '_largeAttack'

        largeAttack_animation.load_images()

        self._character.add_sprite_sheet(FightingAnimation.LARGE_ATTACK.value, largeAttack_animation)
        pass

    def build_defense_animation(self):
        base_name = self._character.name + 'Defense'

        defense_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        defense_animation.base_file_name = base_name
        defense_animation.key_name = self._character.name.lower() + '_defense'

        defense_animation.load_images()

        self._character.add_sprite_sheet(FightingAnimation.DEFENSE.value, defense_animation)
        pass

