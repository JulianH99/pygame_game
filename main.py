import pygame

from fighting_game.dynamics import ScreenSwitcher
from fighting_game.game import Game
from fighting_game.screen import CharacterSelectionScreen, InitialScreen, FightingScreen, ScreenManagerFactory

screen_switcher = ScreenSwitcher.get_instance()

game = Game()

screen_switcher.attach(game)


initial_screen = InitialScreen()
characters_screen = CharacterSelectionScreen()
fighting_screen = FightingScreen()

screen_manager = ScreenManagerFactory.get_screen_manager(game.screen, {
    "initial": initial_screen,
    "characters": characters_screen,
    "fight": fighting_screen
})

game.set_screen_manager(screen_manager)


game.on_switch('initial')
