import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()


original = 0       
increasing = True  

while True:

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    
    if increasing:
        original += 1
        if original >= 255:
            increasing = False
    else:
        original -= 1
        if original <= 0:
            increasing = True

    # screen with the new color
    screen.fill((original, original, original))

    
    pygame.display.flip()
    clock.tick(60)
