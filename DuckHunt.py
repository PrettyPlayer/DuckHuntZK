import os
import pygame
from random import randint

#Параметры
FPS = 60
WIDTH = 1920
HEIGHT = 1080
fullscreen = 0
format = ".png"
time = 0

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
	def fly(self):
		if self.hp!=0:
			if randint(0, 90)==45:
				self.angle=randint(0,359)				
				self.dir=pygame.math.Vector2()
				self.dir.from_polar((1, self.angle))
			if 50>=self.angle>=0 or 359>=self.angle>=270:
				self.dirname0="right"
				self.dirname1="down"
			elif 269>=self.angle>=130:
				self.dirname0="left"
				self.dirname1="down"
			elif 90>=self.angle>=51:
				self.dirname0="right"
				self.dirname1="up"
			elif 129>=self.angle>=91:
				self.dirname0="left"
				self.dirname1="up"
			if 0>self.x-(self.sx//2) and self.dir[0]<0:
				self.dir[0]=-self.dir[0]
				self.dirname0="right"
			elif self.x+(self.sx//2)>1920 and self.dir[0]>0:
				self.dir[0]=-self.dir[0]
				self.dirname0="left"
			if 0>self.y-(self.sy//2) and self.dir[1]<0:
				self.dir[1]=-self.dir[1]
				self.dirname1="down"
			elif self.y+(self.sy//2)>1080 and self.dir[1]>0:
				self.dir[1]=-self.dir[1]
				self.dirname="up"
			self.x+=self.dir[0]*self.acc
			self.y+=self.dir[1]*self.acc
			#Справа снизу
			if self.dirname0=="right" and self.dirname1=="down":
				if time==5:
					self.image = pygame.image.load(path(r"\Sprites\black\\", "duck4"))
					self.image.set_colorkey((187, 238, 167))
					self.image = pygame.transform.scale(self.image, (int(self.sx), int(self.sy)))
					self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
				elif time==10:
					self.image = pygame.image.load(path(r"\Sprites\black\\", "duck5"))
					self.image.set_colorkey((187, 238, 167))
					self.image = pygame.transform.scale(self.image, (int(self.sx), int(self.sy)))
					self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
				elif time==15:
					self.image = pygame.image.load(path(r"\Sprites\black\\", "duck6"))
					self.image.set_colorkey((187, 238, 167))
					self.image = pygame.transform.scale(self.image, (int(self.sx), int(self.sy)))
					self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
			#Слева снизу
			elif self.dirname0=="left" and self.dirname1=="down":
				if time==5:
					self.image = pygame.image.load(path(r"\Sprites\black\\", "duck10"))
					self.image.set_colorkey((187, 238, 167))
					self.image = pygame.transform.scale(self.image, (int(self.sx), int(self.sy)))
					self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
				elif time==10:
					self.image = pygame.image.load(path(r"\Sprites\black\\", "duck11"))
					self.image.set_colorkey((187, 238, 167))
					self.image = pygame.transform.scale(self.image, (int(self.sx), int(self.sy)))
					self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
				elif time==15:
					self.image = pygame.image.load(path(r"\Sprites\black\\", "duck12"))
					self.image.set_colorkey((187, 238, 167))
					self.image = pygame.transform.scale(self.image, (int(self.sx), int(self.sy)))
					self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
			#Справа сверху
			elif self.dirname0=="right" and self.dirname1=="up":
				if time==5:
					self.image = pygame.image.load(path(r"\Sprites\black\\", "duck1"))
					self.image.set_colorkey((187, 238, 167))
					self.image = pygame.transform.scale(self.image, (int(self.sx), int(self.sy)))
					self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
				elif time==10:
					self.image = pygame.image.load(path(r"\Sprites\black\\", "duck2"))
					self.image.set_colorkey((187, 238, 167))
					self.image = pygame.transform.scale(self.image, (int(self.sx), int(self.sy)))
					self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
				elif time==15:
					self.image = pygame.image.load(path(r"\Sprites\black\\", "duck3"))
					self.image.set_colorkey((187, 238, 167))
					self.image = pygame.transform.scale(self.image, (int(self.sx), int(self.sy)))
					self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
			#Слева сверху
			elif self.dirname0=="left" and self.dirname1=="down":
				if time==5:
					self.image = pygame.image.load(path(r"\Sprites\black\\", "duck7"))
					self.image.set_colorkey((187, 238, 167))
					self.image = pygame.transform.scale(self.image, (int(self.sx), int(self.sy)))
					self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
				elif time==10:
					self.image = pygame.image.load(path(r"\Sprites\black\\", "duck8"))
					self.image.set_colorkey((187, 238, 167))
					self.image = pygame.transform.scale(self.image, (int(self.sx), int(self.sy)))
					self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
				elif time==15:
					self.image = pygame.image.load(path(r"\Sprites\black\\", "duck9"))
					self.image.set_colorkey((187, 238, 167))
					self.image = pygame.transform.scale(self.image, (int(self.sx), int(self.sy)))
					self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
			self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))
	def hit(self, pos):
		if self.x-(self.sx//2) <= pos[0] <= self.x+(self.sx//2) and self.y-(self.sy//2) <= pos[1] <= self.y+(self.sy//2) and self.hp!=0:
			self.hp-=1
			print(self.hp)

duck1 = Duck(randint(1, WIDTH), randint(1, HEIGHT), 1.4, "duck7")
duck2 = Duck(randint(1, WIDTH), randint(1, HEIGHT), 1.7, "duck8")
duck3 = Duck(randint(1, WIDTH), randint(1, HEIGHT), 2, "duck9")

#Цикл отрисовки объектов
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
				if fullscreen==0:
					pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
					fullscreen=1
				else:
					pygame.display.set_mode((1000, 800))
					fullscreen=0
	
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