import pygame
from fighting_game.characters import Maid, reDraw

pygame.init()

sprites = pygame.sprite.Group()

maid = Maid(100, 360)


sprites.add(maid)

done = False

clock = pygame.time.Clock()

reDraw = reDraw()

while not done:
    clock.tick(60)
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    for sprite in sprites.sprites():
        sprite.handle_keydown()

    reDraw.redrawGameWindow(sprites)

pygame.quit()
