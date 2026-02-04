import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (500, 500)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

blue_square = pygame.Surface((50, 50))
blue_square.fill((0, 0, 255))
rect_blue = blue_square.get_rect()
rect_blue.left = 0
rect_blue.center = (resolution[0] // 2, resolution[1] // 2)



original = 0

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
    if keys[K_ESCAPE]:
            sys.exit(0)

    if keys[K_w]:
         rect_blue.y -= 5
    elif keys[K_a]:
         rect_blue.x -= 5
    elif keys[K_d]:
         rect_blue.x += 5
    elif keys[K_s]:
         rect_blue.y += 5

    screen.fill((original, original, original))
    screen.blit(blue_square, rect_blue.topleft)
    pygame.display.flip()
    clock.tick(60)