from abc import ABC, abstractmethod
from fighting_game.helpers.colors import RED, BRIGHT_RED
from fighting_game.characters import *
from fighting_game.dynamics import ScreenSwitcher


class Screen(ABC):
    def __init__(self):
        self.screen_name = ''
        self.assets = {}

    def draw(self, screen):
        if screen is None:
            raise ValueError('screen cannot be None')

        self._load_assets()
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
        print("rendering but not rendering")
        screen.blit(self.assets['background'], (0, 0))

        if 500 > mouse[0] > 300 > mouse[1] > 250:

            pygame.draw.rect(screen, RED, (300, 250, 200, 50))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.first_menu = False

                        ScreenSwitcher.get_instance().switch('characters')
        else:
            pygame.draw.rect(screen, BRIGHT_RED, (300, 250, 200, 50))
        screen.blit(self.assets['button_text'], (300, 250))


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

        background_character = Image.load(Path.path_to("backgrounds", "BackgroundNeoTokyo.png"))

        scaled_background = Image.scale_to_window(background_character)

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

        self.assets['background'] = scaled_background

        transparent_surface = pygame.Surface(Character.card_size)  # the size of your rect
        transparent_surface.set_alpha(0)  # alpha level
        transparent_surface.fill(WHITE)
        
        self.assets['surface'] = transparent_surface

    def _handle_event(self, screen):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if 30 + 150 > mouse[0] > 30 and 30 + 100 > mouse[1] > 30:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Bowsette")

            elif 30 + 150 > mouse[0] > 50 and 220 + 100 > mouse[1] > 220:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Maid")

            elif 175 + 150 > mouse[0] > 175 and 30 + 100 > mouse[1] > 30:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Miia")

            elif 175 + 150 > mouse[0] > 175 and 220 + 100 > mouse[1] > 220:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Ryuuko")

            elif 320 + 150 > mouse[0] > 320 and 30 + 100 > mouse[1] > 30:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Saber")

            elif 320 + 150 > mouse[0] > 320 and 220 + 100 > mouse[1] > 220:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Sailor")

            elif 465 + 150 > mouse[0] > 465 and 30 + 100 > mouse[1] > 30:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Sakura")

            elif 465 + 150 > mouse[0] > 465 and 220 + 100 > mouse[1] > 220:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Virgo")

            elif event.type == pygame.QUIT:
                pygame.quit()

    def _render(self, screen):
        pygame.init()
        self.__paint_characters(screen)

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


class FightingScreen(Screen):

    def _load_assets(self):
        background = Image.load(Path.path_to("backgrounds", "BackgroundFairyTail.png"))
        self.assets['background'] = Image.scale_to_window(background)

    def _handle_event(self, screen):
        pass

    def _render(self, screen):
        pygame.init()
        screen.blit(self.assets['background'], (0, 0))
