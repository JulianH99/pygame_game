"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Main module for platform scroller example.

From:
http://programarcadegames.com/python_examples/sprite_sheets/

Explanation video: http://youtu.be/czBDKWJqOao

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame

import fighting_game.constants as constants

from fighting_game.player import Player


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Test Game")

    # Create the player
    player = Player()

    active_sprite_list = pygame.sprite.Group()

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120


        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)


        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()


        active_sprite_list.draw(screen)

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit. pygame.quit()


if __name__ == "__main__":
    main()
