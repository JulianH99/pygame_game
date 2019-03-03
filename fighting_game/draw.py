import pygame
from fighting_game.helpers.screen import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_AREA_Y
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path
from fighting_game.helpers.colors import *

pygame.init()

# Window Settings
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = Image.load(Path.path_to("backgrounds", "BackgroundFairyTail.png"))
background_menu = Image.load(Path.path_to("backgrounds", "Background_Shonen_Jump.png"))
background_character = Image.load(Path.path_to("backgrounds", "BackgroundNeoTokyo.png"))

scaled_background_character = Image.scale_to_window(background_character)
scaled_background_menu = Image.scale_to_window(background_menu)
scaled_background = Image.scale_to_window(background)

# Fonts
title_font = pygame.font.SysFont("Comic Sans MS", 50)
text_font = pygame.font.SysFont("Comic Sans MS", 30)
game_start = text_font.render("START GAME", True, BLACK)

# Clock
clock = pygame.time.Clock()


# Characters_profiles_preloads
bowsette_load = Image.load(Path.path_to("profile", "bowsette_character.png"))
bowsette = pygame.transform.scale(bowsette_load, (50, 200))
maid_load = Image.load(Path.path_to("profile", "maid_character.png"))
maid = pygame.transform.scale(maid_load, (150, 200))
miia_load = Image.load(Path.path_to("profile", "miia_character.png"))
miia = pygame.transform.scale(miia_load, (150, 200))
ryuuko_load = Image.load(Path.path_to("profile", "ryuuko_character.png"))
ryuuko = pygame.transform.scale(ryuuko_load, (150, 200))
saber_load = Image.load(Path.path_to("profile", "saber_character.png"))
saber = pygame.transform.scale(saber_load, (150, 200))
sailor_load = Image.load(Path.path_to("profile", "sailor_character.png"))
sailor = pygame.transform.scale(sailor_load, (150, 200))
sakura_load = Image.load(Path.path_to("profile", "sakura_character.png"))
sakura = pygame.transform.scale(sakura_load, (150, 200))
virgo_load = Image.load(Path.path_to("profile", "virgo_character.png"))
virgo = pygame.transform.scale(virgo_load, (150, 200))

# Transparent Surface
transparentSurface = pygame.Surface((150,200))  # the size of your rect
transparentSurface.set_alpha(0)                # alpha level
transparentSurface.fill((255,255,255))           # this fills the entire surface


class Redraw:
    character_menu = True
    first_menu = True

    def print_character(self):

        win.fill(BLACK)

        win.blit(bowsette, (50, 60))
        win.blit(transparentSurface, (50, 60))

        win.blit(maid, (50, 320))
        win.blit(transparentSurface, (50, 320))

        win.blit(miia, (240, 60))
        win.blit(transparentSurface, (240, 60))

        win.blit(ryuuko, (240, 320))
        win.blit(transparentSurface, (240, 320))

        win.blit(saber, (430, 60))
        win.blit(transparentSurface, (430, 60))

        win.blit(sailor, (430, 320))
        win.blit(transparentSurface, (430, 320))

        win.blit(sakura, (620, 60))
        win.blit(transparentSurface, (620, 60))

        win.blit(virgo, (620, 320))
        win.blit(transparentSurface, (620, 320))

    def main_menu(self):
        mouse = pygame.mouse.get_pos()

        win.blit(scaled_background_menu, (0, 0))

        if 500 > mouse[0] > 300 > mouse[1] > 250:

            pygame.draw.rect(win, RED, (300, 250, 200, 50))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.first_menu = False
        else:
            pygame.draw.rect(win, BRIGHT_RED, (300, 250, 200, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.blit(game_start, (300, 250))
        pygame.display.flip()

    def selection_character(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if 30 + 150 > mouse[0] > 30 and 30 + 100 > mouse[1] > 30:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Bowsette")
                        self.character_menu = False

            elif 50 + 200 > mouse[0] > 50 and 320 + 150 > mouse[1] > 320:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Maid")
                        self.character_menu = False

            elif 240 + 200 > mouse[0] > 240 and 60 + 150 > mouse[1] > 60:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Miia")
                        self.character_menu = False
            elif 240 + 200 > mouse[0] > 240 and 320 + 150 > mouse[1] > 320:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Ryuuko")
                        self.character_menu = False

            elif 430 + 200 > mouse[0] > 430 and 60 + 150 > mouse[1] > 60:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Saber")
                        self.character_menu = False

            elif 430 + 200 > mouse[0] > 430 and 320 + 150 > mouse[1] > 320:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Sailor")
                        self.character_menu = False

            elif 620 + 200 > mouse[0] > 620 and 60 + 150 > mouse[1] > 60:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Sakura")
                        self.character_menu = False

            elif 620 + 200 > mouse[0] > 620 and 320 + 150 > mouse[1] > 320:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Selected Virgo")
                        self.character_menu = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()

    def draw(self, sprites):

        if self.first_menu:
            self.main_menu()

        elif self.character_menu:

            self.print_character()
            self.selection_character()

        else:
            win.blit(scaled_background, (0, 0))

            sprites.update()

            sprites.draw(win)

            pygame.display.flip()

            clock.tick(27)
