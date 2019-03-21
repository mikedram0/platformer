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
tiles_num=64

FPS=60

def main():
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
