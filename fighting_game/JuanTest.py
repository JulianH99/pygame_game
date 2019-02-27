import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("first window")

x = 50
y = 50
width = 40
height = 60
vel = 5

isJump = False
jumpCont = 10

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # keys = pygame.key.get_pressed()
    #
    # if keys[pygame.K_LEFT] and x > vel:
    #     x -= vel * 2
    # if keys[pygame.K_RIGHT] and x < 500 - width - vel:
    #     x += vel * 2
    # if keys[pygame.K_ESCAPE]:
    #     run = False
    # if not(isJump):
    #     if keys[pygame.K_UP] and y > vel:
    #         y -= vel * 2
    #     if keys[pygame.K_DOWN] and y < 500 - height - vel:
    #         y += vel * 2
    #     if keys[pygame.K_SPACE]:
    #         isJump = True
    # else:
    #     if jumpCont >= -10:
    #         neg = 1
    #         if jumpCont < 0:
    #             neg = -1
    #         y -= (jumpCont ** 2) * 0.5 * neg
    #         jumpCont -= 1
    #     else:
    #         isJump = False
    #         jumpCont = 10
    win.fill((0,0,0))
    # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    text1, text2 = text_obje sd
    pygame.display.update()

pygame.quit()