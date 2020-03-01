import os
import pygame
from random import randint

#Параметры
FPS = 60
WIDTH = 1920
HEIGHT = 1080
fullscreen = 1

#Цвета
BLACK = (0, 0, 0)
ORANGE = (255, 150, 100)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)

		#Параметры мыши
#Расстояние начала палочек мыши
mouse_start_len = 3
#Длина палочек мыши
mouse_len = 7
#Толщина палочек мыши
mouse_thickness = 3
#Цвет мыши в меню
mouse_color_menu = RED
#Цвет мыши в игре
mouse_color_game = GREEN

		#Параметры
#Изменение скорости уток (1..Inf)
duck_acc=1

#Предустановка
shotguncount=[0]
shotguncoord=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#Вёрстка окна
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
surf_main = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("DuckHuntZK")
img = pygame.image.load(os.path.realpath("Sprites\\Icon.png"))
pygame.display.set_icon(img)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

#Прицел вместо мыши
def mouse_replace_menu(mouse_color_menu, mouse_start_len, mouse_len, mouse_thickness):
	if pygame.mouse.get_focused():
		pos = pygame.mouse.get_pos()
		pygame.draw.line(surf_main, mouse_color_menu, (pos[0], pos[1] + mouse_start_len), (pos[0], pos[1] + mouse_start_len + mouse_len), mouse_thickness)
		pygame.draw.line(surf_main, mouse_color_menu, (pos[0], pos[1] - mouse_start_len), (pos[0], pos[1] - mouse_start_len - mouse_len), mouse_thickness)
		pygame.draw.line(surf_main, mouse_color_menu, (pos[0] + mouse_start_len, pos[1]), (pos[0] + mouse_start_len + mouse_len, pos[1]), mouse_thickness)
		pygame.draw.line(surf_main, mouse_color_menu, (pos[0] - mouse_start_len, pos[1]), (pos[0] - mouse_start_len - mouse_len, pos[1]), mouse_thickness)

def mouse_replace_game(mouse_mouse_color_game_game, mouse_start_len, mouse_len, mouse_thickness):
	if pygame.mouse.get_focused():
		pos = pygame.mouse.get_pos()
		pygame.draw.line(surf_main, mouse_color_game, (pos[0], pos[1] + mouse_start_len), (pos[0], pos[1] + mouse_start_len + mouse_len), mouse_thickness)
		pygame.draw.line(surf_main, mouse_color_game, (pos[0], pos[1] - mouse_start_len), (pos[0], pos[1] - mouse_start_len - mouse_len), mouse_thickness)
		pygame.draw.line(surf_main, mouse_color_game, (pos[0] + mouse_start_len, pos[1]), (pos[0] + mouse_start_len + mouse_len, pos[1]), mouse_thickness)
		pygame.draw.line(surf_main, mouse_color_game, (pos[0] - mouse_start_len, pos[1]), (pos[0] - mouse_start_len - mouse_len, pos[1]), mouse_thickness)

def fullscreen(fullscreen):
	if fullscreen == 0:
		pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
		fullscreen=1
	else:
		pygame.display.set_mode((WIDTH, HEIGHT))
		fullscreen=0

#Создание кнопок и действие по нажатию на кнопку
class Button(pygame.sprite.Sprite):
	def __init__(self, x, y, size, filename, text, font, sizetext, color):
		pygame.sprite.Sprite.__init__(self)
		self.x=x
		self.y=y
		self.image = pygame.image.load(os.path.realpath("Sprites\\button\\" + filename + ".png"))
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

