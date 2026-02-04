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

blue_square2 = pygame.Surface((50, 50))
blue_square2.fill((0, 0, 255))
rect_blue2 = blue_square2.get_rect()
rect_blue2.left = 0
rect_blue2.bottom = resolution[1]

blue_square3 = pygame.Surface((50, 50))
blue_square3.fill((0, 0, 255))
rect_blue3 = blue_square3.get_rect()
rect_blue3.left = 0
rect_blue3.top = 0




speed = 5
dir_blue = 1
dir_blue2 = 4
dir_blue3 = 2
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
    if keys[K_ESCAPE]:
            sys.exit(0)

 
    
    #movmenent
    rect_blue.x += speed * dir_blue
    rect_blue2.x += speed * dir_blue2
    rect_blue3.x += speed * dir_blue3

    # back and fourth
    if rect_blue.right >= resolution[0] or rect_blue.left <= 0:
        dir_blue *= -1
    if rect_blue2.right >= resolution[0] or rect_blue2.left <= 0:
        dir_blue2 *= -1
    if rect_blue3.right >= resolution[0] or rect_blue3.left <= 0:
        dir_blue3 *= -1

   #color change 
    if rect_blue.colliderect(rect_red) or rect_blue2.colliderect(rect_red) or rect_blue3.colliderect(rect_red):
        red_square.fill((0,255,0))
    else:
        red_square.fill((255,0,0))

    screen.fill((original, original, original))
    screen.blit(red_square, rect_red.topleft)
    screen.blit(blue_square, rect_blue.topleft)
    screen.blit(blue_square2,rect_blue2.topleft)
    screen.blit(blue_square3,rect_blue3.topleft)
    pygame.display.flip()
    clock.tick(60)
