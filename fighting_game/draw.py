import pygame
from fighting_game.helpers.screen import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_AREA_Y
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path
from fighting_game.characters import Character

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = Image.load(Path.path_to("backgrounds", "BackgroundFairyTail.png"))
scaled_background = Image.scale_to_window(background)
clock = pygame.time.Clock()


class redraw():


    def draw(self, sprites):#, character):

        #self.character  = character

        win.blit(scaled_background, (0, 0))

        sprites.update()

        #character.drawHitbox()
        sprites.draw(win)

        pygame.display.flip()

        clock.tick(27)