#Создание уток, их полет и действие по нажатию на утку
class Duck(pygame.sprite.Sprite):
	def __init__(self, duck_x, duck_y, size, acc, filename, name):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.realpath("Sprites\\black\\" + filename + ".png"))
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
					self.image = pygame.image.load(os.path.realpath("Sprites\\" + self.name + "\\duck1.png"))
				elif 5<=self.counter%15<=9:
					self.image = pygame.image.load(os.path.realpath("Sprites\\" + self.name + "\\duck2.png"))
				elif 10<=self.counter%15<=14:
					self.image = pygame.image.load(os.path.realpath("Sprites\\" + self.name + "\\duck3.png"))
				self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*self.size), int(self.image.get_height()*self.size)))
			elif abs(self.dir[0])>abs(self.dir[1]) or abs(self.dir[0])<abs(self.dir[1]) and self.dir[1]>0:
				if 0<=self.counter%15<=4:
					self.image = pygame.image.load(os.path.realpath("Sprites\\" + self.name + "\\duck4.png"))
				elif 5<=self.counter%15<=9:
					self.image = pygame.image.load(os.path.realpath("Sprites\\" + self.name + "\\duck5.png"))
				elif 10<=self.counter%15<=14:
					self.image = pygame.image.load(os.path.realpath("Sprites\\" + self.name + "\\duck6.png"))
				self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*self.size), int(self.image.get_height()*self.size)))
			if self.dirname0==0:
				self.image = pygame.transform.flip(self.image, 1, 0)
			self.x+=self.dir[0]*self.acc*duck_acc
			self.y+=self.dir[1]*self.acc*duck_acc
			self.image.set_colorkey((187, 238, 167))
			self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
			self.time-=1
			self.counter+=1
		else:
			self.x=randint(50,1870)
			self.y=700
			self.hp = 1
	def hit1(self, pos):
		if self.x-(self.sx//2) <= pos[0] <= self.x+(self.sx//2) and self.y-(self.sy//2) <= pos[1] <= self.y+(self.sy//2):
			self.hp-=1
	def hit2(self, shotguncoord, shotguncount):
			for i in range(0,shotguncount[0]*2, 2):
				if self.x-(self.sx//2) <= shotguncoord[i] <= self.x+(self.sx//2) and self.y-(self.sy//2) <= shotguncoord[i+1] <= self.y+(self.sy//2):
					self.hp-=1

def shotguntrace(pos):
	shotguncount[0]=randint(5,7)
	for i in range(0,shotguncount[0]*2, 2):
		dirshot=pygame.math.Vector2()
		dirshot.from_polar((randint(5, 60), randint(0, 359)))
		shotguncoord[i]=round(pos[0]+dirshot[0])
		shotguncoord[i+1]=round(pos[1]+dirshot[1])

#Создание дырок от выстрелов
class Trace(pygame.sprite.Sprite):
	def __init__(self, pos, name, num, size):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.realpath("Sprites\\shot\\" + name + ".png"))
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*size), int(self.image.get_height()*size)))
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
	def activatetrace2(self, pos):
		self.rect = self.image.get_rect(center=(pos[0], pos[1]))
		self.tracetimer=60

#Создание изображения оружия и его поворот
class Weapon(pygame.sprite.Sprite):
	def __init__(self, name, pos0, pos1, timeaftershot):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.realpath("Sprites\\weapon\\" + name + "\\1.png"))
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*5), int(self.image.get_height()*5)))
		self.rect = self.image.get_rect(center=(pos0, pos1))
		self.alpha=-30
		self.alpha2=0
		#Координата Х от центра оружия
		self.xfc2=0
		self.xfc=0
		self.timeaftershot=timeaftershot
	def turn(self, pos):
		self.xfc2=1200-pos[0]
		self.alpha2=self.xfc2//58
		if self.alpha2!=self.alpha:
			self.image2 = pygame.transform.rotozoom(self.image, self.alpha2, 1)
			self.xfc=self.xfc2
			self.alpha=self.alpha2
	def turn2(self, pos):
		self.xfc2=800-pos[0]
		self.alpha2=self.xfc2//52
		if self.alpha2!=self.alpha:
			self.image2 = pygame.transform.rotozoom(self.image, self.alpha2, 1)
			self.xfc=self.xfc2
			self.alpha=self.alpha2
	def reload(self):
		pass
	def aftershot(self):
		if self.timeaftershot!=0:
			self.timeaftershot-=1

def rot_center(image, rect, angle):
		rot_image = pygame.transform.rotate(image, angle)
		rot_rect = rot_image.get_rect(center=rect.center)
		return rot_image,rot_rect

