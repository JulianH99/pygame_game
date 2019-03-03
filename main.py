import pygame
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path
from fighting_game.characters import Maid, Bowsette
from fighting_game.dynamics import LifeBar
from fighting_game.helpers.screen import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_AREA_Y
from fighting_game.characters import Maid
from fighting_game.dynamics import MovingAnimation, FightingAnimation
from fighting_game.character_builder import CharacterDirector, CharacterBuilder
from fighting_game.accessories import Slopes
from fighting_game.screen import ScreenManager, CharacterSelectionScreen

ALLOWED_DISTANCE = 150

pygame.init()

pygame.display.set_caption("TEST GAME")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = Image.load(Path.path_to("backgrounds", "BackgroundFairyTail.png"))
scaled_background = Image.scale_to_window(background)

# slopes = Slopes()


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

print(maid)

done = False

player = pygame.sprite.Group()
enemy = pygame.sprite.Group()
totalSprites = pygame.sprite.Group()
accessories = pygame.sprite.Group()

# accessories.add(slopes)

player.add(maid)
enemy.add(another_maid)

totalSprites.add(player, enemy)

# draw = Redraw()

clock = pygame.time.Clock()


life_bar = LifeBar(screen, maid)
enemy_life_bar = LifeBar(screen, another_maid, index=2)

screen_manager = ScreenManager(screen)
#
# initial_screen = InitialScreen()
characters_screen = CharacterSelectionScreen()
#
# screen_manager.add_screen('start', initial_screen)
screen_manager.add_screen('characters', characters_screen)


# This callback function is passed as the `collided`argument
# to pygame.sprite.spritecollide or groupcollide.
def collided(sprite, other):
    """Check if the hitboxes of the two sprites collide."""
    return sprite.hitbox.colliderect(other.hitbox)


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # draw.draw(totalSprites)

    life_bar.draw()
    enemy_life_bar.draw()

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_a]:
        maid.trigger_animation(MovingAnimation.WALK)
        maid.change_direction(False)
    elif key_pressed[pygame.K_d]:
        maid.trigger_animation(MovingAnimation.WALK)
        maid.change_direction(True)
    elif key_pressed[pygame.K_s]:
        maid.trigger_animation(FightingAnimation.DEFENSE)
    elif key_pressed[pygame.K_g]:
        maid.trigger_animation(FightingAnimation.FIST)
        maid.collision_with_char(another_maid)
    elif key_pressed[pygame.K_h]:
        maid.trigger_animation(FightingAnimation.LARGE_ATTACK)
    elif key_pressed[pygame.K_w]:
        maid.trigger_animation(MovingAnimation.JUMP)

    if key_pressed[pygame.K_LEFT]:
        another_maid.trigger_animation(MovingAnimation.WALK)
        another_maid.change_direction(False)
    elif key_pressed[pygame.K_RIGHT]:
        another_maid.trigger_animation(MovingAnimation.WALK)
        another_maid.change_direction(True)
    elif key_pressed[pygame.K_DOWN]:
        another_maid.trigger_animation(FightingAnimation.DEFENSE)
    elif key_pressed[pygame.K_k]:
        another_maid.trigger_animation(FightingAnimation.FIST)
        another_maid.collision_with_char(maid)
    elif key_pressed[pygame.K_l]:
        another_maid.trigger_animation(FightingAnimation.LARGE_ATTACK)
    elif key_pressed[pygame.K_UP]:
        another_maid.trigger_animation(MovingAnimation.JUMP)

    # collided_sprites = pygame.sprite.spritecollide(player, enemy, False, collided)
    # for sp in collided_sprites:
    #   print('Collision', sp)
    #
    # totalSprites.update()
    #
    # totalSprites.draw(screen)

    screen_manager.switch('characters')

    pygame.display.flip()

    screen.blit(scaled_background, (0, 0))

    clock.tick(27)


pygame.quit()
