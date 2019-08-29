import pygame
import os
import time

pygame.init()
screen = pygame.display.set_mode((1282, 700))

finished = False
# Goku Images
KeyPressed = pygame.key.get_pressed()
Goku = 0

uiIdle = [pygame.image.load("UIGoku/262.png"),pygame.image.load("UIGoku/263.png")]
uiPunch = [pygame.image.load("UIGoku/277.png"),pygame.image.load("UIGoku/278.png")]
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

    if KeyPressed[pygame.K_SPACE] == 1:
        gStance = 2

    if gStance == 1:
        Goku = uiIdle
        gCounter = gCounter + 1
        if gCounter > 1:
            gCounter = 0

    if gStance == 2:
        Goku = uiPunch
        gCounter = gCounter + 1
        if gCounter > 1:
            gCounter = 0

    screen.blit(Goku[gCounter], (450, 358))
    pygame.display.flip()
    frame.tick(12)
