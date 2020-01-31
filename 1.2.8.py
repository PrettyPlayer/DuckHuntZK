import os
import pygame

FPS = 60
WIDTH = 500
HEIGHT = 300

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DuckHuntZK")
img = pygame.image.load(os.path.realpath("") + "\Sprites\Icon.png")
pygame.display.set_icon(img)
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
ORANGE = (255, 150, 100)
sx = 100
sy = 75
x = 0-sx
y = (HEIGHT-sy) // 2
pygame.draw.rect(sc, ORANGE, (x, y, sx, sy))

pygame.display.update()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    sc.fill(BLACK)
    pygame.draw.rect(sc, ORANGE, (x, y, sx, sy))
    
    if x >= WIDTH-sx:
        x-=2
        side="left"
    if x <= 0:
        x+=2
        side="right"
    if 0 < x < WIDTH-sx:
        if side=="left":
            x-=2
        if side=="right":
            x+=2
        
    pygame.display.update()