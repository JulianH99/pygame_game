import random
from abc import ABC, abstractmethod

from fighting_game.accessories import *
from fighting_game.character_builder import CharacterDirector, CharacterBuilder
from fighting_game.helpers import HelpersFacade
from fighting_game.helpers.colors import RED, BRIGHT_RED
from abc import ABC
from fighting_game.accessories import AccessoryFlyweight
from fighting_game.character_factory import CharacterFactory
from fighting_game.characters import *
from fighting_game.dynamics import Player, UsePlayer
from fighting_game.dynamics import ScreenSwitcher, LifeBar
from fighting_game.helpers import HelpersFacade
from fighting_game.helpers.colors import RED, BRIGHT_RED


class Screen(ABC):
    def __init__(self):
        self.screen_name = ''
        self.assets = {}
        self.players = []

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
                        print("Menu oculto")
                        # self.first_menu = False

                        ScreenSwitcher.get_instance().switch('characters')
        else:
            pygame.draw.rect(screen, BRIGHT_RED, (200, 150, 200, 50))

        key = pygame.key.get_pressed()

        if key == pygame.K_SPACE:
            print("Space")
            ScreenSwitcher.get_instance().switch('characters')

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def _update(self, screen):
        pass

    def _render(self, screen):
        self.__paint_characters(screen)
        self.mouse_event()

    def selection(self):
        ScreenSwitcher.get_instance().switch('fight')

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
                        selection = Bowsette
                        self.manage_selection(selection)

            elif 30 + 150 > mouse[0] > 50 and 220 + 100 > mouse[1] > 220:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Maid")
                        selection = Maid
                        self.manage_selection(selection)

            elif 175 + 150 > mouse[0] > 175 and 30 + 100 > mouse[1] > 30:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Miia")
                        selection = Miia
                        self.manage_selection(selection)

            elif 175 + 150 > mouse[0] > 175 and 220 + 100 > mouse[1] > 220:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Ryuuko")
                        selection = Ryyuko
                        self.manage_selection(selection)

            elif 320 + 150 > mouse[0] > 320 and 30 + 100 > mouse[1] > 30:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Saber")
                        selection = Saber
                        self.manage_selection(selection)

            elif 320 + 150 > mouse[0] > 320 and 220 + 100 > mouse[1] > 220:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Sailor")
                        selection = Sailor
                        self.manage_selection(selection)

            elif 465 + 150 > mouse[0] > 465 and 30 + 100 > mouse[1] > 30:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Sakura")
                        selection = Sakura
                        self.manage_selection(selection)

            elif 465 + 150 > mouse[0] > 465 and 220 + 100 > mouse[1] > 220:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Virgo")
                        selection = Virgo
                        self.manage_selection(selection)

    def manage_selection(self, selection):
        player = Player()
        use_player = UsePlayer()
        player.set_player(selection)

        if len(self.players) <= 1:
            self.players.append(player)
            print(len(self.players))
            player.get_player()

        if len(self.players) == 2:
            print("should switch")
            use_player.set_player_1(self.players[0])
            use_player.set_player_2(self.players[1])
            ScreenSwitcher.get_instance().switch('fight')


