import pygame, sys, random

FPS = 60
clock = pygame.time.Clock()
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 1200
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
class Button():
	def __init__(self, image, x_pos, y_pos, text_input, screen):
		main_font = pygame.font.SysFont("cambria", 30)
		self.image = image
		self.screen=screen
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		self.screen.blit(self.image, self.rect)
		self.screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		startgame=GameHorse()
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			option_horse()
			startgame.start_new_round()
	def changeColor(self, position):
		main_font = pygame.font.SysFont("cambria", 30)
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")









class Horse(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y, type,ran):
		super().__init__()
		self.type = type
		self.speed=ran
		self.animate_fps = .2
		self.sprites = []
		for i in range(7):
			image = pygame.image.load(f"./asset/character/horse1/{self.type}/{i + 1}.png")
			scale = image.get_width() / image.get_height()
			image = pygame.transform.scale(image, (scale * 100, 100))
			self.sprites.append(image)
		
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.rect = self.image.get_rect()
		self.rect.bottomleft = (pos_x, pos_y)
		self.positonx = pos_x
	
	def update(self):
		if self.rect.right <= WINDOW_WIDTH:

			self.positonx += self.speed
			self.rect.x = int(self.positonx)
			self.animate(self.animate_fps)
		 
	def animate(self, fps):
		self.current_sprite += fps
		if self.current_sprite >= 6:
			self.current_sprite = 0
			
		self.image = self.sprites[int(self.current_sprite)]


class GameHorse():
	def __init__(self):
		self.map_x=0
		self.scroll = 0
		self.direction_scroll = 1
		image = pygame.image.load("./asset/img/backround.png").convert()
		scale = int(image.get_width() / image.get_height())
		self.back_ground_image = pygame.transform.scale(image, (scale * 1200, 700))
	
	def main(self):
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				self.show_menu()
			clock.tick(FPS)
	
	def show_menu(self):
		
		button_login = pygame.image.load("./asset/button/button.png")
		button_login = pygame.transform.scale(button_login, (220, 100))

		button = Button(button_login, 600, 200, "START",display_surface)
		button_opt=Button(button_login, 600, 400, "OPTION",display_surface)
		main_menu_run = True
		while main_menu_run:
			display_surface.blit(self.back_ground_image, (0, 0))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					button.checkForInput(pygame.mouse.get_pos())
				button.update()
				button_opt.changeColor(pygame.mouse.get_pos())
				button_opt.update()
				button.changeColor(pygame.mouse.get_pos())
				pygame.display.update()
				clock.tick(FPS)
	
	def show_bg(self):
		map=pygame.image.load('./asset/map/map1.png')
		
		scale = int(map.get_width() / map.get_height())
		self.map = pygame.transform.scale(map, (scale * 1200, 700))
		display_surface.blit(self.map, (self.map_x, 0))
		display_surface.blit(self.map, (self.map_x+1200, 0))
		
			
	def start_new_round(self):
		moving_sprite = pygame.sprite.Group()
		for i in range(5):
			ran=random.randint(10,20)/20
			horse = Horse(0,320+ 80 * i , i + 1,ran)
			moving_sprite.add(horse)
		racing = True
		fps = 1
		while racing:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			display_surface.blit(self.back_ground_image,(0,0))
			self.map_x-=1
			self.show_bg()
			
			moving_sprite.update()
			moving_sprite.draw(display_surface)
			
			pygame.display.flip()
			clock.tick(60)

def option_horse():
	running=True
	while running:
		for event in  pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
				if pygame.Rect().collidepoint(event.pos):
					pass
		display_surface.blit( pygame.transform.scale( pygame.image.load("./asset/img/backround.png").convert(), (1200, 700)),(0,0))
		pygame.display.update()
pygame.init()
my_game = GameHorse()
my_game.main()