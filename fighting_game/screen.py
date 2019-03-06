from abc import ABC, abstractmethod

from fighting_game.character_builder import CharacterDirector, CharacterBuilder
from fighting_game.helpers import HelpersFacade
from fighting_game.helpers.colors import RED, BRIGHT_RED
from fighting_game.characters import *
from fighting_game.dynamics import ScreenSwitcher, LifeBar


class Screen(ABC):
    def __init__(self):
        self.screen_name = ''
        self.assets = {}

        self._load_assets()

    def draw(self, screen):
        if screen is None:
            raise ValueError('screen cannot be None')

        self._render(screen)
        self._handle_event(screen)

    @abstractmethod
    def _load_assets(self):
        pass

    @abstractmethod
    def _handle_event(self, screen):
        pass

    @abstractmethod
    def _render(self, screen):
        pass


class ScreenManager:

    def __init__(self, screen):
        self.screens = {}
        self.screen = screen

    def switch(self, key: str):
        try:
            screen = self.screens[key]
            screen.draw(self.screen)
        except KeyError as err:
            print("No screen found with name {}".format(err))

    def add_screen(self, key: str, screen: Screen):
        self.screens[key] = screen


class InitialScreen(Screen):

    def _load_assets(self):
        background_image = Image.load(Path.path_to("backgrounds", "Background_Shonen_Jump.png"))

        scaled_background = Image.scale_to_window(background_image)

        self.assets['background'] = scaled_background

        text_font = pygame.font.SysFont("Comic Sans MS", 30)

        game_start = text_font.render("START GAME", True, BLACK)

        self.assets['button_text'] = game_start

    def _handle_event(self, screen):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    def _render(self, screen):
        pygame.init()
        mouse = pygame.mouse.get_pos()
        screen.blit(self.assets['background'], (0, 0))

        if 500 > mouse[0] > 200 > mouse[1] > 150:

            pygame.draw.rect(screen, RED, (200, 150, 200, 50))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.first_menu = False

                        ScreenSwitcher.get_instance().switch('characters')
        else:
            pygame.draw.rect(screen, BRIGHT_RED, (200, 150, 200, 50))

        screen.blit(self.assets['button_text'], (200, 150))


class CharacterSelectionScreen(Screen):

    def _load_assets(self):
        maid = Character.get_card_image('maid')
        bowsette = Character.get_card_image('bowsette')
        miia = Character.get_card_image('miia')
        ryuuko = Character.get_card_image('ryuuko')
        saber = Character.get_card_image('saber')
        sailor = Character.get_card_image('sailor')
        sakura = Character.get_card_image('sakura')
        virgo = Character.get_card_image('virgo')

        self.assets['characters'] = {
            'maid': maid,
            'bowsette': bowsette,
            'miia': miia,
            'ryuuko': ryuuko,
            'saber': saber,
            'sailor': sailor,
            'sakura': sakura,
            'virgo': virgo
        }

        transparent_surface = pygame.Surface(Character.card_size)  # the size of your rect
        transparent_surface.set_alpha(0)  # alpha level
        transparent_surface.fill(WHITE)
        self.assets['surface'] = transparent_surface

    def _handle_event(self, screen):
        pass

    def _update(self, screen):
        pass

    def _render(self, screen):
        self.__paint_characters(screen)
        self.mouse_event()

    def __paint_characters(self, screen):
        screen.fill(BLACK)

        screen.blit(self.assets['characters']['bowsette'], (30, 30))
        screen.blit(self.assets['surface'], (30, 30))

        screen.blit(self.assets['characters']['maid'], (30, 220))
        screen.blit(self.assets['surface'], (30, 220))

        screen.blit(self.assets['characters']['miia'], (175, 30))
        screen.blit(self.assets['surface'], (175, 30))

        screen.blit(self.assets['characters']['ryuuko'], (175, 220))
        screen.blit(self.assets['surface'], (175, 220))

        screen.blit(self.assets['characters']['saber'], (320, 30))
        screen.blit(self.assets['surface'], (320, 30))

        screen.blit(self.assets['characters']['sailor'], (320, 220))
        screen.blit(self.assets['surface'], (320, 220))

        screen.blit(self.assets['characters']['sakura'], (465, 30))
        screen.blit(self.assets['surface'], (465, 30))

        screen.blit(self.assets['characters']['virgo'], (465, 220))
        screen.blit(self.assets['surface'], (465, 220))

    def mouse_event(self):
        selection = ""
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if 30 + 150 > mouse[0] > 30 and 30 + 100 > mouse[1] > 30:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Bowsette")
                        selection = "Bowsette"
            elif 30 + 150 > mouse[0] > 50 and 220 + 100 > mouse[1] > 220:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Maid")
                        selection = "Maid"
            elif 175 + 150 > mouse[0] > 175 and 30 + 100 > mouse[1] > 30:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Miia")
                        selection = "Miia"
            elif 175 + 150 > mouse[0] > 175 and 220 + 100 > mouse[1] > 220:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Ryuuko")
                        selection = "Ryuuko"
            elif 320 + 150 > mouse[0] > 320 and 30 + 100 > mouse[1] > 30:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Saber")
                        selection = "Saber"
            elif 320 + 150 > mouse[0] > 320 and 220 + 100 > mouse[1] > 220:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Sailor")
                        selection = "Sailor"
            elif 465 + 150 > mouse[0] > 465 and 30 + 100 > mouse[1] > 30:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Sakura")
                        selection = "Sakura"
            elif 465 + 150 > mouse[0] > 465 and 220 + 100 > mouse[1] > 220:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Virgo")
                        selection = "Virgo"
            if event == pygame.QUIT:
                pygame.quit()

        return selection


