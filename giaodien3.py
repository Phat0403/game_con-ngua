import pygame, sys, random
import playsound
WINDOW_WIDTH =1200
WINDOW_HEIGHT =675

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock=pygame.time.Clock()
FPS=60





class Horse(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, type,ran):
        super().__init__()
        
        self.type = type
        self.speed=1
        self.animate_fps = .2
        self.sprites = []
        for i in range(7):
            image = pygame.image.load(f"./asset/character/horse{main_game.index}/{self.type}/{i + 1}.png")
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
			
            
            self.positonx += (random.randint(2,400)/400)*bua
            
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
        for i in range(0,5):
            self.bua_x.append(random.randint(200,800))
        #tien
        #tien
        #tien
        self.coin=1000
        #loai ngua
        self.index=2
        #loai map
        self.map=1
        #chay map
        self.stop_map=0
        self.speed_map=2
    
    def maingame(self):
        horse1=Horse(0,480+ 50* 0 , 0 + 1,1)
        horses1= pygame.sprite.Group()
        horses1.add(horse1)    
        horse2=Horse(0,480+ 50* 1 , 1 + 1,1)
        horses2= pygame.sprite.Group()
        horses2.add(horse2)    
        horse3=Horse(0,480+ 50* 2 , 2 + 1,1)
        horses3= pygame.sprite.Group()
        horses3.add(horse3)    
        horse4=Horse(0,480+ 50* 3 , 3 + 1,1)
        horses4= pygame.sprite.Group()
        horses4.add(horse4)    
        horse5=Horse(0,480+ 50* 4 , 4 + 1,1)
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
            image=pygame.image.load(f'./asset/map/map{self.map}.png')
            scale = image.get_width() / image.get_height()
            image_map=pygame.transform.scale(image,(scale * 800, 450))
            self.screen.blit(self.background,(0,0))
            self.speed_map-=2
            self.screen.blit(image_map,(self.speed_map,250))
            self.screen.blit(image_map,(self.speed_map+600,250))
            self.screen.blit(image_map,(self.speed_map+600*2,250))
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
                    self.screen.blit(self.img_bua,(self.bua_x[i-1],300+i*50))
            pygame.display.flip()
            clock.tick(60)

pygame.init()
main_game=Game()
main_game.maingame()
pygame.quit()