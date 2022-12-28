import pygame,sys

WINDOW_HEIGHT = 675
WINDOW_WIDTH = 1200
screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('window')
class Button():
	def __init__(self, pos_x,pos_y,scale, img):
		width = img.get_width()
		height = img.get_height()
		self.image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (pos_x, pos_y)
		self.pos_unhover = (pos_x, pos_y)
		self.pos_hover = (pos_x, pos_y + 3)
	
	def draw(self, screen):
		screen.blit(self.image, self.rect)
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			self.rect.center = self.pos_hover
		else:
			self.rect.center = self.pos_unhover


    
