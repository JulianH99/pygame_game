import pygame

from fighting_game.factories import ScreenManagerFactory
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path
from fighting_game.characters import Maid, Bowsette
from fighting_game.dynamics import LifeBar
from fighting_game.helpers.screen import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_AREA_Y
from fighting_game.characters import Maid
from fighting_game.dynamics import MovingAnimation, FightingAnimation, ScreenSwitcher
from fighting_game.character_builder import CharacterDirector, CharacterBuilder, PowerUpBuilder
from fighting_game.accessories import Slopes
from fighting_game.game import Game
from fighting_game.screen import ScreenManager, CharacterSelectionScreen, InitialScreen, FightingScreen
from fighting_game.powerups import CharacterPowerUp
import random


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

#
# while not done:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#
#     # draw.draw(totalSprites)
#
#     life_bar.draw()
#     enemy_life_bar.draw()
#
#     key_pressed = pygame.key.get_pressed()
#
#     if key_pressed[pygame.K_a]:
#         maid.trigger_animation(MovingAnimation.WALK)
#         maid.change_direction(False)
#     elif key_pressed[pygame.K_d]:
#         maid.trigger_animation(MovingAnimation.WALK)
#         maid.change_direction(True)
#     elif key_pressed[pygame.K_s]:
#         maid.trigger_animation(FightingAnimation.DEFENSE)
#     elif key_pressed[pygame.K_g]:
#         maid.trigger_animation(FightingAnimation.FIST)
#         maid.collision_with_char(another_maid)
#     elif key_pressed[pygame.K_h]:
#         maid.trigger_animation(FightingAnimation.LARGE_ATTACK)
#     elif key_pressed[pygame.K_w]:
#         maid.trigger_animation(MovingAnimation.JUMP)
#
#     if key_pressed[pygame.K_LEFT]:
#         another_maid.trigger_animation(MovingAnimation.WALK)
#         another_maid.change_direction(False)
#     elif key_pressed[pygame.K_RIGHT]:
#         another_maid.trigger_animation(MovingAnimation.WALK)
#         another_maid.change_direction(True)
#     elif key_pressed[pygame.K_DOWN]:
#         another_maid.trigger_animation(FightingAnimation.DEFENSE)
#     elif key_pressed[pygame.K_k]:
#         another_maid.trigger_animation(FightingAnimation.FIST)
#         another_maid.collision_with_char(maid)
#     elif key_pressed[pygame.K_l]:
#         another_maid.trigger_animation(FightingAnimation.LARGE_ATTACK)
#     elif key_pressed[pygame.K_UP]:
#         another_maid.trigger_animation(MovingAnimation.JUMP)
#
#     # collided_sprites = pygame.sprite.spritecollide(player, enemy, False, collided)
#     # for sp in collided_sprites:
#     #   print('Collision', sp)
#     #
#     totalSprites.update()
#     #
#     totalSprites.draw(screen)
#
#     if random.random() < accessory_chance:
#         slopes.rect.centerx = random.randrange(10, SCREEN_WIDTH - 10)
#         accessories.add(slopes)
#
#     accessories.draw(screen)
#
#     collisions = pygame.sprite.groupcollide(totalSprites, accessories, False, False)
#
#     for collision in collisions.keys():
#
#         accessory = collisions[collision][0]
#
#         if accessory:
#
#             power_up_builder.create_instance(CharacterPowerUp, collision, accessory)
#
#             character_director.set_builder(power_up_builder)
#
#             character_director.construct()
#
#             maid = power_up_builder.character
#
#         accessories.empty()
#
#
#     # screen_manager.switch('characters')
#
#     pygame.display.flip()
#
#     screen.blit(scaled_background, (0, 0))
#
#     clock.tick(27)
#
#
# pygame.quit()
