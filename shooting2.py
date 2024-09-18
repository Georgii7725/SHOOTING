import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()
bullets = []

while not done:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            bullets.append(list(pygame.mouse.get_pos()))
    
    if len(bullets) > 0:
        bullet = bullets[0]
        pygame.draw.circle(screen, (0, 0, 0), bullet, 5)
        bullets[0][1] -= 4
        if bullet[1] <= 10:
            pygame.draw.circle(screen, (255, 0, 0), bullet, 20)
            bullets.pop(0)

    clock.tick(60)

    pygame.display.flip()
