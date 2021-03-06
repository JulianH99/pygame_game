import pygame
import os
from fighting_game.helpers.image import Image
from fighting_game.helpers.path import Path

rightAnimation = [pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidRight\MaidRunRight (1).png"),
                  pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidRight\MaidRunRight (2).png"),
                  pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidRight\MaidRunRight (3).png"),
                  pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidRight\MaidRunRight (4).png"),
                  pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidRight\MaidRunRight (5).png"),
                  pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidRight\MaidRunRight (6).png"),
                  pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidRight\MaidRunRight (7).png"),
                  pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidRight\MaidRunRight (8).png")]

leftAnimation = [pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLeft\MaidRunLeft (1).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLeft\MaidRunLeft (2).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLeft\MaidRunLeft (3).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLeft\MaidRunLeft (4).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLeft\MaidRunLeft (5).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLeft\MaidRunLeft (6).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLeft\MaidRunLeft (7).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLeft\MaidRunLeft (8).png"), ]

defenseAnimation = [pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDefense\MaidDefense (1).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDefense\MaidDefense (2).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDefense\MaidDefense (3).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDefense\MaidDefense (4).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDefense\MaidDefense (5).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDefense\MaidDefense (6).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDefense\MaidDefense (7).png"),
                    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDefense\MaidDefense (8).png")]

fistAnimation = [pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidFist\MaidFist (1).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidFist\MaidFist (2).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidFist\MaidFist (3).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidFist\MaidFist (4).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidFist\MaidFist (5).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidFist\MaidFist (6).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidFist\MaidFist (7).png"),
                 pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidFist\MaidFist (8).png")]

largeAttackAnimation = [
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLargeAttack\MaidLargeAttack (1).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLargeAttack\MaidLargeAttack (2).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLargeAttack\MaidLargeAttack (3).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLargeAttack\MaidLargeAttack (4).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLargeAttack\MaidLargeAttack (5).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLargeAttack\MaidLargeAttack (6).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLargeAttack\MaidLargeAttack (7).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidLargeAttack\MaidLargeAttack (8).png"),
    ]

proDefenseAnimation = [
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProDefense\MaidProDefense (1).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProDefense\MaidProDefense (2).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProDefense\MaidProDefense (3).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProDefense\MaidProDefense (4).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProDefense\MaidProDefense (5).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProDefense\MaidProDefense (6).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProDefense\MaidProDefense (7).png"),
    pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProDefense\MaidProDefense (8).png"),
    ]

proLargeAttackAnimation = [
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProLargeAttack\MaidProLargeAttack (1).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProLargeAttack\MaidProLargeAttack (2).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProLargeAttack\MaidProLargeAttack (3).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProLargeAttack\MaidProLargeAttack (4).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProLargeAttack\MaidProLargeAttack (5).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProLargeAttack\MaidProLargeAttack (6).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProLargeAttack\MaidProLargeAttack (7).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProLargeAttack\MaidProLargeAttack (8).png")]

proFistAnimation = [
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProFistAnimation\MaidProFist (1).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProFistAnimation\MaidProFist (2).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProFistAnimation\MaidProFist (3).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProFistAnimation\MaidProFist (4).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProFistAnimation\MaidProFist (5).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProFistAnimation\MaidProFist (6).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProFistAnimation\MaidProFist (7).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidProFistAnimation\MaidProFist (8).png")]

staticAnimation = [
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidStaticAnimation\MaidStatic (1).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidStaticAnimation\MaidStatic (2).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidStaticAnimation\MaidStatic (3).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidStaticAnimation\MaidStatic (4).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidStaticAnimation\MaidStatic (5).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidStaticAnimation\MaidStatic (6).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidStaticAnimation\MaidStatic (7).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidStaticAnimation\MaidStatic (8).png")
]

dieAnimation=[
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDie\MaidDie (1).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDie\MaidDie (2).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDie\MaidDie (3).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDie\MaidDie (4).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDie\MaidDie (5).png"),
pygame.image.load("assets\sprites\SpriteSheets\Maid\MaidDie\MaidDie (6).png")]
