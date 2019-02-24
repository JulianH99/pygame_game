import pygame
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path
from fighting_game.characters import Maid
from fighting_game.dynamics import MovingAnimation, FightingAnimation, ProFightingAnimation
from fighting_game.helpers.screen import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_AREA_Y
from fighting_game.character_builder import CharacterDirector, CharacterBuilder
from fighting_game.draw import redraw

pygame.init()

pygame.display.set_caption("TEST GAME")


character_builder = CharacterBuilder(Maid)
character_director = CharacterDirector(character_builder)

character_director.construct()

maid = character_builder.character

character_builder.change_class(Maid)
character_director.set_builder(character_builder)

another_maid = character_builder.character


maid.set_x_y((100, GROUND_AREA_Y))
another_maid.set_x_y((400, GROUND_AREA_Y))


print(maid)

done = False


sprites = pygame.sprite.Group()
sprites2 = pygame.sprite.Group()

sprites.add(maid)
sprites2.add(another_maid)

draw = redraw()

def collided(sprite, other):
    """Check if the hitboxes of the two sprites collide."""
    return sprite.hitbox.colliderect(other.hitbox)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    draw.draw(sprites)
    draw.draw(sprites2)
    #collided_sprites = pygame.sprite.spritecollide(sprites, sprites2, False, collided)
    #for sp in collided_sprites:
    #    print('Collision', sp)

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

pygame.quit()
