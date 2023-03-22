import pygame
pygame.init()
screen=pygame.display.set_mode((1500,1000))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
name = input()