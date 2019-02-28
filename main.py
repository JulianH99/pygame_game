import pygame
import os
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path
from fighting_game.characters import Maid, Bowsette
from fighting_game.dynamics import MovingAnimation, FightingAnimation
from fighting_game.helpers.screen import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_AREA_Y
from fighting_game.characters import Maid
from fighting_game.dynamics import MovingAnimation, FightingAnimation, ProFightingAnimation
from fighting_game.helpers.screen import GROUND_AREA_Y
from fighting_game.character_builder import CharacterDirector, CharacterBuilder
from fighting_game.draw import Redraw

ALLOWED_DISTANCE = 150

pygame.init()

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

print(maid)

done = False
isJump = False

player = pygame.sprite.Group()
enemy = pygame.sprite.Group()
totalSprites = pygame.sprite.Group()

player.add(maid)
enemy.add(another_maid)
totalSprites.add(player, enemy)

draw = Redraw()


# This callback function is passed as the `collided`argument
# to pygame.sprite.spritecollide or groupcollide.
def collided(sprite, other):
    """Check if the hitboxes of the two sprites collide."""
    return sprite.hitbox.colliderect(other.hitbox)


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    draw.draw(totalSprites)

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_LEFT]:
        maid.trigger_animation(MovingAnimation.WALK)
        maid.change_direction(False)
    elif key_pressed[pygame.K_RIGHT]:
        maid.trigger_animation(MovingAnimation.WALK)
        maid.change_direction(True)
    elif key_pressed[pygame.K_DOWN]:
        maid.trigger_animation(FightingAnimation.DEFENSE)
    elif key_pressed[pygame.K_z]:
        maid.trigger_animation(FightingAnimation.FIST)
    elif key_pressed[pygame.K_x]:
        maid.trigger_animation(FightingAnimation.LARGE_ATTACK)
    elif key_pressed[pygame.K_SPACE]:
        maid.trigger_animation(MovingAnimation.JUMP)
        pass
    #collided_sprites = pygame.sprite.spritecollide(player, enemy, False, collided)
    #for sp in collided_sprites:
     #   print('Collision', sp)

pygame.quit()
