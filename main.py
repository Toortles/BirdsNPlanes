import pygame

# PyGame Initialization
pygame.init()

# Imports
program_icon = pygame.image.load("images/icon.png")

# Game setup
pygame.display.set_icon(program_icon)
pygame.display.set_caption("Birds N' Planes")
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE, 32, vsync=True)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135, 206, 235))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
