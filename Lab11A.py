import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

original = 0

#still rect
red_square = pygame.Surface((50, 400))
red_square.fill((255, 0, 0))
rect_red = red_square.get_rect()
rect_red.centerx = resolution[0] // 2
rect_red.top = 0

blue_square = pygame.Surface((50, 50))
blue_square.fill((0, 0, 255))
rect_blue = blue_square.get_rect()
rect_blue.left = 0
rect_blue.centery = resolution[1] // 2


speed = 5
dir_blue = 1

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
    if keys[K_ESCAPE]:
            sys.exit(0)

 
    
    #movmenent
    rect_blue.x += speed * dir_blue

    # back and fourth
    if rect_blue.right >= resolution[0] or rect_blue.left <= 0:
        dir_blue *= -1

   #color change 
    if rect_blue.colliderect(rect_red):
        red_square.fill((0,255,0))
    else:
        red_square.fill((255,0,0))

    screen.fill((original, original, original))
    screen.blit(red_square, rect_red.topleft)
    screen.blit(blue_square, rect_blue.topleft)
    pygame.display.flip()
    clock.tick(60)
