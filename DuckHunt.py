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
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)

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

def path2(folder, folder2, filename):
	return (os.path.realpath("") + folder + folder2 + filename + ".png")

def shot(pos):
	shotimg = pygame.image.load(path("\Sprites\shot\\", str(randint(1,3))))
	shotimg = pygame.transform.scale(shotimg, (int(shotimg.get_width()*1), int(shotimg.get_height()*1)))
	shotrect = shotimg.get_rect(center=(pos[0], pos[1]))

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
	def __init__(self, duck_x, duck_y, size, acc, filename, name):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(path(r"\Sprites\black\\", filename))
		self.image.set_colorkey((187, 238, 167))
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*size), int(self.image.get_height()*size)))
		self.rect = self.image.get_rect(center=(duck_x, duck_y))
		self.x=duck_x
		self.y=duck_y
		self.clock=randint(1,60)
		self.hp=1
		self.sx=self.image.get_width()
		self.sy=self.image.get_height()
		self.angle=45
		self.dir=[0.838671, 0.544639]
		self.dirname0=1
		self.dirname1=0
		self.acc=acc*size
		self.time=0
		self.counter=0
		self.name=name
		self.size=size
	def spriteduck(self, nameduck, name):
		self.image = pygame.image.load(path(r"\Sprites\black\\", name))
	def fly(self):
		if self.hp>0:
			if self.time==0:
				self.dir=pygame.math.Vector2()
				self.dir.from_polar((1, randint(0, 359)))
				self.time=randint(30, 60)
				#Смена направления от ускорения
				if self.dir[0]>=0:
					self.dirname0=1
				elif self.dir[0]<0:
					self.dirname0=0
				if self.dir[1]<0:
					self.dirname1=0
				elif self.dir[1]>=0:
					self.dirname1=1
			#Смена направления и ускорения от выхода за экран
			if self.x+self.sx//2>=WIDTH and self.dirname0==1:
				self.dir[0]=-self.dir[0]
				self.dirname0=0
			elif self.x-self.sx//2<=0 and self.dirname0==0:
				self.dir[0]=-self.dir[0]
				self.dirname0=1
			if self.y+self.sy//2>=661 and self.dirname1==1:
				self.dir[1]=-self.dir[1]
				self.dirname1=0
			elif self.y-self.sy//2<=0 and self.dirname1==0:
				self.dir[1]=-self.dir[1]
				self.dirname1=1
			#Смена спрайта каждые counter тиков и в зависимости от направления движения
			if abs(self.dir[0])<abs(self.dir[1]) and self.dir[1]<0:
				if 0<=self.counter%15<=4:
					self.image = pygame.image.load(path2(r"\Sprites\\", r"black\\", "duck1"))
					if self.dirname0==0:
						self.image = pygame.transform.flip(self.image, 1, 0)
				elif 5<=self.counter%15<=9:
					self.image = pygame.image.load(path2(r"\Sprites\\", r"black\\", "duck2"))
					if self.dirname0==0:
						self.image = pygame.transform.flip(self.image, 1, 0)
				elif 10<=self.counter%15<=14:
					self.image = pygame.image.load(path2(r"\Sprites\\", r"black\\", "duck3"))
					if self.dirname0==0:
						self.image = pygame.transform.flip(self.image, 1, 0)
				self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*self.size), int(self.image.get_height()*self.size)))
			elif abs(self.dir[0])>abs(self.dir[1]) or abs(self.dir[0])<abs(self.dir[1]) and self.dir[1]>0:
				if 0<=self.counter%15<=4:
					self.image = pygame.image.load(path2(r"\Sprites\\", r"black\\", "duck4"))
					if self.dirname0==0:
						self.image = pygame.transform.flip(self.image, 1, 0)
				elif 5<=self.counter%15<=9:
					self.image = pygame.image.load(path2(r"\Sprites\\", r"black\\", "duck5"))
					if self.dirname0==0:
						self.image = pygame.transform.flip(self.image, 1, 0)
				elif 10<=self.counter%15<=14:
					self.image = pygame.image.load(path2(r"\Sprites\\", r"black\\", "duck6"))
					if self.dirname0==0:
						self.image = pygame.transform.flip(self.image, 1, 0)
				self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*self.size), int(self.image.get_height()*self.size)))
			self.x+=self.dir[0]*self.acc
			self.y+=self.dir[1]*self.acc
			self.image.set_colorkey((187, 238, 167))
			self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
			self.time-=1
			self.counter+=1
		else:
			self.x=randint(50,1870)
			self.y=700
			self.hp = 1
	def hit(self, pos):
		if self.x-(self.sx//2) <= pos[0] <= self.x+(self.sx//2) and self.y-(self.sy//2) <= pos[1] <= self.y+(self.sy//2):
			self.hp-=1

class Trace(pygame.sprite.Sprite):
	def __init__(self, pos, name, num):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(path("\Sprites\shot\\", name))
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*0.2), int(self.image.get_height()*0.2)))
		self.rect = self.image.get_rect(center=(pos[0], pos[1]))
		self.num=num
		self.tracetimer=0
	def showtrace(self):
		if self.tracetimer!=0:
			surf_main.blit(self.image, self.rect)
			self.tracetimer-=1
		else:
			pass
	def activatetrace(self, pos, num):
		if self.num==num:
			self.rect = self.image.get_rect(center=(pos[0], pos[1]))
			self.tracetimer=60

