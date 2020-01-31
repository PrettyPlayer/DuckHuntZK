import os
import pygame
from random import randint

#Прицел вместо мыши
def mouse_replace(color, mouse_start_len, mouse_len, mouse_thickness):
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        pygame.draw.line(surf_main, color, (pos[0], pos[1] + mouse_start_len), (pos[0], pos[1] + mouse_start_len + mouse_len), mouse_thickness)
        pygame.draw.line(surf_main, color, (pos[0], pos[1] - mouse_start_len), (pos[0], pos[1] - mouse_start_len - mouse_len), mouse_thickness)
        pygame.draw.line(surf_main, color, (pos[0] + mouse_start_len, pos[1]), (pos[0] + mouse_start_len + mouse_len, pos[1]), mouse_thickness)
        pygame.draw.line(surf_main, color, (pos[0] - mouse_start_len, pos[1]), (pos[0] - mouse_start_len - mouse_len, pos[1]), mouse_thickness)

def path(folder, filename):
    return (os.path.realpath("") + folder + filename + format)

class Duck(pygame.sprite.Sprite):
    def __init__(self, x, y, k, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path(r"\Sprites\black\\", "duck7")).convert()
        self.image.set_colorkey((187, 238, 167))
        self.rect = self.image.get_rect(center=(x, y))

#Параметры
FPS = 60
WIDTH = 1920
HEIGHT = 1080
fullscreen = 0
format = ".png"

#Цвета
BLACK = (0, 0, 0)
ORANGE = (255, 150, 100)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
CYAN= (0, 255, 255)

#Параметры мыши
mouse_start_len = 3
mouse_len = 7
mouse_thickness = 3

#Вёрстка окна
pygame.init()
surf_main = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DuckHuntZK")
img = pygame.image.load(os.path.realpath("") + r"\Sprites\Icon.png")
pygame.display.set_icon(img)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

gamewindow = pygame.image.load(os.path.realpath("") + r"\Sprites\gamewindow.png")
gamewindow_rect = gamewindow.get_rect(topleft=(0, 0))
surf_main.blit(gamewindow, gamewindow_rect)

#Загрузка утки без фона
duck_x=WIDTH//2
duck_y=HEIGHT//2
size_k=1.4
acc_x=3
acc_y=4
hp=0
dirx="0"
diry="0"
time_img=1
time_die=1

duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck7.png")
duck_black.set_colorkey((187, 238, 167))
duck_black = pygame.transform.scale(duck_black, (int(duck_black.get_width()*size_k), int(duck_black.get_height()*size_k)))
duck_black_rect = duck_black.get_rect(center=(duck_x, duck_y))
duck_size=[duck_black.get_width(), duck_black.get_height()]

duck1 = Duck(randint(1, WIDTH), randint(1, HEIGHT), size_k, "duck7")
#Первое обновление дисплея
pygame.display.update()

#Цикл отрисовки объектов
while True:
    clock.tick(FPS)
    surf_main.blit(gamewindow, gamewindow_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        #Если нажал на утку, то отнимает хп
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if duck_x-duck_size[0]//2 <= event.pos[0] <= duck_x+duck_size[0]//2 and duck_y-duck_size[1]//2 <= event.pos[1] <= duck_y+duck_size[1]//2 and hp!=0:
                hp-=1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if fullscreen==0:
                    pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
                    fullscreen=1
                else:
                    pygame.display.set_mode((1000, 800))
                    fullscreen=0
                    
    if 60==randint(1,120):
        ran1=randint(0,1)
        dirx=ran1
    if 120==randint(1,120):
        ran2=randint(0,1)
        diry=ran2
    acc_x+=randint(-1, 1)
    if acc_x<0:
        acc_x=-acc_x
    elif acc_x>6:
        acc_x=6-(acc_x-6)
    if acc_y<0:
        acc_y=-acc_y
    elif acc_y>6:
        acc_y=6-(acc_y-6)
    acc_y+=randint(-1, 1)
    
    if time_img==5:
        if dirx == "0" and diry == "0" and acc_y > acc_x:
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck8.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "0" and diry == "0" and acc_y < acc_x:
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck11.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "1" and diry == "0" and acc_y > acc_x:
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck2.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "1" and diry == "0" and acc_y < acc_x:
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck5.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "0" and diry == "1":
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck11.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "1" and diry == "1":
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck5.png")
            duck_black.set_colorkey((187, 238, 167))
    elif time_img==10:
        if dirx == "0" and diry == "0" and acc_y > acc_x:
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck9.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "0" and diry == "0" and acc_y < acc_x:
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck12.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "1" and diry == "0" and acc_y > acc_x:
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck3.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "1" and diry == "0" and acc_y < acc_x:
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck6.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "0" and diry == "1":
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck12.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "1" and diry == "1":
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck6.png")
            duck_black.set_colorkey((187, 238, 167))
    elif time_img==15:
        if dirx == "0" and diry == "0" and acc_y > acc_x:
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck7.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "0" and diry == "0" and acc_y < acc_x:
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck10.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "1" and diry == "0" and acc_y > acc_x:
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck1.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "1" and diry == "0" and acc_y < acc_x:
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck4.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "0" and diry == "1":
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck10.png")
            duck_black.set_colorkey((187, 238, 167))
        elif dirx == "1" and diry == "1":
            duck_black = pygame.image.load(os.path.realpath("") + r"\Sprites\black\duck4.png")
            duck_black.set_colorkey((187, 238, 167))
        time_img=0
    if time_die==180:
        hp=0
    #Пока утка жива - летит
    if hp>0:
        if 30 < duck_x-duck_size[0]//2 and dirx == "0":
            duck_x-=acc_x
        else:
            dirx = "1"
        if duck_x+30 < WIDTH-duck_size[0]//2 and dirx == "1":
            duck_x+=acc_x
        else:
            dirx = "0"
        if 30 < duck_y-duck_size[1]//2 and diry == "0":
            duck_y-=acc_y
        else:
            diry = "1"
        if duck_y+30 < HEIGHT-duck_size[1]//2 and diry == "1":
            duck_y+=acc_y
        else:
            diry = "0"
        duck_black = pygame.transform.scale(duck_black, (duck_size[0]*2, duck_size[1]*2))
        duck_black_rect = duck_black.get_rect(center=(duck_x, duck_y))
        surf_main.blit(duck_black, duck_black_rect)
    else:
        var=randint(1, 8)
        if var==1:
            duck_x=WIDTH//2
            duck_y=HEIGHT+duck_size[1]
        if var==2:
            duck_x=-duck_size[0]
            duck_y=HEIGHT+duck_size[1]
        if var==3:
            duck_x=-duck_size[0]
            duck_y=HEIGHT//2
        if var==4:
            duck_x=-duck_size[0]
            duck_y=-duck_size[1]
        if var==5:
            duck_x=WIDTH//2
            duck_y=-duck_size[1]
        if var==6:
            duck_x=WIDTH+duck_size[0]
            duck_y=-duck_size[1]
        if var==7:
            duck_x=WIDTH+duck_size[0]
            duck_y=HEIGHT//2
        if var==8:
            duck_x=WIDTH+duck_size[0]
            duck_y=HEIGHT+duck_size[1]
        hp=1
        time_die=0
    surf_main.blit(duck1.image, duck1.rect)
    if duck1.rect.y < HEIGHT:
        duck1.rect.y += 2
    else:
        duck1.rect.y = 0
    #Замена мыши
    mouse_replace(RED, mouse_start_len, mouse_len, mouse_thickness)
    #Обновление дисплея
    pygame.display.update()
    time_img+=1
    time_die+=1