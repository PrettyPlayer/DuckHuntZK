import os
import pygame
from random import randint

#Параметры
FPS = 60
WIDTH = 1920
HEIGHT = 1080
fullscreen = 1
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
surf_main = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("DuckHuntZK")
img = pygame.image.load(os.path.realpath("") + r"\Sprites\Icon.png")
pygame.display.set_icon(img)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

#Прицел вместо мыши
def mouse_replace(color, mouse_start_len, mouse_len, mouse_thickness):
	if pygame.mouse.get_focused():
		pos = pygame.mouse.get_pos()
		pygame.draw.line(surf_main, color, (pos[0], pos[1] + mouse_start_len), (pos[0], pos[1] + mouse_start_len + mouse_len), mouse_thickness)
		pygame.draw.line(surf_main, color, (pos[0], pos[1] - mouse_start_len), (pos[0], pos[1] - mouse_start_len - mouse_len), mouse_thickness)
		pygame.draw.line(surf_main, color, (pos[0] + mouse_start_len, pos[1]), (pos[0] + mouse_start_len + mouse_len, pos[1]), mouse_thickness)
		pygame.draw.line(surf_main, color, (pos[0] - mouse_start_len, pos[1]), (pos[0] - mouse_start_len - mouse_len, pos[1]), mouse_thickness)

def fullscreen(fullscreen):
	if fullscreen == 0:
		pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
		fullscreen=1
	else:
		pygame.display.set_mode((1920, 1080))
		fullscreen=0

def path(folder, filename):
	return (os.path.realpath("") + folder + filename + format)
class Button(pygame.sprite.Sprite):
	def __init__(self, x, y, size, filename, text, font, sizetext, color):
		pygame.sprite.Sprite.__init__(self)
		self.x=x
		self.y=y
		self.image = pygame.image.load(path(r"\Sprites\button\\", filename))
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*size), int(self.image.get_height()*size)))
		self.rect = self.image.get_rect(center=(x, y))
		self.sx=self.image.get_width()
		self.sy=self.image.get_height()
		self.font = pygame.font.Font('Fonts/'+font, sizetext)
		self.text = self.font.render(text, 1, color)
		self.place = self.text.get_rect(center=(self.sx//2, self.sy//2))
		self.name = text
	def click(self, pos):
		if self.x-(self.sx//2) <= pos[0] <= self.x+(self.sx//2) and self.y-(self.sy//2) <= pos[1] <= self.y+(self.sy//2):
			if self.name == "Играть":
				GameWindow()

class Duck(pygame.sprite.Sprite):
	def __init__(self, duck_x, duck_y, size, filename):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(path(r"\Sprites\black\\", filename))
		self.image.set_colorkey((187, 238, 167))
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*size), int(self.image.get_height()*size)))
		self.rect = self.image.get_rect(center=(duck_x, duck_y))
		self.x=duck_x
		self.y=duck_y
		self.clock=randint(1,60)
		self.acc=3
		self.hp=1
		self.sx=self.image.get_width()
		self.sy=self.image.get_height()
		self.angle=45
		self.dir=[0.838671, 0.544639]
		self.dirname0="right"
		self.dirname1="up"
	def spriteduck(self, name, x, y, sx, sy):
		self.image = pygame.image.load(path(r"\Sprites\black\\", name))
		self.image.set_colorkey((187, 238, 167))
		self.image = pygame.transform.scale(self.image, (int(sx), int(sy)))
		self.rect = self.image.get_rect(center=(int(x), int(y)))
	def fly(self):
		pass
	def hit(self, pos):
		if self.x-(self.sx//2) <= pos[0] <= self.x+(self.sx//2) and self.y-(self.sy//2) <= pos[1] <= self.y+(self.sy//2) and self.hp!=0:
			self.hp-=1
			print(self.hp)

###################################################################################################################################################
##Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры##
###################################################################################################################################################
def GameWindow():
	gamewindow = pygame.image.load(os.path.realpath("") + r"\Sprites\gamewindow.png")
	gamewindow_rect = gamewindow.get_rect(topleft=(0, 0))
	surf_main.blit(gamewindow, gamewindow_rect)
	
	duck1 = Duck(randint(1, WIDTH), randint(1, HEIGHT), 1.4, "duck7")
	duck2 = Duck(randint(1, WIDTH), randint(1, HEIGHT), 1.7, "duck8")
	duck3 = Duck(randint(1, WIDTH), randint(1, HEIGHT), 2, "duck9")
	
	time = 0
	flag=False
	
	while True:
		if time==16:
			time=1
		surf_main.blit(gamewindow, gamewindow_rect)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				duck1.hit(event.pos)
				duck2.hit(event.pos)
				duck3.hit(event.pos)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					fullscreen(fullscreen)
				if event.key == pygame.K_ESCAPE:
					flag=True
					break
		if flag:
			break
		
		duck1.fly()
		duck2.fly()
		duck3.fly()
		
		surf_main.blit(duck1.image, duck1.rect)
		surf_main.blit(duck2.image, duck2.rect)
		surf_main.blit(duck3.image, duck3.rect)
		
		#Замена мыши
		mouse_replace(RED, mouse_start_len, mouse_len, mouse_thickness)
		
		#Обновление дисплея
		pygame.display.update()
		time+=1
		
		#Задержка (FPS)
		clock.tick(FPS)

##################################################################################################################################################
##Главное меню#Главное меню#Главное меню#Главное меню#Главное меню#Главное меню#Главное меню#Главное меню#Главное меню#Главное меню#Главное меню##
##################################################################################################################################################
button1 = Button(400, 200, 8, "button1", "Играть", "times.ttf", 36, RED)
button2 = Button(400, 400, 8, "button1", "Магазин", "times.ttf", 36, RED)
button3 = Button(400, 600, 8, "button1", "Настройки", "times.ttf", 36, RED)

menuwindow = pygame.image.load(os.path.realpath("") + r"\Sprites\menuwindow.png")
menuwindow_rect = menuwindow.get_rect(topleft=(0, 0))

while True:
	surf_main.blit(menuwindow, menuwindow_rect)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			button1.click(event.pos)
			button2.click(event.pos)
			button3.click(event.pos)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quit()
				sys.exit()
			if event.key == pygame.K_RETURN:
				fullscreen(fullscreen)
	
	#Отображение кнопок на фоне меню
	menuwindow.blit(button1.image, button1.rect)
	menuwindow.blit(button2.image, button2.rect)
	menuwindow.blit(button3.image, button3.rect)

	#Отображение текста на кнопках
	button1.image.blit(button1.text, button1.place)
	button2.image.blit(button2.text, button2.place)
	button3.image.blit(button3.text, button3.place)
	
	#Замена мыши
	mouse_replace(RED, mouse_start_len, mouse_len, mouse_thickness)
	
	#Обновление дисплея
	pygame.display.update()
	
	#Задержка (FPS)
	clock.tick(FPS)