import pygame

pygame.init()
size = width, height = list(map(int, input().split()))
screen = pygame.display.set_mode(size)

screen.fill((0, 0, 0))
pygame.draw.rect(screen, (255, 0, 0), (1, 1, width - 1, height - 1))
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass

pygame.quit()