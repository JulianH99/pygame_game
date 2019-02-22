import pygame
pygame.init()

win = pygame.display.set_mode((800,400))

pygame.display.set_caption("TEST GAME")

rightAnimation = [pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidRight\MaidRunRight (1).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidRight\MaidRunRight (2).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidRight\MaidRunRight (3).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidRight\MaidRunRight (4).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidRight\MaidRunRight (5).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidRight\MaidRunRight (6).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidRight\MaidRunRight (7).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidRight\MaidRunRight (8).png")]
leftAnimation = [pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLeft\MaidRunLeft (1).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLeft\MaidRunLeft (2).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLeft\MaidRunLeft (3).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLeft\MaidRunLeft (4).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLeft\MaidRunLeft (5).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLeft\MaidRunLeft (6).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLeft\MaidRunLeft (7).png"),
                   pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLeft\MaidRunLeft (8).png"),]
defenseAnimation = [pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidDefense\MaidDefense (1).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidDefense\MaidDefense (2).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidDefense\MaidDefense (3).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidDefense\MaidDefense (4).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidDefense\MaidDefense (5).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidDefense\MaidDefense (6).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidDefense\MaidDefense (7).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidDefense\MaidDefense (8).png")]
fistAnimation = [pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidFist\MaidFist (1).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidFist\MaidFist (2).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidFist\MaidFist (3).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidFist\MaidFist (4).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidFist\MaidFist (5).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidFist\MaidFist (6).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidFist\MaidFist (7).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidFist\MaidFist (8).png")]
largeAttackAnimation = [pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLargeAttack\MaidLargeAttack (1).png"),
                        pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLargeAttack\MaidLargeAttack (2).png"),
                        pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLargeAttack\MaidLargeAttack (3).png"),
                        pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLargeAttack\MaidLargeAttack (4).png"),
                        pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLargeAttack\MaidLargeAttack (5).png"),
                        pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLargeAttack\MaidLargeAttack (6).png"),
                        pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLargeAttack\MaidLargeAttack (7).png"),
                        pygame.image.load("assets\sprites\SpriteSheets\RealMaid\MaidLargeAttack\MaidLargeAttack (8).png"),
                        ]

backGround = pygame.image.load('assets\sprites\Backgrounds\BackgroundFairyTail.png')
basicSprite = pygame.image.load('assets\sprites\SpriteSheets\Maid\MaidBasicModel.png')

clock = pygame.time.Clock()

x = 100
y = 100
width = 48
height =48
vel = 5
isJump = False
jumpCount = 5
left = False
right = False
defense = False
attack = False
largeAttack = False

walkCount = 0

def reDrawGameWindow():
    global walkCount
    win.blit(backGround, (0,0))

    if walkCount +1>=8:
        walkCount =0
    if attack:
        win.blit(fistAnimation[walkCount // 1], (x, y))
        walkCount += 1
    if largeAttack:
        win.blit(largeAttackAnimation[walkCount // 1], (x, y))
        walkCount += 1
    if defense:
        win.blit(defenseAnimation[walkCount // 1], (x, y))
        walkCount += 1
    if right:
        win.blit(rightAnimation[walkCount//1], (x,y))
        walkCount+=1
    if left:
        win.blit(leftAnimation[walkCount//1], (x,y))
        walkCount+=1
    else:
        win.blit(basicSprite, (x,y))

    pygame.display.update()


#mainloop
run = False
while not run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -=vel
        left = True
        right = False
        defense = False
        attack = False
        largeAttack = False
    elif keys[pygame.K_RIGHT] and x < (800 - width - vel):
        x += vel
        right = True
        left = False
        defense = False
        attack = False
        largeAttack = False
    elif keys[pygame.K_DOWN]:
        defense = True
        right = False
        left = False
        attack = False
        largeAttack = False
    elif keys[pygame.K_z]:
        defense = False
        right = False
        left = False
        attack = True
        largeAttack = False
    elif keys[pygame.K_x]:
        defense = False
        right = False
        left = False
        attack = False
        largeAttack = True
    else:
        right = False
        left = False
        defense = False
        attack = False
        largeAttack = False
        walkCount = 0
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
    else:
        if jumpCount >=-5:
            neg =1
            if jumpCount <0:
                neg =-1
            y -= (jumpCount ** 2) *0.5 * neg
            jumpCount =-1
        else:
            isJump = False
            jumpCount = 10
    reDrawGameWindow()
pygame.quit()