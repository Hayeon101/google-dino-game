import pygame

pygame.init()

SCREEN = pygame.display.set_mode((1000,800))
clock = pygame.time.Clock()

while True:
    SCREEN.fill((255,255,255))
    
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.display.update()

pygame.quit()