import pygame
from abc import abstractmethod
from fighting_game.helpers.colors import *


class Character(pygame.sprite.Sprite):
    width = 64
    height = 64

    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = self.get_image()
        self.image.set_colorkey(BLACK)
        self.x = x
        self.y = y

        pygame.draw.rect(self.image, WHITE, [100, 100, self.width, self.height])

        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y
        self.speed = [1, 0.5]

        self.jumping = False

        self.force = 8
        self.mass = 2

    @abstractmethod
    def get_image(self):
        pass

    def handle_keydown(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.rect.centerx += self.speed[0]
        if key[pygame.K_LEFT]:
            self.rect.centerx -= self.speed[0]
        if key[pygame.K_UP]:
            self.jumping = True

    def update(self, *args):
        if self.jumping:
            if self.force > 0:
                F = (0.5 * self.mass * (self.force*self.force))
            else :
                F = -(0.5 * self.mass * (self.force*self.force))

            self.rect.centery = self.rect.centery - F

            self.force -= 1

            if self.rect.centery >= 360:
                self.rect.centery = 360
                self.jumping = False
                self.force = 8


class Sakura(Character):
    def __init__(self, x, y):
        super().__init__(x, y)

    def get_image(self):
        return pygame.image.load("./assets/sprites/SpriteSheets/Sakura/SakuraBasicModel.png").convert()

