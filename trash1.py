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
RED = (255, 0, 0)

#Вёрстка окна
pygame.init()
pygame.display.set_caption("DuckHuntZK")
img = pygame.image.load(os.path.realpath("") + "\Sprites\Icon.png")
pygame.display.set_icon(img)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
side="right"
#Первая отрисовка прямоугольника и его параметры
class rect1:
    sizex = 100
    sizey = 75
    def __init__(self, surface, color):
        self.surf = surface
        self.color = color
        self.x = 0-self.sizex
        self.y = (HEIGHT-self.sizex) // 2
    
    def fly(self):
        pygame.draw.rect(sc, ORANGE, (self.x, self.y, self.sizex, self.sizex))
        #Движение прямоугольника влево, вправо
        if self.x >= WIDTH-self.sizex:
            self.x-=2
            side="left"
        elif self.x <= 0:
            self.x+=2
            side="right"
        elif 0 < self.x < WIDTH-self.sizex:
            if side=="left":
                self.x-=2
            if side=="right":
                self.x+=2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y-=3
        elif keys[pygame.K_DOWN]:
            self.y+=3
        elif self.y!=((HEIGHT-self.sizex) // 2):
            if self.y>((HEIGHT-self.sizex) // 2):
                self.y-=5
            if self.y<((HEIGHT-self.sizex) // 2):
                self.y+=5
sc = pygame.display.set_mode((WIDTH, HEIGHT))
surfrect1 = pygame.Surface((WIDTH//2, HEIGHT//2))
surfrect1.fill(BLUE)
sc.blit(surfrect1, (WIDTH-(WIDTH//2), HEIGHT-(HEIGHT//2)))
Rect1 = rect1(surfrect1, ORANGE)
#Первое обновление дисплея
pygame.display.update()

#Цикл отрисовки объектов
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    surfrect1.fill(BLACK)
    Rect1.fly()
    sc.blit(surfrect1, (WIDTH-(WIDTH//2), HEIGHT-(HEIGHT//2)))
    
    #Круг вместо мыши
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(sc, RED, (pos[0], pos[1]), 5)
    pygame.display.update()