import pygame
# from time import sleep
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# pygame.draw.rect(screen, (255,0,34), pygame.Rect(42,15,40,32))
# pygame.display.flip()
# sleep(5)

window_dimensions = 800, 600
screen = pygame.display.set_mode(window_dimensions)
player_quit = False

while not player_quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_quit = True
pygame.display.flip()