###################################################################################################################################################
##Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры#Начало игры##
###################################################################################################################################################
def GameWindow():
	frontwindow = pygame.image.load(os.path.realpath("Sprites\\front.png")).convert_alpha()
	frontwindow_rect = frontwindow.get_rect(topleft=(0, 0))
	
	backwindow = pygame.image.load(os.path.realpath("Sprites\\back.png")).convert_alpha()
	backwindow_rect = backwindow.get_rect(topleft=(0, 0))
	
	trace1 = Trace((-200, -200), "trace1", 1, 0.2)
	trace2 = Trace((-200, -200), "trace2", 2, 0.2)
	trace3 = Trace((-200, -200), "trace3", 3, 0.2)
	trace4 = Trace((-200, -200), "trace1", 4, 0.2)
	trace5 = Trace((-200, -200), "trace2", 5, 0.2)
	trace6 = Trace((-200, -200), "trace3", 6, 0.2)
	trace11 = Trace((-200, -200), "trace1", 1, 0.1)
	trace12 = Trace((-200, -200), "trace2", 2, 0.1)
	trace13 = Trace((-200, -200), "trace3", 3, 0.1)
	trace14 = Trace((-200, -200), "trace1", 4, 0.1)
	trace15 = Trace((-200, -200), "trace2", 5, 0.1)
	trace16 = Trace((-200, -200), "trace3", 6, 0.1)
	trace17 = Trace((-200, -200), "trace1", 7, 0.1)
	
	pistol = Weapon("pistol\\", WIDTH//2+300, 900, 15)
	shotgun = Weapon("shotgun\\", WIDTH//2-300, 900, 60)
	
	duck1 = Duck(randint(1, WIDTH), randint(1, HEIGHT), 1.4, 3, "duck7", "black")
	duck2 = Duck(randint(1, WIDTH), randint(1, HEIGHT), 1.7, 3, "duck8", "black")
	duck3 = Duck(randint(1, WIDTH), randint(1, HEIGHT), 2, 3, "duck9", "black")
	
	shotgun.turn2((200, 200))
	pistol.turn((400, 200))
	
	num = 1
	time = 0
	flag=False
	
	sound_magnumfire1=pygame.mixer.Sound("Sounds\\guns\\Magnum\\fire1.wav")
	sound_magnumreload=pygame.mixer.Sound("Sounds\\guns\\Magnum\\reload.wav")
	sound_shotgunfire1=pygame.mixer.Sound("Sounds\\guns\\BigShotgun\\fire1.wav")
	sound_shotgunreload=pygame.mixer.Sound("Sounds\\guns\\BigShotgun\\reload1.wav")
	sound_noammo=pygame.mixer.Sound("Sounds\\guns\\noammo.wav")
	
	revolverimage = pygame.image.load(os.path.realpath("Sprites\\weapon\\pistol\\ammo.png"))
	revolverrect = revolverimage.get_rect(center=(500, 500))
	
	mousekey0=0
	mousekey2=0
	ammomagnum=6
	ammoshotgun=2
	reloadmagnum=0
	reloadshotgun=0
	
	while True:
		surf_main.blit(backwindow, backwindow_rect)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					fullscreen(fullscreen)
				elif event.key == pygame.K_ESCAPE:
					flag=True
					break
				elif event.key == pygame.K_q:
					print(ammomagnum, reloadmagnum)
					if reloadmagnum==0:
						ammomagnum=0
						channel1=sound_magnumreload.play()
						reloadmagnum=FPS*2.3
				elif event.key == pygame.K_e:
					print(ammoshotgun, reloadshotgun)
					if reloadshotgun==0:
						ammoshotgun=0
						channel2=sound_shotgunreload.play()
						reloadshotgun=FPS*1
			elif event.type == pygame.MOUSEMOTION:
				pistol.turn(event.pos)
				shotgun.turn2(event.pos)
			if event.type == pygame.MOUSEBUTTONDOWN or mousekey0==1 or mousekey2==1:
				mousekey=pygame.mouse.get_pressed()
				if mousekey[0]==1 or mousekey0==1:
					if pistol.timeaftershot==0:
						if ammomagnum>0:
							channel=sound_magnumfire1.play()
							try:
								duck1.hit1(event.pos)
								duck2.hit1(event.pos)
								duck3.hit1(event.pos)
								trace1.activatetrace(event.pos, num)
								trace2.activatetrace(event.pos, num)
								trace3.activatetrace(event.pos, num)
								trace4.activatetrace(event.pos, num)
								trace5.activatetrace(event.pos, num)
								trace6.activatetrace(event.pos, num)
							except AttributeError:
								print("AttributeError")
							num+=1
							if num==7:
								num=1
							pistol.timeaftershot=15
							ammomagnum-=1
						elif ammomagnum==0:
							channel3=sound_noammo.play()
							pistol.timeaftershot=15
					mousekey0=1
				if mousekey[2]==1 or mousekey2==1:
					if shotgun.timeaftershot==0:
						if ammoshotgun>0:
							channel2=sound_shotgunfire1.play()
							try:
								shotguntrace(event.pos)
								duck1.hit2(shotguncoord, shotguncount)
								duck2.hit2(shotguncoord, shotguncount)
								duck3.hit2(shotguncoord, shotguncount)
								trace11.activatetrace2((shotguncoord[0],shotguncoord[1]))
								trace12.activatetrace2((shotguncoord[2],shotguncoord[3]))
								trace13.activatetrace2((shotguncoord[4],shotguncoord[5]))
								trace14.activatetrace2((shotguncoord[6],shotguncoord[7]))
								trace15.activatetrace2((shotguncoord[8],shotguncoord[9]))
								trace16.activatetrace2((shotguncoord[10],shotguncoord[11]))
								trace17.activatetrace2((shotguncoord[12],shotguncoord[13]))
							except AttributeError:
								print("AttributeError")
							shotgun.timeaftershot=20
							ammoshotgun-=1
						if ammoshotgun==0:
							channel3=sound_noammo.play()
							shotgun.timeaftershot=20
					mousekey2=1
			if event.type == pygame.MOUSEBUTTONUP:
				mousekey=pygame.mouse.get_pressed()
				if mousekey[0]==0:
					mousekey0=0
				if mousekey[2]==0:
					mousekey2=0
		if flag:
			break
		surf_main.blit(revolverimage, revolverrect)
		trace1.showtrace()
		trace2.showtrace()
		trace3.showtrace()
		trace4.showtrace()
		trace5.showtrace()
		trace6.showtrace()
		
		trace11.showtrace()
		trace12.showtrace()
		trace13.showtrace()
		trace14.showtrace()
		trace15.showtrace()
		if shotguncount[0]>5:
			trace16.showtrace()
			if shotguncount[0]>6:
				trace17.showtrace()
		
		duck1.fly()
		duck2.fly()
		duck3.fly()
		
		surf_main.blit(duck1.image, duck1.rect)
		surf_main.blit(duck2.image, duck2.rect)
		surf_main.blit(duck3.image, duck3.rect)
		
		surf_main.blit(frontwindow, frontwindow_rect)
		
		#Замена мыши
		mouse_replace_game(mouse_color_game, mouse_start_len, mouse_len, mouse_thickness)
		
		surf_main.blit(pistol.image2, pistol.rect)
		surf_main.blit(shotgun.image2, shotgun.rect)
		#Обновление дисплея
		pygame.display.update()
		time+=1
		pistol.aftershot()
		shotgun.aftershot()
		if reloadmagnum!=0:
			reloadmagnum-=1
			if reloadmagnum==1:
				ammomagnum=6
		if reloadshotgun!=0:
			reloadshotgun-=1
			if reloadshotgun==1:
				ammoshotgun=2
		
		#Задержка (FPS)
		clock.tick(FPS)

##################################################################################################################################################
##Главное меню#Главное меню#Главное меню#Главное меню#Главное меню#Главное меню#Главное меню#Главное меню#Главное меню#Главное меню#Главное меню##
##################################################################################################################################################
def MenuWindow():
	button1 = Button(400, 200, 8, "button1", "Играть", "times.ttf", 36, RED)
	button2 = Button(400, 400, 8, "button1", "Магазин", "times.ttf", 36, RED)
	button3 = Button(400, 600, 8, "button1", "Настройки", "times.ttf", 36, RED)
	
	menuwindow = pygame.image.load(os.path.realpath("Sprites\\menuwindow.png"))
	menuwindow_rect = menuwindow.get_rect(topleft=(0, 0))
	
	while True:
		surf_main.blit(menuwindow, menuwindow_rect)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
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
		mouse_replace_menu(mouse_color_menu, mouse_start_len, mouse_len, mouse_thickness)
		
		#Обновление дисплея
		pygame.display.update()
		
		#Задержка (FPS)
		clock.tick(FPS*1.2)

MenuWindow()