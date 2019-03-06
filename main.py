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


game.on_switch('characters')
done = True

while not done:

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         done = True
    #
    # # draw.draw(totalSprites)
    #
    # life_bar.draw()
    # enemy_life_bar.draw()
    #
    # # collided_sprites = pygame.sprite.spritecollide(player, enemy, False, collided)
    # # for sp in collided_sprites:
    # #   print('Collision', sp)
    # #
    # totalSprites.update()
    # #
    # totalSprites.draw(screen)
    #
    # if random.random() < accessory_chance:
    #     slopes.rect.centerx = random.randrange(10, SCREEN_WIDTH - 10)
    #     accessories.add(slopes)
    #
    # accessories.draw(screen)
    #
    # collisions = pygame.sprite.groupcollide(totalSprites, accessories, False, False)
    #
    # for collision in collisions.keys():
    #
    #     accessory = collisions[collision][0]
    #
    #     if accessory:
    #
    #         power_up_builder.create_instance(CharacterPowerUp, collision, accessory)
    #
    #         character_director.set_builder(power_up_builder)
    #
    #         character_director.construct()
    #
    #         maid = power_up_builder.character
    #
    #     accessories.empty()
    #

    screen_manager.switch('initial')
    pygame.display.flip()

    # screen.blit(scaled_background, (0, 0))
    #
    # clock.tick(27)


pygame.quit()
