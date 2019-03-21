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

tiles_num=64
tile_width=tile_height=32

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
		self.rect=pygame.Rect(0,0,tile_width,tile_height)

	def draw(self):
		#self.rect.center=(self.x,self.y)
		pygame.draw.rect(screen,(255,0,0),self.rect)

	def collision_detect(self):
		pass

	def move(self):
		pass

player1=Player(width/2,height/2)

def main():

	screen.fill(black)

	player1.draw()

	clock.tick(FPS)

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
		if event.type == pygame.KEYDOWN:
			
			if event.key==pygame.K_ESCAPE:
				sys.exit()

			'''
			if event.key==pygame.K_a:

			if event.key==pygame.K_SPACE:

			if event.key==pygame.K_LSHIFT:

			if event.key==pygame.K_d:

			if event.key==pygame.K_s:

			if event.key == pygame.K_w:
			'''


while 1:
	main()
pygame.quit()
quit()
