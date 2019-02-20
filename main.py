import sys, pygame
from pygame.locals import *
from pygame_functions import *

screenSize(800, 400)
setBackgroundImage("assets\\sprites\\Backgrounds\\BackgroundLeafVillage.png")
testSprite = makeSprite("assets\\sprites\\SpriteSheets\\Maid\\Maid.png", 32)
# 32)  links.gif contains 32 separate frames of animation.

moveSprite(testSprite, 300, 300, True)
showSprite(testSprite)

nextFrame = clock()
frame = 0

xpos = 200
ypos= 200
xspeed = 0
go = 0

while True:
    if clock() > nextFrame:                         # We only animate our character every 80ms.
        frame = (frame+1) % 8                         # There are 8 frames of animation in each direction
        nextFrame += 200                             # so the modulus 8 allows it to loop
        changeSpriteImage(testSprite, 1)
    if keyPressed("z"):
        changeSpriteImage(testSprite, 1 * 8 + frame)
    if keyPressed("right"):
        changeSpriteImage(testSprite, 2 * 8 + frame)  # 0*8 because right animations are the 0th set in the sprite sheet
        """go = 2
        xpos += xspeed
        moveSprite(testSprite, xpos, 0)
        xspeed += 1 - go"""
    if keyPressed("down"):
        changeSpriteImage(testSprite, 3 * 8 + frame)
    #else:
        #changeSpriteImage(testSprite, 0*8 + frame)
    tick(120)

    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)


#  endWait()
