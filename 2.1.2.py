import os
import pygame

#Параметры
FPS = 60
WIDTH = 1000
HEIGHT = 700

#Цвета
BLACK = (0, 0, 0)
ORANGE = (255, 150, 100)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Вёрстка окна
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DuckHuntZK")
img = pygame.image.load(os.path.realpath("") + "\Sprites\Icon.png")
pygame.display.set_icon(img)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

#Первая отрисовка прямоугольника и его параметры
sx = 100
sy = 75
x = 0-sx
y = (HEIGHT-sy) // 2
pygame.draw.rect(sc, ORANGE, (x, y, sx, sy))

#Первое обновление дисплея
pygame.display.update()

#Цикл отрисовки объектов
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    sc.fill(BLACK)
    pygame.draw.rect(sc, ORANGE, (x, y, sx, sy))
    
    #Движение прямоугольника вверх, вниз от нажатия клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y-=3
    elif keys[pygame.K_DOWN]:
        y+=3
    elif y!=((HEIGHT-sy) // 2):
        if y>((HEIGHT-sy) // 2):
            y-=5
        if y<((HEIGHT-sy) // 2):
            y+=5
    
    #Движение прямоугольника влево, вправо
    if x >= WIDTH-sx:
        x-=10
        side="left"
    if x <= 0:
        x+=10
        side="right"
    if 0 < x < WIDTH-sx:
        if side=="left":
            x-=10
        if side=="right":
            x+=10
            
    #Круг вместо мыши
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(sc, YELLOW, (pos[0], pos[1]), 5)
    pygame.display.update()