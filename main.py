import pygame
import os
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path
from fighting_game.characters import Maid
from fighting_game.dynamics import SpriteSheet, MovingAnimation, FightingAnimation
from fighting_game.helpers.screen import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_AREA_Y
from fighting_game.character_builder import CharacterDirector, CharacterBuilder


pygame.init()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("TEST GAME")


character_builder = CharacterBuilder(Maid)
character_director = CharacterDirector(character_builder)

character_director.construct()

maid = character_builder.character

maid.set_x_y((100, GROUND_AREA_Y))

print(maid)

background = Image.load(Path.path_to("backgrounds", "BackgroundFairyTail.png"))

scaled_background = Image.scale_to_window(background)

done = False


sprites = pygame.sprite.Group()

sprites.add(maid)


clock = pygame.time.Clock()


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_LEFT]:
        maid.trigger_animation(MovingAnimation.LEFT)
    elif key_pressed[pygame.K_RIGHT]:
        maid.trigger_animation(MovingAnimation.RIGHT)
    elif key_pressed[pygame.K_DOWN]:
        maid.trigger_animation(FightingAnimation.DEFENSE)

    win.blit(scaled_background, (0, 0))

    # for sprite in sprites.sprites():
    #     sprite.handle_keydown()

    sprites.update()

    sprites.draw(win)

    pygame.display.flip()

    clock.tick(27)


pygame.quit()
