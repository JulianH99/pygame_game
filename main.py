import pygame
import os
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path
from fighting_game.characters import Maid, Bowsette
from fighting_game.dynamics import MovingAnimation, FightingAnimation, ProFightingAnimation
from fighting_game.helpers.screen import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_AREA_Y
from fighting_game.character_builder import CharacterDirector, CharacterBuilder


ALLOWED_DISTANCE = 150

pygame.init()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("TEST GAME")


character_builder = CharacterBuilder(Maid)
character_director = CharacterDirector(character_builder)

character_director.construct()

maid = character_builder.character

character_builder.change_class(Maid)
character_director.set_builder(character_builder)

character_director.construct()

another_maid = character_builder.character


maid.set_x_y((100, GROUND_AREA_Y))
another_maid.set_x_y((400, GROUND_AREA_Y))

character_builder.change_class(Bowsette)
character_director.set_builder(character_builder)

character_director.construct()

bowsette = character_builder.character

bowsette.set_x_y((400, GROUND_AREA_Y))

background = Image.load(Path.path_to("backgrounds", "BackgroundFairyTail.png"))

scaled_background = Image.scale_to_window(background)

done = False


sprites = pygame.sprite.Group()

sprites.add(maid)
sprites.add(bowsette)


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
    elif key_pressed[pygame.K_z]:
        maid.trigger_animation(FightingAnimation.FIST)
    elif key_pressed[pygame.K_x]:
        maid.trigger_animation(FightingAnimation.LARGE_ATTACK)

    distance = maid.rect.centerx - bowsette.rect.centerx

    # if abs(distance) < ALLOWED_DISTANCE:
    #     bowsette.trigger_animation(MovingAnimation.LEFT)
    # elif abs(distance) > ALLOWED_DISTANCE:
    #     bowsette.trigger_animation(MovingAnimation.RIGHT)

    win.blit(scaled_background, (0, 0))

    maid.collision_with_char(another_maid)

    sprites.update()

    sprites.draw(win)

    pygame.display.flip()

    clock.tick(27)


pygame.quit()
