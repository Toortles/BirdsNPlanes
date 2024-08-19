import pygame

# Window Setup
pygame.display.set_caption("Birds N' Planes")
pygame.display.set_icon(pygame.image.load("images/icon.png"))

# PyGame setup
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE, 32, vsync=True)
clock = pygame.time.Clock()
running = True


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x += 35

    def update(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.move_ip(0, -2)
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.move_ip(0, 2)


player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill([135, 206, 235])

    screen.blit(player.image, player.rect)
    player.update()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
