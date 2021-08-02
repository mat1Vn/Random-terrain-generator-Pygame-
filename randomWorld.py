from world import wd
import pygame
from random import randint


pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
fps=60

data = []

largura = 60 #Width of terrain
altura = 6 #Height of terrarin
spriteSize = 40 #Sprite Block Size

def generate():
	global data
	for i in range(0, largura):
		alt = range(1, randint(altura-2, altura))
		row = []
		for i in alt:
			if i == alt[-1]:
				row.append(1)
			else:
				row.append(2)
		data.append(row)	

generate()				
												
world = wd(screen, data, spriteSize)

while True:
	screen.fill((0,0,0))
	clock.tick(fps)
	world.draw(True)
	
	point = pygame.mouse.get_pos()
	reset = pygame.draw.rect(screen, (0,255,0), (650, 1100,40,40))
	
	if reset.collidepoint(point):
		data = []
		generate()
		world = wd(screen, data, spriteSize)
		
	pygame.display.update()
