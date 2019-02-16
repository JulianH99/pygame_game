import sys, pygame
from fighting_game.spritesheet import spritesheet
from pygame.locals import KEYDOWN, KEYUP, RLEACCEL, Color, K_ESCAPE, K_RETURN, QUIT
from fighting_game.spriteStripAnim import SpriteStripAnim

# Sizes of the window
WIDTH = 640
HEIGHT = 480

""" This is the prototype for the player, first im going to use the maid static, but this needs be an abstract class for
    can be used for ever other character, i guess than the best is pass another parameter"""
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        FPS = 120
        frames = FPS / 12
        strips = [
            SpriteStripAnim('assets\sprites\SpriteSheets\Maid\MaidStatic.png', (0, 0, 48, 48), 8, 1, True, frames),

        ]
        black = Color('black')
        clock = pygame.time.Clock()
        n = 0
        strips[n].iter()
        image = strips[n].next()
        while True:
            for e in pygame.event.get():
                if e.type == KEYUP:
                    if e.key == K_ESCAPE:
                        sys.exit()
                    elif e.key == K_RETURN:
                        n += 1
                        if n >= len(strips):
                            n = 0
                        strips[n].iter()
            image = strips[n].next()
            clock.tick(FPS)

        self.image = load_image("assets\sprites\SpriteSheets\Maid\MaidStatic.png", True)
        self.rect = self.image.get_rect()
        self.rect.width = 20
        self.rect.height = 20
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]

# Function for load the images on the screen
def load_image(filename, transparent=False):
    # In the following lines i have a mistake, is fault of my version of python, discoment in your case

    #try:
    image = pygame.image.load(filename)

    #except pygame.error, message:
        #raise SystemExit, message

    image = image.convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image


def main ():

    # Creation of the Screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Test game")

    # Creation of the player
    player = Player()

    # Event for the close of the window

    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        screen.blit(player.image, player.rect)
        pygame.display.flip()
    return 0


if __name__ == '__main__':
    pygame.init()
    main()
