import pygame

# PyGame Initialization
# pygame.init()
player_pos = pygame.Vector2(150, 350)

# Imports
program_icon = pygame.image.load("images/icon.png")

player_rotation = pygame.Surface((32, 32))
player_rotation.fill((255, 255, 255, 0))
player_icon = pygame.image.load("images/player.png")

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

    screen.blit(player_rotation, player_pos)

    if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
        player_rotation = pygame.transform.rotate(player_icon, 5)
        player_pos = player_pos - pygame.Vector2(0, 5)
    elif pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
        player_pos = player_pos + pygame.Vector2(0, 5)
        player_rotation = pygame.transform.rotate(player_icon, -5)
    else:
        player_rotation = player_icon

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
