import pygame

class wd():
	def __init__(self, screen, data, size, flip=False):
		self.tile_list = []
		self.size=size
		self.screen = screen
		self.flip = flip
		#load images
		pedra = pygame.image.load("tijolo_pedra.png")
		grama = pygame.image.load("grama.png")
		terra = pygame.image.load("terra.png")
		
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(grama, (self.size, self.size))
					img_rect = img.get_rect()
					img_rect.x = col_count * self.size
					img_rect.y = row_count * self.size
					tile = (img, img_rect)
					self.tile_list.append(tile)

				if tile == 2:
					img = pygame.transform.scale(terra, (self.size, self.size))
					img_rect = img.get_rect()
					img_rect.x = col_count * self.size
					img_rect.y = row_count * self.size
					
					tile = (img, img_rect)
					self.tile_list.append(tile)
					
				else:
					pass
				col_count += 1
			row_count += 1
			
	def draw(self, flip=False):
		for tile in self.tile_list:
			if flip:
				img_flip = image = pygame.transform.rotate(tile[0], 270)
				self.screen.blit(img_flip, tile[1])
			else:
				self.screen.blit(tile[0], tile[1])
