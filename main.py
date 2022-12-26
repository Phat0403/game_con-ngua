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
			##### ĐẶT 1 BIẾN ĐỂ LẤY ĐƯỢC ĐƯỜNG ĐUA TƯƠNG ỨNG
			# DÙNG 2 BIẾN MAP VÀ HORSE ĐỂ SAU NÀY XỬ LÝ BƯỚC TIẾP THEO 
			MAP_HORSE=option_horse()
			MAP=MAP_HORSE[0] # LẤY ĐƯỢC GIÁ TRỊ MAP ĐUA LÀ CÁI ĐƯỜNG LINK ẢNH ĐÃ GÁN Ở DƯỚI 
			HORSE=MAP_HORSE[1] #  LẤY ĐƯỢC GIÁ TRỊ LÀ MẢNG 2 CHIỀU GỒM 5 CON NGỰA ĐÃ CHỌN VÀ TÊN 5 CON NGƯẠ
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
			image = pygame.image.load(f"./asset/character/horse2/{self.type}/{i + 1}.png")
			scale = image.get_width() / image.get_height()
			image = pygame.transform.scale(image, (scale * 250, 250))
			self.sprites.append(image)
		
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.rect = self.image.get_rect()
		self.rect.bottomleft = (pos_x, pos_y)
		self.positonx = pos_x
	
	def update(self):
		if self.rect.right <= WINDOW_WIDTH:
			# if  self.positonx>600:
				# self.positonx += random.randint(-50,50)/10
			# else :
			self.positonx += random.randint(2,50)/20
			self.rect.x = (self.positonx)
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
		image = pygame.image.load("./asset/img/background1.png").convert()
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
		map1=pygame.image.load('./asset/map/map2.png')
		
		scale = int(map.get_width() / map.get_height())
		self.map = pygame.transform.scale(map, (scale * 1200, 700))
		self.map1 = pygame.transform.scale(map, (scale * 1200, 700))
		display_surface.blit(self.map1, (self.map_x, 0))
		display_surface.blit(self.map, (self.map_x+1200, 0))
		display_surface.blit(self.map, (self.map_x+2*1200, 0))
		
			
	def start_new_round(self):
		moving_sprite = pygame.sprite.Group()
		for i in range(5):
			ran=random.randint(10,20)/20
			horse = Horse(0,380+ 80 * i , i + 1,ran)
			moving_sprite.add(horse)
		racing = True
		fps = 1
		while racing:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			display_surface.blit(self.back_ground_image,(0,0))
			self.map_x-=3
			self.show_bg()
			
			moving_sprite.update()
			moving_sprite.draw(display_surface)
			
			pygame.display.flip()
			clock.tick(60)
