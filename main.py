# import pygame, random, sys, re, threading
# import numpy as np
# FPS=60
# clock=pygame.time.Clock()


# green=(13, 255, 0)
# black=(0,0,0)
# yellow=(255,255,0)
# red=(255,3,3)
# gray=(80,80,80)
# white=(255,255,255)
# class Game():
# 	def __init__(self):
# 		self.WINDOW_WIDTH=1200
# 		self.WINDOW_HEIGHT=675
# 		self.screen=pygame.display.set_mode(self.WINDOW_HEIGHT, self.WINDOW_WIDTH)
# 		self.load_map_run=False
# 		self.load_horse_run=False
# 	def main(self):
# 		self.show_main_menu()
# 	def load_map(self):
# 		self.map_image=[]
# 		for i in range(1,3):
# 			img = pygame.image.load(f"./asset/map/map{i}.png")
# 			img=pygame.transform.scale(img,(int(0,2*self.WINDOW_WIDTH),int(0,2*self.WINDOW_WIDTH)))
# 			self.map_image.append(img)
# 		#Chèn hiệu ứng button tại đây :))
# 		self.load_map_run=True
# 	def load_horse(self):
# 		self.map_image=[]
# 		for i in range(11,20):
# 			img = pygame.image.load(f"./asset/character/horse_avt/{i}.png")
# 			img=pygame.transform.scale(img,(int(0,2*self.WINDOW_WIDTH),int(0,2*self.WINDOW_WIDTH)))
# 			self.map_image.append(img)
# 		#Chèn hiệu ứng button tại đây :))
# 		self.load_horse_run=True
# 	def show_main_menu(self):
# 		if not self.load_map_run:
# 			self.load_map_thread = threading.Thread(target=self.load_map)
# 			self.load_map_thread.start()
# 		if not self.load_horse_run:
# 			self.load_set_thread = threading.Thread(target=self.load_horse)
# 			self.load_set_thread.start()
# 		#Load background
# 		img = pygame.image.load("./asset/image/background1.png").convert()
# 		scale = int(img.get_width() / img.get_height())
# 		self.background_image = pygame.transform.scale(img, (int(self.WINDOW_HEIGHT * scale), self.WINDOW_HEIGHT))
# 		#Buttons of menu
# 		image = pygame.image.load("./asset/button/start.png")
# 		scale = image.get_width() / image.get_height()
# 		image = pygame.transform.scale(image,
# 		                               (self.WINDOW_HEIGHT // 10 * scale, self.WINDOW_HEIGHT // 10))
# 		resolution_button = Button(self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 3, image, 1)
		
# 		menu_run = True
# 		while menu_run:
# 			for event in pygame.event.get():
# 				if event.type == pygame.QUIT:
# 					pygame.quit()
# 					sys.exit()
# 				if event.type == pygame.MOUSEBUTTONDOWN:
# 					pos = pygame.mouse.get_pos()
# 					# Check click Map
# 					if start_button.rect.collidepoint(pos):
# 						self.new_round()
# 					# if resolution_button.rect.collidepoint(pos):
# 					# 	self.show_resolution()
# 			#In button ra manfn hình
# 			#In button ra manfn hình
# 			pygame.display.update()
# 			clock.tick(FPS)

# 	def new_round(self):
# 		self.show_map()
import pygame, sys, giaodien1

WINDOW_HEIGHT = 675
WINDOW_WIDTH = 1200
screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('window')
pygame.init()
giaodien1.load_bg()
pygame.quit()

	