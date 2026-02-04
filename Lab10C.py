import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (1000, 500)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

original = 0
increasing = True

green_square = pygame.Surface((100, 100))
green_square.fill((0, 255, 0))
blue_square = pygame.Surface((100, 100))
blue_square.fill((0, 0, 255))

rect_green = pygame.Rect(0, 0, 100, 100)
rect_blue = pygame.Rect(0, resolution[1]-100, 100, 100)


speed = 5
dir_green = 1
dir_blue = 1

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
    if keys[K_ESCAPE]:
        sys.exit(0)

    #movmenent
    rect_green.x += speed * dir_green
    rect_blue.x += speed * dir_blue

    # back and fourth
    if rect_green.right >= resolution[0] or rect_green.left <= 0:
        dir_green *= -1
    if rect_blue.right >= resolution[0] or rect_blue.left <= 0:
        dir_blue *= -1

    
    screen.fill((original, original, original))
    screen.blit(green_square, rect_green.topleft)
    screen.blit(blue_square, rect_blue.topleft)

    pygame.display.flip()
    clock.tick(60)
