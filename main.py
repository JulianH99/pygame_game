import pygame
import os
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path
from fighting_game.characters import Maid
from fighting_game.dynamics import SpriteSheet, MovingAnimation, FightingAnimation
from fighting_game.helpers.screen import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_AREA_Y
import copy

print(MovingAnimation.RIGHT)

pygame.init()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("TEST GAME")

maid = Maid(100, GROUND_AREA_Y)

right_animation = SpriteSheet(
    base_sprite_path=os.path.join(maid.get_sprite_path(), 'MaidRight'), frames=8)

right_animation.base_file_name = 'MaidRunRight'
right_animation.key_name = 'maid_right'

right_animation.load_images()

left_animation = SpriteSheet(
    base_sprite_path=os.path.join(maid.get_sprite_path(), 'MaidLeft'),
    frames=8
)

left_animation.base_file_name = 'MaidRunLeft'
left_animation.key_name = 'maid_left'

left_animation.load_images()


defense_animation = SpriteSheet(
    base_sprite_path=os.path.join(maid.get_sprite_path(), 'MaidDefense'),
    frames=8
)

defense_animation.base_file_name = 'MaidDefense'
defense_animation.key_name = 'maid_defense'

defense_animation.load_images()

maid.add_sprite_sheet(MovingAnimation.RIGHT.value, right_animation)
maid.add_sprite_sheet(MovingAnimation.LEFT.value, left_animation)
maid.add_sprite_sheet(FightingAnimation.DEFENSE.value, defense_animation)

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
