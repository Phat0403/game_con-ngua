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


import pygame, sys, random, button
WINDOW_WIDTH =1200
WINDOW_HEIGHT =675

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock=pygame.time.Clock()
FPS=60
class Horse(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, type,ran):
        super().__init__()
        
        self.type = type
        self.speed=ran
        self.animate_fps = .4
        self.sprites = []
        for i in range(7):
            image = pygame.image.load(f"./asset/character/horse{main_game.index+1}/{self.type}/{i + 1}.png")
            scale = image.get_width() / image.get_height()
            image = pygame.transform.scale(image, (scale * 150, scale*150))
            self.sprites.append(image)
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (pos_x, pos_y)
        self.positonx = pos_x
	
    def update(self,bua):
        if self.rect.right==main_game.rect_bua.left:
            main_game.showbua=False

        if self.rect.right <= WINDOW_WIDTH:
			
            
            self.positonx += (self.speed)*bua
            
            self.rect.x = (self.positonx)
            
            self.animate(self.animate_fps)
        else:
            # main_game.rank.append(self)
            if len(main_game.rank)>=1:
                main_game.speed_map=main_game.stop_map

    def animate(self, fps):
        self.current_sprite += fps
        if self.current_sprite >= 6:
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]






class Game():
    def __init__(self):
        self.WINDOW_WIDTH = 1200
        self.WINDOW_HEIGHT = 675
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        # hinh anh background
        background=pygame.image.load('./asset/img/cloud.png')
        scale = background.get_width() / background.get_height()
        self.background=pygame.transform.scale(background,(scale * 1200, 700))
        img_bua=pygame.image.load(f"./asset/bua/bua.png")
        self.img_bua=pygame.transform.scale(img_bua, (100,100))
        self.rect_bua=self.img_bua.get_rect()

        #Bua
        self.showbua=True
        self.rank=[]
        self.bua_x=[]
        self.list_horse=[]
        for i in range(0,5):
            self.bua_x.append(random.randint(200,800))
        #tien
        self.coin=1000
        #loai ngua
        self.index=0
        #loai map
        self.map=0
        #chay map
        self.stop_map=0
        self.speed_map=2
    def load_bg(self):
        self.menu_music = pygame.mixer.Sound("./asset/sound/music.mp3")
        self.menu_music.set_volume(.2)
        self.menu_music.play(-1)
        img1=pygame.image.load('./asset/img/bg1.png')
        background=pygame.transform.scale(img1, (1200,800))
        img2=pygame.image.load('./asset/img/cloud.png')
        cloud=pygame.transform.scale(img2, (1200,600))
        img_button_start=pygame.image.load('./asset/img/button_start.png')
        button_start=pygame.transform.scale(img_button_start, (200,100))
        button_start=button.Button(610,150,1,button_start)
        img_button_setting=pygame.image.load('./asset/img/button_setting.png')
        button_setting=pygame.transform.scale(img_button_setting, (240,90))
        button_setting=button.Button(607,280,1,button_setting)
        running=True
        cloud_x=0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if button_start.rect.collidepoint(pos):
                        self.option_horse()

                    if button_setting.rect.collidepoint(pos):
                        print('danh')
            self.screen.blit(cloud, (cloud_x,-50))
            self.screen.blit(cloud, (cloud_x+1170,-50))

            cloud_x-=1
            self.screen.blit(background, (0,-125))
            if cloud_x==-1170:
                cloud_x=0
            button_start.draw(self.screen)
            button_setting.draw(self.screen)
            pygame.display.update()


    def option_horse(self):
        running=True
        RECT=pygame.transform.scale(pygame.image.load(r"asset/img/rect.png"),(120,120))
        RECT_hover=pygame.transform.scale(pygame.image.load(r"asset/img/rect.png"),(120,120))
        START_BTN=button.Button(610,600,0.3,pygame.image.load(r"asset/img/button_start.png"))

    	# tự đổi map chỗ đây 
        MAP=[
    		pygame.transform.scale(pygame.image.load(r"asset/map/map1.png"),(400,200)),   #MAP1
    		pygame.transform.scale(pygame.image.load(r"asset/map/map2.png"),(400,200)),  #MAP2
            pygame.transform.scale(pygame.image.load(r"asset/map/map3.png"),(400,200))   #MAP3
        ]
    	# set 1
    	# tự chọn con ngựa khác cũng đc 
        HORSE1=[
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/1/4.png"),(100,100)),"ten1_1"], # tự đổi tên chỗ đây
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/2/4.png"),(100,100)),"ten1_2"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/3/4.png"),(100,100)),"ten1_3"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/4/4.png"),(100,100)),"ten1_4"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse1/5/4.png"),(100,100)),"ten1_5"]
    	]
    	#set 2
        HORSE2=[
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse2/1/4.png"),(100,100)),"ten2_1"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse2/2/4.png"),(100,100)),"ten2_2"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse2/3/4.png"),(100,100)),"ten2_3"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse2/4/4.png"),(100,100)),"ten2_4"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse2/5/4.png"),(100,100)),"ten2_5"]
        ]
    	# set /
        HORSE3=[
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/1/4.png"),(100,100)),"ten3_1"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/2/4.png"),(100,100)),"ten3_2"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/3/4.png"),(100,100)),"ten3_3"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/4/4.png"),(100,100)),"ten3_4"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse3/5/4.png"),(100,100)),"ten3_5"]
    	]
        HORSE4=[
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/1/4.png"),(100,100)),"ten4_1"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/2/4.png"),(100,100)),"ten4_2"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/3/4.png"),(100,100)),"ten4_3"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/4/4.png"),(100,100)),"ten4_4"],
    		[pygame.transform.scale(pygame.image.load(r"asset/character/horse4/5/4.png"),(100,100)),"ten4_5"]
    	]
        HORSE=[HORSE1,HORSE2,HORSE3,HORSE4]
        button_go_back=button.Button(50,50,0.1,pygame.image.load(r"asset/button/go_back.png"))
        
        
        BG_x=0
        while running:
            clock.tick(60)
            for event in  pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
    				
                    if button_go_back.rect.collidepoint(event.pos): 
                        running = False 
                    #right_map

                    if pygame.Rect((829,380),(130,130)).collidepoint(event.pos):
                        if self.map==2:
                            self.map=0
                        else:
                            self.map+=1
    				#left_map
                    if pygame.Rect((330,380),(130,130)).collidepoint(event.pos):
                        if self.map==0:
                            self.map=2
                        else:
                            self.map-=1
    			    #right_chose_hourse
                    if pygame.Rect((1000,182),(100,100)).collidepoint(event.pos):
                        if self.index==3:
                            self.index=0
                        else :
                            self.index+=1
    
    				#left_chose_hourse
                    if pygame.Rect((182,190),(100,100)).collidepoint(event.pos):
                        if self.index==0:
                            self.index=3
                        else:
                            self.index-=1
    
                    if pygame.Rect((490,580),(250,100)).collidepoint(event.pos):
    					# LẤY GIÁ TRỊ MAP VỚI 5 CON NGỰA VÀ TÊN 5 CON NGỰA ĐỂ HIỂN THỊ ĐƯỜNG ĐUA TƯƠNG ỨNG 
                        self.maingame()
                    #
                            

            rect_x=260
            rect_y=200
            self.screen.blit( pygame.transform.scale( pygame.image.load("./asset/img/cloud.png").convert(), (1200, 900)),(BG_x,0))
    
            for i in range(0,5):
                # 5 hình vuông
                self.screen.blit(RECT,(rect_x,rect_y))
                # 5 con ngựa 
                self.screen.blit(HORSE[self.index][i][0],(rect_x+10,rect_y+10))
                
                # tên 5 con ngựa 
                self.screen.blit(pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf',20).render(f'{HORSE[self.index][i][1]}',True, (246, 142, 2)),(rect_x+20,rect_y-25))
                rect_x+=150
            self.screen.blit(pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf',100).render(f'<',True, (246, 142, 2)),(182,190)) #đổi màu nút left tại đây 
            self.screen.blit(pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf',100).render(f'>',True, (246, 142, 2)),(1000,190))  #có thể đổi màu
            self.screen.blit(pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf',50).render(f'TÙY CHỈNH CHẾ ĐỘ',True, (246, 142, 2)),(370,50))  #có thể đổi màu 
            self.screen.blit(pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf',130).render(f'<',True, (246, 142, 2)),(330,350)) #có thể đổi màu
            self.screen.blit(pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf',130).render(f'>',True, (246, 142, 2)),(829,350)) #có thể đổi màu
            self.screen.blit(MAP[self.map],(420,350))
            self.screen.blit(MAP[self.map],(420,350))
            START_BTN.draw(self.screen)
            button_go_back.draw(self.screen)
            self.coin
            pygame.display.update()
    
    #đặt cược
    def coin(self):
        
        base_font = pygame.font.Font(None,32)
        user_text = ''
        input_rect = pygame.Rect(200,200,140,32)
        color = pygame.Color(135,206,250)
        color2 = pygame.Color(255,127,90)
        run = True
        active = False
        temp = ''
        coin = 100
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        temp = event.unicode
                        if temp.isdigit() and int(user_text + temp) <= coin:
                            user_text += temp 

           
            if active == True:
                color = color2
            pygame.draw.rect(self.screen,color,input_rect,2)

            text_surface = base_font.render(user_text,True,(255,255,255))

            self.screen.blit(text_surface,(input_rect.x +100,input_rect.y + 500))
            input_rect.w = max(100, text_surface.get_width()+10)
            pygame.display.flip()


        

    def maingame(self):
        self.menu_music.stop()
        ran=random.randint(2,400)/400
        horse1=Horse(0,260+ 110* 0 , 0 + 1,ran)
        horses1= pygame.sprite.Group()
        horses1.add(horse1)
        ran=random.randint(2,400)/400    
        horse2=Horse(0,260+ 110* 1 , 1 + 1,ran)
        horses2= pygame.sprite.Group()
        horses2.add(horse2) 
        ran=random.randint(2,400)/400   
        horse3=Horse(0,260+ 110* 2 , 2 + 1,ran)
        horses3= pygame.sprite.Group()
        horses3.add(horse3) 
        ran=random.randint(2,400)/400   
        horse4=Horse(0,260+ 110* 3 , 3 + 1,ran)
        horses4= pygame.sprite.Group()
        horses4.add(horse4)  
        ran=random.randint(2,400)/400  
        horse5=Horse(0,260+ 110* 4 , 4 + 1,ran)
        horses5= pygame.sprite.Group()
        horses5.add(horse5)   
        racing = True
        dem=0
        horse_x=[0,0,0,0,0]
        hidden=[True,True,True,True,True] # hidden của bùa 
        active=[False,False,False,False,False] # trạng thái kích hoạt bùa 
        horse=[horse1,horse2,horse3,horse4,horse5] # lấy ra 5 con ngụaư cho dễ gọi vòng for
        bua=[5,0.2,0,-200,200,900] 
        # tăng tốc
        # giảm tốc 
        # choáng 
        # tốc biến ngược 
        # tốc biến until
        # về đích 
        bua_get=[1,1,1,1,1,1] # bùa tạm thời 
        end_bua=[0,0,0,0,0,0] # đêm vòng lặp để kết thúc trạng thái bùa 
        bua_input=[1,1,1,1,1,1] # bùa truyền con ngựa 
        end_horse=[False,False,False,False,False]  # trạng thái về đích của ngựa 
        while racing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            image=pygame.image.load(f'./asset/map/map{self.map+1}.png')
            scale = image.get_width() / image.get_height()
            image_map=pygame.transform.scale(image,(scale * 800, 675))
            self.screen.blit(self.background,(0,0))
            self.speed_map-=2
            self.screen.blit(image_map,(self.speed_map,0))
            self.screen.blit(image_map,(self.speed_map+600,0))
            self.screen.blit(image_map,(self.speed_map+600*2,0))
            if self.speed_map==-600:
                self.speed_map=0
                #=========
            horses1.update(bua_input[0])
            horse_x[0]=horse1.positonx
            horses2.update(bua_input[1])
            horse_x[1]=horse2.positonx
            horses3.update(bua_input[2])
            horse_x[2]=horse3.positonx
            horses4.update(bua_input[3])
            horse_x[3]=horse4.positonx
            horses5.update(bua_input[4])
            horse_x[4]=horse5.positonx
            for i in range(5):
                # kích hoạt bùa và ẩn hình ảnh bùa 
                if (horse_x[i]+50)>=self.bua_x[i] and hidden[i]:
                    hidden[i]=False
                    active[i]=True
                    bua_get[i]=random.randint(0,5) # random  bùa nhận được 
            for i in range(5):
                if active[i] and int(end_bua[i])<=160: # kiểm tra điều kiện kích hoạt bùa 
                    if 3<=bua_get[i]<=4:
                        horse[i].positonx+=bua[bua_get[i]]
                        end_bua[i]=170
                    elif bua_get[i]==5:
                        horse[i].positonx=bua[bua_get[i]]
                        end_bua[i]=170
                    else:
                        bua_input[i]=bua[bua_get[i]]
                        end_bua[i]+=1
                elif end_bua[i]>20:
                    bua_input[i]=1
                if horse[i].rect.right>=WINDOW_WIDTH and (not end_horse[i]):
                    self.rank.append(i)
                    end_horse[i]=True
                    print(self.rank)
            if len(self.rank)==5:
                return self.rank
            #=============
            horses1.draw(self.screen)
            horses2.draw(self.screen)
            horses3.draw(self.screen)
            horses4.draw(self.screen)
            horses5.draw(self.screen)
            for i in range(1, 6):
                if self.showbua and hidden[i-1]:
                    self.screen.blit(self.img_bua,(self.bua_x[i-1],40+i*105))
            pygame.display.flip()
            clock.tick(60)
pygame.init()
main_game=Game()
main_game.load_bg()
pygame.quit()

	