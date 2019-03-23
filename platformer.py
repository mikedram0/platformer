import sys
import pygame
import time
import math
import random
pygame.init()
#size = width, height = 1920, 1080
size = width, height = 32*32, 18*32
black = 0, 0, 0

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
mag1 = pygame.image.load("magician1.png")
mag2 = pygame.image.load("magician2.png")
brick_img = pygame.image.load("brick.png")
screen = pygame.display.set_mode((width, height))

clock=pygame.time.Clock()

staticList = []

FPS=60

class Player():
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.vx=0
		self.vy=0
		self.on_ground=True
		self.on_ground=False
		self.health=100
		self.mana=100
		self.rect=pygame.Rect(0,0,25,25)
		self.dir=-1
		self.image = mag1

		self.rect=self.image.get_rect()

	def draw(self):
		global direction
		self.rect.center = (self.x,self.y)

		if self.on_ground==False:
			self.image=mag2
		else:
			self.image=mag1

		screen.blit(self.image,self.rect)

	def collision_detect(self):
		for static in staticList:
			if self.rect.bottom>=static.rect.top:
				self.on_ground=True
				self.vy=0
				self.rect.bottom=static.rect.top
				pygame.draw.rect(screen,(255,255,255),self.rect,2)
				print(self.y)


	def move(self):
		print(self.vy)
		if self.y+self.rect.height/2 >= height:
			self.vy=0
			self.y=height-25/2
		'''
		if not self.on_ground: 
			self.vy+=0.01
			if self.y+self.rect.height/2 >= height:
				self.on_ground = True
				self.y=height-32/2
				self.vy=0
	'''
		self.vy += 0.03

		#if self.on_ground:
		if self.y + self.rect.height + self.vy >= height:

			self.on_ground = True
			self.vy = 0
			self.y = height-self.rect.height

		else:
			self.on_ground = False

		if self.on_ground==True:
			self.vy = 0


		self.vy+=0.01

		self.x+=self.vx
		self.y+=self.vy


class Static:

	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.rect = brick_img.get_rect()
		staticList.append(self)

	def draw(self):
		self.rect.center = (self.x,self.y)
		screen.blit(brick_img,self.rect)
		pygame.draw.rect(screen,(255,255,255),self.rect,2)

static1=Static(width/2,height/2)
player1=Player(width/2,height/2-150)

def main():
	global direction,mag1,mag2

	clock.tick(FPS)
	screen.fill(black)
	player1.collision_detect()
	player1.move()
	player1.draw()
	for static in staticList:
		static.draw()

	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
		if event.type == pygame.KEYUP:
			if event.key==pygame.K_a:
				player1.vx=0
			if event.key==pygame.K_SPACE:
				pass
			if event.key==pygame.K_LSHIFT:
				pass
			if event.key==pygame.K_d:
				player1.vx=0
			if event.key==pygame.K_s:
				pass
			if event.key == pygame.K_w:
				pass
		if event.type == pygame.KEYDOWN:
			
			if event.key==pygame.K_ESCAPE:
				sys.exit()

			if event.key==pygame.K_a:
				tmp=player1.dir
				player1.dir=-1
				player1.vx=-2
				if tmp*player1.dir<0:
					mag2=pygame.transform.flip(mag2,True,False)
					mag1=pygame.transform.flip(mag1,True,False)

			if event.key==pygame.K_SPACE:
				pass
			if event.key==pygame.K_LSHIFT:
				pass

			if event.key==pygame.K_d:
				tmp=player1.dir
				player1.dir=1
				player1.vx=2
				if tmp*player1.dir<0:
					mag2=pygame.transform.flip(mag2,True,False)
					mag1=pygame.transform.flip(mag1,True,False)

			if event.key==pygame.K_s:
				pass

			if event.key == pygame.K_w:
				player1.vy=-4
				#player1.on_ground = False
				if player1.on_ground:
					player1.vy=-2
				#player1.on_ground = False
				#player1.on_ground = True



while 1:
	main()

pygame.quit()
quit()
