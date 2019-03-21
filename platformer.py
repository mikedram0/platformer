import pygame


pygame.init()
width = 1280
height = 720
black = (0,0,0)
white = (255,255,255)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
sysfont = pygame.font.SysFont(None , 40)

nTilesX = 64
nTilesY = 64


def main():
	
	event_handeler()




def event_handeler():

	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()
			quit()


while 1:
	main()

pygame.quit()
quit()