#============================================================================
def option_horse():
	running=True
	RECT=pygame.transform.scale(pygame.image.load(r"asset/img/rect.png"),(120,120))
	START_BTN=pygame.transform.scale(pygame.image.load(r"asset/button/start.png"),(250,100))
	# tự đổi map chỗ đây 
	MAP=[
		pygame.transform.scale(pygame.image.load(r"asset\map\map1.png"),(400,200)),   #MAP1
		pygame.transform.scale(pygame.image.load(r"asset\map\map2.png"),(400,200)),  #MAP2
        pygame.transform.scale(pygame.image.load(r"asset\map\map3.png"),(400,200))   #MAP3
    ]
	# set 1
	# tự chọn con ngựa khác cũng đc 
	HORSE1=[
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse1\1\4.png"),(100,100)),"ten1_1"], # tự đổi tên chỗ đây
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse1\2\4.png"),(100,100)),"ten1_2"],
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse1\3\4.png"),(100,100)),"ten1_3"],
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse1\4\4.png"),(100,100)),"ten1_4"],
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse1\5\4.png"),(100,100)),"ten1_5"]
	]
	#set 2
	HORSE2=[
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse2\1\4.png"),(100,100)),"ten2_1"],
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse2\2\4.png"),(100,100)),"ten2_2"],
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse2\3\4.png"),(100,100)),"ten2_3"],
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse2\4\4.png"),(100,100)),"ten2_4"],
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse2\5\4.png"),(100,100)),"ten2_5"]
	]
	# set 3
	HORSE3=[
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse3\1\4.png"),(100,100)),"ten3_1"],
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse3\2\4.png"),(100,100)),"ten3_2"],
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse3\3\4.png"),(100,100)),"ten3_3"],
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse3\4\4.png"),(100,100)),"ten3_4"],
		[pygame.transform.scale(pygame.image.load(r"asset\character\horse3\5\4.png"),(100,100)),"ten3_5"]
	]
	HORSE=[HORSE1,HORSE2,HORSE3]
	select_horse=1
	map_select=0
	BG_x=0
	while running:
		clock.tick(1000)
		for event in  pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
				#right_map
				if pygame.Rect((829,380),(130,130)).collidepoint(event.pos):
					if map_select==2:
						map_select=0
					else:
						map_select+=1
				#left_map
				if pygame.Rect((330,380),(130,130)).collidepoint(event.pos):
					if map_select==0:
						map_select=2
					else:
						map_select-=1
			    #right_chose_hourse
				if pygame.Rect((1000,182),(100,100)).collidepoint(event.pos):
					if select_horse==2:
						select_horse=0
					else :
						select_horse+=1
					
				#left_chose_hourse
				if pygame.Rect((182,190),(100,100)).collidepoint(event.pos):
					if select_horse==0:
						select_horse=2
					else:
						select_horse-=1
					
				if pygame.Rect((490,580),(250,100)).collidepoint(event.pos):
					# LẤY GIÁ TRỊ MAP VỚI 5 CON NGỰA VÀ TÊN 5 CON NGỰA ĐỂ HIỂN THỊ ĐƯỜNG ĐUA TƯƠNG ỨNG 
					return MAP[map_select],HORSE[select_horse]
		rect_x=260
		rect_y=200
		display_surface.blit( pygame.transform.scale( pygame.image.load("./asset/img/backround.png").convert(), (1200, 700)),(BG_x,0))
		display_surface.blit( pygame.transform.scale( pygame.image.load("./asset/img/backround.png").convert(), (1200, 700)),(BG_x+1200,0))
		for i in range(0,5):
			# 5 hình vuông 
			display_surface.blit(RECT,(rect_x,rect_y))
			# 5 con ngựa 
			display_surface.blit(HORSE[select_horse][i][0],(rect_x+10,rect_y+10))
			# tên 5 con ngựa 
			display_surface.blit(pygame.font.Font(r'asset\img\SourceCodePro-Black.ttf',20).render(f'{HORSE[select_horse][i][1]}',True, (246, 142, 2)),(rect_x+20,rect_y-25))
			rect_x+=150
		display_surface.blit(pygame.font.Font(r'asset\img\SourceCodePro-Black.ttf',100).render(f'<',True, (246, 142, 2)),(182,190)) #đổi màu nút left tại đây 
		display_surface.blit(pygame.font.Font(r'asset\img\SourceCodePro-Black.ttf',100).render(f'>',True, (246, 142, 2)),(1000,190))  #có thể đổi màu
		display_surface.blit(pygame.font.Font(r'asset\img\SourceCodePro-Black.ttf',50).render(f'TÙY CHỈNH CHẾ ĐỘ',True, (246, 142, 2)),(370,50))  #có thể đổi màu 
		display_surface.blit(pygame.font.Font(r'asset\img\SourceCodePro-Black.ttf',130).render(f'<',True, (246, 142, 2)),(330,380)) #có thể đổi màu
		display_surface.blit(pygame.font.Font(r'asset\img\SourceCodePro-Black.ttf',130).render(f'>',True, (246, 142, 2)),(829,380)) #có thể đổi màu
		display_surface.blit(MAP[map_select],(420,360))
		display_surface.blit(MAP[map_select],(420,360))
		display_surface.blit(START_BTN,(490,580))
		pygame.display.update()
pygame.init()
my_game = GameHorse()
my_game.main()