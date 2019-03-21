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
screen = pygame.display.set_mode((width, height))

clock=pygame.time.Clock()


FPS=60

class Player():
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.vx=0
		self.vy=0
		self.on_ground=True
		self.health=100
		self.mana=100
		self.rect=pygame.Rect(0,0,25,25)

	def draw(self):
		self.rect.center=(self.x,self.y)
		pygame.draw.rect(screen,(255,0,0),self.rect)

	def collision_detect(self):
		pass

	def move(self):
		print(self.vy)
		if self.y+self.rect.height/2 >= height:
			self.vy=0
			self.y=height-25/2

		self.vy+=0.01
		self.x+=self.vx
		self.y+=self.vy

player1=Player(width/2,height/2)

def main():

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
				player1.vy=-4



while 1:
	main()

pygame.quit()
quit()

