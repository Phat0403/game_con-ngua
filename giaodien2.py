# import pygame, sys, button
# FPS=60
# clock=pygame.time.Clock()
# WINDOW_HEIGHT = 675
# WINDOW_WIDTH = 1200
# screen=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
# pygame.display.set_caption('window')

# def option_horse():
#     running=True
#     RECT=pygame.transform.scale(pygame.image.load(r"asset/img/rect.png"),(120,120))
#     START_BTN=button.Button(610,600,0.3,pygame.image.load(r"asset/img/button_start.png"))
    
# 	# tự đổi map chỗ đây 
#     MAP=[
# 		pygame.transform.scale(pygame.image.load(r"asset\map\map1.png"),(400,200)),   #MAP1
# 		pygame.transform.scale(pygame.image.load(r"asset\map\map2.png"),(400,200)),  #MAP2
#         pygame.transform.scale(pygame.image.load(r"asset\map\map3.png"),(400,200))   #MAP3
#     ]
# 	# set 1
# 	# tự chọn con ngựa khác cũng đc 
#     HORSE1=[
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse1\1\4.png"),(100,100)),"ten1_1"], # tự đổi tên chỗ đây
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse1\2\4.png"),(100,100)),"ten1_2"],
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse1\3\4.png"),(100,100)),"ten1_3"],
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse1\4\4.png"),(100,100)),"ten1_4"],
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse1\5\4.png"),(100,100)),"ten1_5"]
# 	]
# 	#set 2
#     HORSE2=[
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse2\1\4.png"),(100,100)),"ten2_1"],
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse2\2\4.png"),(100,100)),"ten2_2"],
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse2\3\4.png"),(100,100)),"ten2_3"],
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse2\4\4.png"),(100,100)),"ten2_4"],
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse2\5\4.png"),(100,100)),"ten2_5"]
# 	]
# 	# set 3
#     HORSE3=[
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse3\1\4.png"),(100,100)),"ten3_1"],
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse3\2\4.png"),(100,100)),"ten3_2"],
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse3\3\4.png"),(100,100)),"ten3_3"],
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse3\4\4.png"),(100,100)),"ten3_4"],
# 		[pygame.transform.scale(pygame.image.load(r"asset\character\horse3\5\4.png"),(100,100)),"ten3_5"]
# 	]
#     HORSE=[HORSE1,HORSE2,HORSE3]
#     button_go_back=button.Button(50,50,0.1,pygame.image.load(r"asset/button/go_back.png"))
#     select_horse=1
#     map_select=0
#     BG_x=0
#     while running:
#         clock.tick(1000)
#         for event in  pygame.event.get():
#             if event.type==pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
# 				#right_map
#                 if button_go_back.rect.collidedict(event.pos): 
#                     pass


#                 if pygame.Rect((829,380),(130,130)).collidepoint(event.pos):
#                     if map_select==2:
#                         map_select=0
#                     else:
#                         map_select+=1
# 				#left_map
#                 if pygame.Rect((330,380),(130,130)).collidepoint(event.pos):
#                     if map_select==0:
#                         map_select=2
#                     else:
#                         map_select-=1
# 			    #right_chose_hourse
#                 if pygame.Rect((1000,182),(100,100)).collidepoint(event.pos):
#                     if select_horse==2:
#                         select_horse=0
#                     else :
#                         select_horse+=1
					
# 				#left_chose_hourse
#                 if pygame.Rect((182,190),(100,100)).collidepoint(event.pos):
#                     if select_horse==0:
#                         select_horse=2
#                     else:
#                         select_horse-=1
					
#                 if pygame.Rect((490,580),(250,100)).collidepoint(event.pos):
# 					# LẤY GIÁ TRỊ MAP VỚI 5 CON NGỰA VÀ TÊN 5 CON NGỰA ĐỂ HIỂN THỊ ĐƯỜNG ĐUA TƯƠNG ỨNG 
#                     return MAP[map_select],HORSE[select_horse]
                    
#         rect_x=260
#         rect_y=200
#         screen.blit( pygame.transform.scale( pygame.image.load("./asset/img/cloud.png").convert(), (1200, 900)),(BG_x,0))
		
#         for i in range(0,5):
#             # 5 hình vuông
#             screen.blit(RECT,(rect_x,rect_y))
#             # 5 con ngựa 
#             screen.blit(HORSE[select_horse][i][0],(rect_x+10,rect_y+10))
#             # tên 5 con ngựa 
#             screen.blit(pygame.font.Font(r'asset\img\SourceCodePro-Black.ttf',20).render(f'{HORSE[select_horse][i][1]}',True, (246, 142, 2)),(rect_x+20,rect_y-25))
#             rect_x+=150
#         screen.blit(pygame.font.Font(r'asset\img\SourceCodePro-Black.ttf',100).render(f'<',True, (246, 142, 2)),(182,190)) #đổi màu nút left tại đây 
#         screen.blit(pygame.font.Font(r'asset\img\SourceCodePro-Black.ttf',100).render(f'>',True, (246, 142, 2)),(1000,190))  #có thể đổi màu
#         screen.blit(pygame.font.Font(r'asset\img\SourceCodePro-Black.ttf',50).render(f'TÙY CHỈNH CHẾ ĐỘ',True, (246, 142, 2)),(370,50))  #có thể đổi màu 
#         screen.blit(pygame.font.Font(r'asset\img\SourceCodePro-Black.ttf',130).render(f'<',True, (246, 142, 2)),(330,300)) #có thể đổi màu
#         screen.blit(pygame.font.Font(r'asset\img\SourceCodePro-Black.ttf',130).render(f'>',True, (246, 142, 2)),(829,300)) #có thể đổi màu
#         screen.blit(MAP[map_select],(420,300))
#         screen.blit(MAP[map_select],(420,300))
#         START_BTN.draw(screen)
#         button_go_back.draw(screen)
#         pygame.display.update()
import pygame


def coin():
    screen = pygame.display.set_mode([800,800])
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
                     
        screen.fill((0,0,0))
        if active == True:
            color = color2
        pygame.draw.rect(screen,color,input_rect,2)
    
        text_surface = base_font.render(user_text,True,(255,255,255))
    
        screen.blit(text_surface,(input_rect.x +5,input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width()+10)
        pygame.display.flip()
pygame.init()
coin()
