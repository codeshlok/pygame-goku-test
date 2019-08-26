import pygame
import os
import time

pygame.init()
screen = pygame.display.set_mode((1282, 700))

finished = False
# Goku Images
KeyPressed = pygame.key.get_pressed()
Goku = 0
gokuIdle = [pygame.image.load("Goku/0.png"), pygame.image.load("Goku/1.png"), pygame.image.load("Goku/2.png")]
gokuBlast = [pygame.image.load("Goku/63.png"),pygame.image.load("Goku/64.png"), pygame.image.load("Goku/65.png"), pygame.image.load("Goku/66.png")]
left = False
right = False
idleCount = 0
white = (255, 255, 255)
# Goku Images
frame = pygame.time.Clock()
gCounter = 0
gStance = 1
while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.fill(white)

    if gStance == 1:
        Goku = gokuIdle
        if gCounter < 2:
            gCounter = gCounter + 1
    print(f"{gCounter}")
    screen.blit(Goku[gCounter], (450, 358))
    pygame.display.flip()
    frame.tick(12)
