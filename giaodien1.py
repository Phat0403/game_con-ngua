import pygame, sys, button
clock=pygame.time.Clock()
FPS=60
WINDOW_HEIGHT = 675
WINDOW_WIDTH = 1200
screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('window')
def load_bg():
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
                    option_horse()

                if button_setting.rect.collidepoint(pos):
                    print('danh')
        screen.blit(cloud, (cloud_x,-50))
        screen.blit(cloud, (cloud_x+1170,-50))
        
        cloud_x-=1
        screen.blit(background, (0,-125))
        if cloud_x==-1170:
            cloud_x=0
        button_start.draw(screen)
        button_setting.draw(screen)
        pygame.display.update()


def option_horse():
    running=True
    RECT=pygame.transform.scale(pygame.image.load(r"asset/img/rect.png"),(120,120))
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
    HORSE=[HORSE1,HORSE2,HORSE3]
    button_go_back=button.Button(50,50,0.1,pygame.image.load(r"asset/button/go_back.png"))
    select_horse=1
    map_select=0
    BG_x=0
    while running:
        clock.tick(60)
        for event in  pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
				#right_map
                if button_go_back.rect.collidepoint(event.pos): 
                    running = False 


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
        screen.blit( pygame.transform.scale( pygame.image.load("./asset/img/cloud.png").convert(), (1200, 900)),(BG_x,0))
		
        for i in range(0,5):
            # 5 hình vuông
            screen.blit(RECT,(rect_x,rect_y))
            # 5 con ngựa 
            screen.blit(HORSE[select_horse][i][0],(rect_x+10,rect_y+10))
            # tên 5 con ngựa 
            screen.blit(pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf',20).render(f'{HORSE[select_horse][i][1]}',True, (246, 142, 2)),(rect_x+20,rect_y-25))
            rect_x+=150
        screen.blit(pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf',100).render(f'<',True, (246, 142, 2)),(182,190)) #đổi màu nút left tại đây 
        screen.blit(pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf',100).render(f'>',True, (246, 142, 2)),(1000,190))  #có thể đổi màu
        screen.blit(pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf',50).render(f'TÙY CHỈNH CHẾ ĐỘ',True, (246, 142, 2)),(370,50))  #có thể đổi màu 
        screen.blit(pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf',130).render(f'<',True, (246, 142, 2)),(330,300)) #có thể đổi màu
        screen.blit(pygame.font.Font(r'asset/img/SourceCodePro-Black.ttf',130).render(f'>',True, (246, 142, 2)),(829,300)) #có thể đổi màu
        screen.blit(MAP[map_select],(420,300))
        screen.blit(MAP[map_select],(420,300))
        START_BTN.draw(screen)
        button_go_back.draw(screen)
        pygame.display.update()


pygame.init()
load_bg()
pygame.quit()





