
import pygame
import sys

size = (400, 400)
speed = 40
colour = (120, 150, 80)

screen = pygame.display.set_mode(size)
display = screen.get_rect()

ship = pygame.image.load('rocket_game_practice/images/ship.bmp')
ship_rect = ship.get_rect()

while True:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP and ship_rect.top > display.top:
                ship_rect.y -= speed
            if event.key == pygame.K_DOWN and ship_rect.bottom < display.bottom:
                ship_rect.y += speed
            if event.key == pygame.K_LEFT and ship_rect.left > display.left:
                ship_rect.x -= speed
            if event.key == pygame.K_RIGHT and ship_rect.right < display.right:
                ship_rect.x += speed

    

        screen.fill(colour)
        screen.blit(ship, ship_rect)
        pygame.display.flip()