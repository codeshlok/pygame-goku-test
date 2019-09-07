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


gokuIdle = [pygame.image.load("Goku/4.png"),pygame.image.load("Goku/5.png"), pygame.image.load("Goku/6.png")]
gokuIT = [pygame.image.load("Goku/28.png"),pygame.image.load("Goku/29.png"), pygame.image.load("Goku/32.png"), pygame.image.load("Goku/33.png"), pygame.image.load("Goku/34.png"), pygame.image.load("Goku/35.png"), pygame.image.load("Goku/34.png"),pygame.image.load("Goku/33.png"), pygame.image.load("Goku/32.png"), pygame.image.load("Goku/28.png")]
gokuCharge = [pygame.image.load("Goku/77.png"), pygame.image.load("Goku/78.png"), pygame.image.load("Goku/79.png")]
uiIdle = [pygame.image.load("MUIGoku/7.png"),pygame.image.load("MUIGoku/8.png"), pygame.image.load("MUIGoku/9.png"), pygame.image.load("MUIGoku/10.png"), pygame.image.load("MUIGoku/11.png"), pygame.image.load("MUIGoku/12.png")]
uiPunch = [pygame.image.load("MUIGoku/13.png"),pygame.image.load("MUIGoku/14.png")]
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
    if KeyPressed[pygame.K_i] == 1:
        gCounter = 0
        gStance = 1
    if KeyPressed[pygame.K_q] == 1:
        gStance = 2
    if KeyPressed[pygame.K_SPACE] == 1:
        gStance = 3
    if gStance == 1:
        Goku = gokuIdle
        x = 450
        y = 358
        if gCounter < 2:
            gCounter = gCounter + 1
    if gStance == 2:
        Goku = gokuIT
        x = 450
        y = 358
        if gCounter < 9:
            gCounter = gCounter + 1
    if gStance == 3:
        Goku = gokuCharge
        x = 430
        y = 338
        gCounter = gCounter + 1
        if gCounter > 2:
            gCounter = 0

    screen.blit(Goku[gCounter], (x, y))
    pygame.display.flip()
    frame.tick(13)
