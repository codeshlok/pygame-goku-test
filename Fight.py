import pygame
import os
import time

pygame.init()
screen = pygame.display.set_mode((1282, 700))

x = 450
y = 358
finished = False
# Goku Images
KeyPressed = pygame.key.get_pressed()
Goku = 0

gokuIdle = [pygame.image.load("Goku/4.png"),pygame.image.load("Goku/3.png")]
gokuIT = [pygame.image.load("Goku/28.png"),pygame.image.load("Goku/29.png"), pygame.image.load("Goku/30.png"), pygame.image.load("Goku/31.png"), pygame.image.load("Goku/32.png"), pygame.image.load("Goku/33.png"), pygame.image.load("Goku/34.png"), pygame.image.load("Goku/35.png"), pygame.image.load("Goku/34.png"),pygame.image.load("Goku/33.png"), pygame.image.load("Goku/32.png"), pygame.image.load("Goku/31.png"), pygame.image.load("Goku/30.png"), pygame.image.load("Goku/28.png")]
gokuCharge = [pygame.image.load("Goku/77.png"), pygame.image.load("Goku/78.png"), pygame.image.load("Goku/79.png")]
uiIdle = [pygame.image.load("UIGoku/4.png"),pygame.image.load("UIGoku/5.png")]
uiPunch = [pygame.image.load("UIGoku/13.png"),pygame.image.load("UIGoku/14.png")]
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
    KeyPressed = pygame.key.get_pressed()

    if KeyPressed[pygame.K_q] == 1:
        gStance = 2
    if KeyPressed[pygame.K_SPACE] == 1:
        gStance = 3
    if gStance == 1:
        Goku = gokuIdle
        if gCounter < 1:
            gCounter = gCounter + 1
    if gStance == 2:
        Goku = gokuIT
        x = 450
        y = 358
        if gCounter < 13:
            gCounter = gCounter + 1
    if gStance == 3:
        Goku = gokuCharge
        x = 433
        y = 340
        gCounter = gCounter + 1
        if gCounter > 2:
            gCounter = 0
    if gStance == 10:
        Goku = uiIdle
        gCounter = gCounter + 1
        if gCounter > 1:
            gCounter = 0

    if gStance == 11:
        Goku = uiPunch
        gCounter = gCounter + 1
        if gCounter > 1:
            gCounter = 0

    screen.blit(Goku[gCounter], (x, y))
    pygame.display.flip()
    frame.tick(12)
