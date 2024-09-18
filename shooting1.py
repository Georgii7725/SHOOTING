import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()
flag = False

while not done:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP and not flag:
            x, y = pygame.mouse.get_pos()
            flag = True
    if flag:
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 5)
        if y <= 10:
            pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)
            flag = False        
        y -= 2

    clock.tick(60)

    pygame.display.flip()
