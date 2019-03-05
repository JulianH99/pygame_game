import pygame
from fighting_game.helpers import HelpersFacade
from fighting_game.screen import ScreenManager
from fighting_game.dynamics import ScreenSwitcherSubject


class Game(ScreenSwitcherSubject):

    def __init__(self):

        self.clock = pygame.time.Clock()

        pygame.display.set_caption("TEST GAME")

        self.screen = pygame.display.set_mode((HelpersFacade.screen.SCREEN_WIDTH,
                                               HelpersFacade.screen.SCREEN_HEIGHT))

        self.screen_manager: ScreenManager = None

        self.done = False

    def set_screen_manager(self, screen_manager: ScreenManager):
        self.screen_manager = screen_manager

    def on_switch(self, screen_key: str):
        pygame.init()
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            self.screen_manager.switch(screen_key)

            pygame.display.flip()

            self.clock.tick(27)
        pygame.quit()


