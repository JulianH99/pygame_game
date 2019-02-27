import abc
import os
from fighting_game.characters import Character
from fighting_game.dynamics import SpriteSheet, MovingAnimation, FightingAnimation, ProFightingAnimation


class CharacterDirector:
    def __init__(self, character_builder):
        """
        Initializes the CharacterDirector to use a specific CharacterBuilder
        :param character_builder: The character builder to use in construction process
        :type character_builder: AbstractCharacterBuilder
        """
        self.character_builder = character_builder

    def construct(self):
        self.character_builder.build_walk_animation()
        self.character_builder.build_jump_animation()
        self.character_builder.build_defense_animation()
        self.character_builder.build_pro_defense_animation()
        self.character_builder.build_fist_animation()
        self.character_builder.build_pro_fist_animation()
        self.character_builder.build_large_attack_animation()
        self.character_builder.build_pro_large_attack_animation()
        self.character_builder.build_static_animation()

        "The method die is giving problems"
        #self.character_builder.build_die_animation()

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
    def build_walk_animation(self):
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
    def build_pro_fist_animation(self):
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
    def build_pro_large_attack_animation(self):
        """
        Builds the pro large attack animation for the character
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

    @abc.abstractmethod
    def build_pro_defense_animation(self):
        """
        Builds the pro-defense animation for the character
        :return:
        """
        pass

    @abc.abstractmethod
    def build_die_animation(self):
        """
        Builds the die animation for the character
        :return:
        """
        pass

    @abc.abstractmethod
    def build_static_animation(self):
        """
        Builds the static animation for the character
        :return:
        """
        pass


class CharacterBuilder(AbstractCharacterBuilder):

    def __init__(self, ch_class):
        super().__init__(ch_class)

        self._character: Character = ch_class()

    def build_walk_animation(self):
        base_name = self._character.name + 'Walk'

        walk_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        walk_animation.base_file_name = base_name
        walk_animation.key_name = self._character.name.lower() + '_walk'

        walk_animation.load_images()

        self._character.add_sprite_sheet(MovingAnimation.WALK.value, walk_animation)
        pass

    def build_jump_animation(self):
        base_name = self._character.name + 'Jump'

        jump_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        jump_animation.base_file_name = base_name
        jump_animation.key_name = self._character.name.lower() + '_jump'

        jump_animation.load_images()

        self._character.add_sprite_sheet(MovingAnimation.JUMP.value, jump_animation)
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

    def build_pro_fist_animation(self):
        base_name = self._character.name + 'ProFist'

        pro_fist_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        pro_fist_animation.base_file_name = base_name
        pro_fist_animation.key_name = self._character.name.lower() + '_pro_fist'

        pro_fist_animation.load_images()

        self._character.add_sprite_sheet(ProFightingAnimation.PRO_FIST.value, pro_fist_animation)
        pass

    def build_large_attack_animation(self):
        base_name = self._character.name + 'LargeAttack'

        large_attack_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        large_attack_animation.base_file_name = base_name
        large_attack_animation.key_name = self._character.name.lower() + '_largeAttack'

        large_attack_animation.load_images()

        self._character.add_sprite_sheet(FightingAnimation.LARGE_ATTACK.value, large_attack_animation)
        pass

    def build_pro_large_attack_animation(self):
        base_name = self._character.name + 'ProLargeAttack'

        pro_large_attack_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        pro_large_attack_animation.base_file_name = base_name
        pro_large_attack_animation.key_name = self._character.name.lower() + '_pro_largeAttack'

        pro_large_attack_animation.load_images()

        self._character.add_sprite_sheet(ProFightingAnimation.PRO_LARGE_ATTACK.value, pro_large_attack_animation)
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

    def build_pro_defense_animation(self):
        base_name = self._character.name + 'ProDefense'

        pro_defense_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        pro_defense_animation.base_file_name = base_name
        pro_defense_animation.key_name = self._character.name.lower() + '_pro_defense'

        pro_defense_animation.load_images()

        self._character.add_sprite_sheet(ProFightingAnimation.PRO_DEFENSE.value, pro_defense_animation)
        pass

    " FALTA AGREGAR DIE DENTRO DE LAS DINAMYCS"

    def build_die_animation(self):
        base_name = self._character.name + 'Die'

        die_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        die_animation.base_file_name = base_name
        die_animation.key_name = self._character.name.lower() + '_die'

        die_animation.load_images()

        self._character.add_sprite_sheet(FightingAnimation.DIE.value, die_animation)
        pass

    def build_static_animation(self):
        base_name = self._character.name + 'Static'

        static_animation = SpriteSheet(
            base_sprite_path=os.path.join(self._character.get_sprite_path(), base_name),
            frames=8
        )

        static_animation.base_file_name = base_name
        static_animation.key_name = self._character.name.lower() + '_static'

        static_animation.load_images()

        self._character.add_sprite_sheet(MovingAnimation.STATIC.value, static_animation)
        pass
