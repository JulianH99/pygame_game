import pygame
from fighting_game.helpers.screen import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_AREA_Y
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path

pygame.init()

# Window Settings
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = Image.load(Path.path_to("backgrounds", "BackgroundFairyTail.png"))
background_menu = Image.load(Path.path_to("backgrounds", "Background_Shonen_Jump.png"))
background_character = Image.load(Path.path_to("backgrounds", "BackgroundNeoTokyo.png"))

scaled_background_character = Image.scale_to_window(background_character)
scaled_background_menu = Image.scale_to_window(background_menu)
scaled_background = Image.scale_to_window(background)

# Colors
black = (0,0,0)
white = (255, 255, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)

# Fonts
title_font = pygame.font.SysFont("Comic Sans MS", 50)
text_font = pygame.font.SysFont("Comic Sans MS", 30)
game_start = text_font.render("START GAME", True, black)

# Clock
clock = pygame.time.Clock()


# Characters_profiles_preloads
bowsette_load = Image.load(Path.path_to("profile", "bowsette_character.png"))
bowsette = pygame.transform.scale(bowsette_load, (150, 200))
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
transparentSurface.set_alpha(128)                # alpha level
transparentSurface.fill((255,255,255))           # this fills the entire surface

class redraw():
    character_menu = True
    first_menu = True

    def draw(self, sprites):

        if self.first_menu:

            mouse = pygame.mouse.get_pos()

            win.blit(scaled_background_menu, (0, 0))

            if 300 + 200 > mouse[0] > 300 and 250 + 50 > mouse[1] > 250:

                pygame.draw.rect(win, red, (300, 250, 200, 50))

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.first_menu = False
            else:
                pygame.draw.rect(win, bright_red, (300, 250, 200, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            win.blit(game_start, (300, 250))
            pygame.display.flip()

        elif self.character_menu:

            mouse = pygame.mouse.get_pos()

            win.fill(black)

            character_display = character_menu()
            character_display.character_selection()

            for event in pygame.event.get():
                if 50 + 200 > mouse[0] > 50 and 60 + 150 > mouse[1] > 60:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            print("Selected Bowsette")
                            self.character_menu = False
                elif 50 + 200 > mouse[0] > 50 and 320 + 150 > mouse[1] > 320:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            print("Selected Maid")
                            self.character_menu = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.flip()


        else:
            win.blit(scaled_background, (0, 0))

            sprites.update()

            sprites.draw(win)

            pygame.display.flip()

            clock.tick(27)


class character_menu():
    def character_selection(self):

        win.blit(bowsette, (50, 60))
        win.blit(transparentSurface, (50, 60))

        win.blit(maid, (50, 320))
        win.blit(transparentSurface, (50, 320))

        win.blit(miia, (240, 60))
        win.blit(ryuuko, (240, 320))
        win.blit(saber, (430, 60))
        win.blit(sailor, (430, 320))
        win.blit(sakura, (620, 60))
        win.blit(virgo, (620, 320))

class character_selection_rect():
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if 50 + 200 > mouse[0] > 50 and 60 + 150 > mouse[1] > 60:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("Selected Bowsette")

        if 50 + 200 > mouse[0] > 50 and 320 + 150 > mouse[1] > 320:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("Selected Maid")
