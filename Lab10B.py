import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (600, 600)
screen = pygame.display.set_mode(resolution)
# clock = pygame.time.Clock()

original = 0

# Create a red 60×60 Surface
square = pygame.Surface((60, 60))
square.fill((255, 0, 0))

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
    if keys[K_ESCAPE]:
        sys.exit(0)

    # backround color
    screen.fill((original, original, original))

    # square placements
    screen.blit(square, (0, 0))
    screen.blit(square, (540,0))
    screen.blit(square, (0,540))
    screen.blit(square, (540,540))
    screen.blit(square, (540,540))
    screen.blit(square, (270,270))

    pygame.display.flip()
   # clock.tick(60)
