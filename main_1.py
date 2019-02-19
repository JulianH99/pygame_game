import pygame
from fighting_game.helpers.screen import SCREEN_HEIGHT, SCREEN_WIDTH
from fighting_game.characters import Sakura
from fighting_game.helpers.colors import WHITE

pygame.init()


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

sprites = pygame.sprite.Group()

sakura = Sakura(100, 360)


sprites.add(sakura)

done = False

clock = pygame.time.Clock()

background = pygame.image.load('./assets/sprites/Backgrounds/BackgroundFairyTail.png').convert()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    sprites.draw(screen)

    for sprite in sprites.sprites():
        sprite.handle_keydown()

    sprites.update()

    clock.tick(60)

    pygame.display.flip()

    screen.blit(background, (0, 0))

pygame.quit()