class FightingScreen(Screen):
    is_jump_player_1 = False
    is_jump_player_2 = False

    def _load_assets(self):
        background = Image.load(Path.path_to("backgrounds", "BackgroundFairyTail.png"))
        self.assets['background'] = Image.scale_to_window(background)

        self.assets['accessory_fl'] = AccessoryFlyweight()

        self.assets['accessory_group'] = pygame.sprite.Group()
        total_sprites = pygame.sprite.Group()

        # player_2 = character_builder.character

        self.assets['sprites'] = total_sprites
        self.assets['player_1'] = None
        self.assets['player_2'] = None
        self.assets['player_1_life'] = None
        self.assets['player_2_life'] = None

    def _handle_event(self, screen):
        pass

    def _render(self, screen):
        pygame.init()

        self._load_characters()

        screen.blit(self.assets['background'], (0, 0))
        player_1 = self.assets['player_1']
        player_2 = self.assets['player_2']

        sprites = self.assets['sprites']

        life_bar = self.assets['player_1_life']
        
        life_bar_2 = self.assets['player_2_life']

        accessory = any
        type = random.randint(1, 600)
        position = random.randint(1, HelpersFacade.screen.SCREEN_WIDTH)
        if type == 200:
            accessory = self.assets['accessory_fl'].get_accessory(Accessories.slopes)
            print('1')
        elif type == 400:
            accessory = self.assets['accessory_fl'].get_accessory(Accessories.toast)
            print("2")
        elif type == 590:
            accessory = self.assets['accessory_fl'].get_accessory(Accessories.transmutation_circle)
            print('3')
        if accessory != any:
            accessory.set_x(position)
            self.assets['accessory_group'].add(accessory)
        screen.blit(self.assets['background'], (0, 0))

        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_a]:
            player_1.trigger_animation(MovingAnimation.WALK)
            player_1.change_direction(False)
        if key_pressed[pygame.K_d]:
            player_1.trigger_animation(MovingAnimation.WALK)
            player_1.change_direction(True)
        if key_pressed[pygame.K_s]:
            player_1.trigger_animation(FightingAnimation.DEFENSE)
        if key_pressed[pygame.K_g]:
            player_1.trigger_animation(FightingAnimation.FIST)
            player_1.collision_with_char(player_2)
        if key_pressed[pygame.K_h]:
            player_1.trigger_animation(FightingAnimation.LARGE_ATTACK)
            player_1.collision_with_char(player_2)
        if key_pressed[pygame.K_w]:
            self.is_jump_player_1 = True

        if self.is_jump_player_1:
            self.is_jump_player_1 = player_1.trigger_animation(MovingAnimation.JUMP)

        self.assets['accessory_group'].draw(screen)

        if key_pressed[pygame.K_LEFT]:
            player_2.trigger_animation(MovingAnimation.WALK)
            player_2.change_direction(False)
        if key_pressed[pygame.K_RIGHT]:
            player_2.trigger_animation(MovingAnimation.WALK)
            player_2.change_direction(True)
        if key_pressed[pygame.K_DOWN]:
            player_2.trigger_animation(FightingAnimation.DEFENSE)
        if key_pressed[pygame.K_k]:
            player_2.trigger_animation(FightingAnimation.FIST)
            player_2.collision_with_char(player_1)
        if key_pressed[pygame.K_l]:
            player_2.trigger_animation(FightingAnimation.LARGE_ATTACK)
            player_2.collision_with_char(player_1)
        if key_pressed[pygame.K_UP]:
            player_2.trigger_animation(MovingAnimation.JUMP)
            self.is_jump_player_2 = True
        if self.is_jump_player_2:
            self.is_jump_player_2 = player_2.trigger_animation(MovingAnimation.JUMP)

        if player_2.dead:
            sprites.remove(player_2)

        if player_1.dead:
            sprites.remove(player_1)
            
        sprites.update()
        sprites.draw(screen)

        life_bar.draw(screen)
        
        life_bar_2.draw(screen)

    def _load_characters(self):
        if self.assets['player_1'] is None and self.assets['player_2'] is None:
            use_player = UsePlayer()

            player_1 = CharacterFactory.get_character(use_player.player1.player)
            player_2 = CharacterFactory.get_character(use_player.player2.player)

            player_1.set_x_y((10, HelpersFacade.screen.GROUND_AREA_Y))
            player_2.set_x_y((HelpersFacade.screen.SCREEN_WIDTH - 10, HelpersFacade.screen.GROUND_AREA_Y))

            self.assets['player_1'] = player_1
            self.assets['player_2'] = player_2

            self.assets['player_1_life'] = LifeBar(player_1)
            self.assets['player_2_life'] = LifeBar(player_2, index=2)

            self.assets['sprites'].add(player_1)
            self.assets['sprites'].add(player_2)


class ScreenManagerFactory:

    @staticmethod
    def get_screen_manager(screen, screens: Dict[str, Screen]):
        screen_manager = ScreenManager(screen)

        for screen in screens.keys():
            screen_manager.add_screen(screen, screens[screen])

        return screen_manager
