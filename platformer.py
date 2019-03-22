import sys
import pygame
import time
import math
import random

pygame.init()

size = width, height = 800, 600
black = (0, 0, 0)
white = (255,255,255)
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
mag1 = pygame.image.load("magician1.png")
screen = pygame.display.set_mode((width, height))
clock=pygame.time.Clock()
FPS=60
staticList = []

class Player():
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.vx=0
		self.vy=0
		self.on_ground=False
		self.gravity = 0.03
		self.health=100
		self.mana=100
		self.image = mag1

		self.rect=self.image.get_rect()

	def draw(self):
		self.rect.center = (self.x,self.y)		
		screen.blit(self.image,self.rect)
		pygame.draw.rect(screen,white,self.rect,3)

	def collision_detect(self):

		for static in staticList:
			if self.y+self.rect.height/2 <= static.y+static.rect.height/2:
				if self.rect.colliderect(static.rect):
					self.vy=0
					self.y=static.y-static.rect.height/2-self.rect.height/2
					self.on_ground=True
				

	def move(self):
		
		self.vy += self.gravity
		if self.y + self.rect.height + self.vy >= height:

			self.on_ground = True
			self.vy = 0
			self.y = height-self.rect.height
			
		else:
			self.on_ground = False
	
		self.x+=self.vx
		self.y+=self.vy

class Static:

	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.rect = pygame.Rect(0,0,width,height)
		self.rect.center = (self.x,self.y)
		staticList.append(self)

	def draw(self):

		self.rect.center = (self.x,self.y)
		pygame.draw.rect(screen,white,self.rect)







player1=Player(width/2,height/2)
block1 = Static(width/2,height - 100 , 500 , 50)

def main():

	clock.tick(FPS)
	dt = clock.get_fps()

	event_handeler()

	screen.fill(black)

	player1.collision_detect()
	player1.move()
	player1.draw()

	for static in staticList:
		static.draw()


	pygame.display.update()

	

def event_handeler():
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
				player1.vx=-2
				

			if event.key==pygame.K_SPACE:
				pass

			if event.key==pygame.K_LSHIFT:
				pass

			if event.key==pygame.K_d:
				player1.vx=2
				
			if event.key==pygame.K_s:
				pass

			if event.key == pygame.K_w:
				#player1.on_ground = False
				if player1.on_ground:
					player1.vy=-2
				#player1.on_ground = False
				#player1.on_ground = True



while 1:
	main()

pygame.quit()
quit()
