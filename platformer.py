import sys
import pygame
import time
import math
import random

pygame.init()

#size = width, height = 1920, 1080
size = width, height = 800, 600

black = 0, 0, 0

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
mag1 = pygame.image.load("magician1.png")
mag2 = pygame.image.load("magician2.png")
screen = pygame.display.set_mode((width, height))

clock=pygame.time.Clock()

CameraX = 0
CameraY = 0

FPS=60

class Player():
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.vx=0
		self.vy=0
		self.on_ground=False
		self.health=100
		self.mana=100
		self.dir=-1
		self.image = mag1

		self.rect=self.image.get_rect()

	def draw(self):
		global CameraX , CameraY, direction
		self.rect.center = (self.x,self.y)

		if self.on_ground==False:
			self.image=mag2
		else:
			self.image=mag1
		
		screen.blit(self.image,(self.x - CameraX, self.y - CameraY))
		pygame.display.update()

	def collision_detect(self):
		pass

	def move(self):
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
	

		
		self.x+=self.vx
		self.y+=self.vy


player1=Player(width/2,height/2)

def main():
	global CameraX , CameraYg ,direction,mag1,mag2

	screen.fill(black)

	player1.move()
	player1.draw()

	clock.tick(FPS)

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
				CameraX += -10

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

				CameraX += 10

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