class Weapon(pygame.sprite.Sprite):
	def __init__(self, name):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(path2("\Sprites\weapon\\", name, "1"))
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*5), int(self.image.get_height()*5)))
		self.rect = self.image.get_rect(center=(WIDTH//2+300, 900))
		self.alpha=-30
		self.alpha2=0
		#Координата Х от центра оружия
		self.xfc2=0
		self.xfc=0
	def turn(self, pos):
		self.xfc2=1200-pos[0]
		self.alpha2=self.xfc2//58
		if self.alpha2!=self.alpha:
			self.image2 = pygame.transform.rotozoom(self.image, self.alpha2, 1)
			self.xfc=self.xfc2
			self.alpha=self.alpha2

###################################################################################################################################################
##Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры##
###################################################################################################################################################
def GameWindow():
	frontwindow = pygame.image.load(os.path.realpath("") + r"\Sprites\front.png").convert_alpha()
	frontwindow_rect = frontwindow.get_rect(topleft=(0, 0))
	
	backwindow = pygame.image.load(os.path.realpath("") + r"\Sprites\back.png").convert_alpha()
	backwindow_rect = backwindow.get_rect(topleft=(0, 0))
	
	trace1 = Trace((-200, -200), "trace1", 1)
	trace2 = Trace((-200, -200), "trace2", 2)
	trace3 = Trace((-200, -200), "trace3", 3)
	trace4 = Trace((-200, -200), "trace1", 4)
	trace5 = Trace((-200, -200), "trace2", 5)
	trace6 = Trace((-200, -200), "trace3", 6)
	
	pistol = Weapon("pistol\\")
	
	duck1 = Duck(randint(1, WIDTH), randint(1, HEIGHT), 1.4, 3, "duck7", "black")
	duck2 = Duck(randint(1, WIDTH), randint(1, HEIGHT), 1.7, 3, "duck8", "black")
	duck3 = Duck(randint(1, WIDTH), randint(1, HEIGHT), 2, 3, "duck9", "black")
	
	pistol.turn((400, 200))
	
	num = 1
	time = 0
	flag=False
	
	while True:
		surf_main.blit(backwindow, backwindow_rect)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.MOUSEMOTION:
				pistol.turn(event.pos)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				duck1.hit(event.pos)
				duck2.hit(event.pos)
				duck3.hit(event.pos)
				trace1.activatetrace(event.pos, num)
				trace2.activatetrace(event.pos, num)
				trace3.activatetrace(event.pos, num)
				trace4.activatetrace(event.pos, num)
				trace5.activatetrace(event.pos, num)
				trace6.activatetrace(event.pos, num)
				num+=1
				if num==7:
					num=1
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					fullscreen(fullscreen)
				if event.key == pygame.K_ESCAPE:
					flag=True
					break
		if flag:
			break
		
		trace1.showtrace()
		trace2.showtrace()
		trace3.showtrace()
		trace4.showtrace()
		trace5.showtrace()
		trace6.showtrace()
		
		duck1.fly()
		duck2.fly()
		duck3.fly()
		
		surf_main.blit(duck1.image, duck1.rect)
		surf_main.blit(duck2.image, duck2.rect)
		surf_main.blit(duck3.image, duck3.rect)
		
		surf_main.blit(frontwindow, frontwindow_rect)
		
		#Замена мыши
		mouse_replace(GREEN, mouse_start_len, mouse_len, mouse_thickness)
		
		surf_main.blit(pistol.image2, pistol.rect)
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