class FightingScreen(Screen):
    is_jump = False

    def _load_assets(self):
        background = Image.load(Path.path_to("backgrounds", "BackgroundFairyTail.png"))
        self.assets['background'] = Image.scale_to_window(background)

        total_sprites = pygame.sprite.Group()
        character_builder = CharacterBuilder(Maid)
        character_director = CharacterDirector()
        character_director.set_builder(character_builder)

        character_director.construct()
        maid = character_builder.character

        print(maid)
        # another_maid = character_builder.character
        life_bar = LifeBar(maid)
        # enemy_life_bar = LifeBar(screen, another_maid)
        total_sprites.add(maid)

        maid.set_x_y((10, HelpersFacade.screen.GROUND_AREA_Y))

        self.assets['sprites'] = total_sprites
        self.assets['player_1'] = maid
        self.assets['player_1_life'] = life_bar

    def _handle_event(self, screen):
        pass

    def _render(self, screen):
        maid = self.assets['player_1']

        sprites = self.assets['sprites']

        life_bar = self.assets['player_1_life']

        screen.blit(self.assets['background'], (0, 0))
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_a]:
            maid.trigger_animation(MovingAnimation.WALK)
            maid.change_direction(False)
        elif key_pressed[pygame.K_d]:
            maid.trigger_animation(MovingAnimation.WALK)
            maid.change_direction(True)
        elif key_pressed[pygame.K_s]:
            maid.trigger_animation(FightingAnimation.DEFENSE)
        elif key_pressed[pygame.K_g]:
            maid.trigger_animation(FightingAnimation.FIST)
            # maid.collision_with_char(another_maid)
        elif key_pressed[pygame.K_h]:
            maid.trigger_animation(FightingAnimation.LARGE_ATTACK)
        elif key_pressed[pygame.K_w]:
            self.is_jump = True

        if self.is_jump:
            self.is_jump = maid.trigger_animation(MovingAnimation.JUMP)

        print(maid.rect.centerx)


        # if key_pressed[pygame.K_LEFT]:
        #     another_maid.trigger_animation(MovingAnimation.WALK)
        #     another_maid.change_direction(False)
        # elif key_pressed[pygame.K_RIGHT]:
        #     another_maid.trigger_animation(MovingAnimation.WALK)
        #     another_maid.change_direction(True)
        # elif key_pressed[pygame.K_DOWN]:
        #     another_maid.trigger_animation(FightingAnimation.DEFENSE)
        # elif key_pressed[pygame.K_k]:
        #     another_maid.trigger_animation(FightingAnimation.FIST)
        #     another_maid.collision_with_char(maid)
        # elif key_pressed[pygame.K_l]:
        #     another_maid.trigger_animation(FightingAnimation.LARGE_ATTACK)
        # elif key_pressed[pygame.K_UP]:
        #     another_maid.trigger_animation(MovingAnimation.JUMP)
        sprites.update()
        sprites.draw(screen)

        life_bar.draw(screen)

        self.assets['player_1'] = maid
        self.assets['player_1_life'] = life_bar
