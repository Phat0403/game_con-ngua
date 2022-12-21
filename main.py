import pygame,sys,random
FPS=60
clock=pygame.time.Clock()
WINDOW_HEIGHT=700
WINDOW_WIDTH=1200
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

class Horse(pygame.sprite.Sprite):
    def __init__(self,pos_x, pox_y, type):
        super().__init__()
        self.type = type
        
        self.sprites=[]
        for i in range(7):
            image = pygame.image.load(f"./asset/character/horse1/{self.type}/{i+1}.png")
            scale = image.get_width() / image.get_height()
            image = pygame.transform.scale(image, (scale * 100, 100))
            self.sprites.append(image)
	        
        self.current_sprite=0
        self.image=self.sprites[self.current_sprite]
        self.rect=self.image.get_rect(topleft=(pos_x,pox_y))
    
    def update(self,speed):
        self.rect.x+=1
       
        self.current_sprite+=speed
        if self.current_sprite>= len(self.sprites):
            self.current_sprite=0
        self.image=self.sprites[int(self.current_sprite)]
class GameHorse():
    def __init__(self):
        self.scroll = 0
        self.direction_scroll = 1
        image = pygame.image.load("D:/NII/asset/img/backround.png").convert()
        scale = int(image.get_width() / image.get_height())
        self.back_ground_image = pygame.transform.scale(image,(scale * 1200, 700))
        
    def main(self):
        running =True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.show_menu()
            clock.tick(FPS)
    
    def show_menu(self):
        img_button=pygame.image.load("D:/NII/asset/button/start.png")
        scale1 = int(img_button.get_width() / img_button.get_height())
        self.start_button = pygame.transform.scale(img_button,(scale1 * 100, 100))
        
        main_menu_run=True
        while main_menu_run:
            self.show_bg()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.start_button.rect.collidepoint(pos):
                        self.start_new_round()
            
                self.back_ground_image.blit(self.start_button, (550, 200))
                
                pygame.display.update()
                clock.tick(FPS)
    def show_bg(self):
        display_surface.blit(self.back_ground_image, (0, 0))
        pygame.display.flip()
    def start_new_round(self):
        
        moving_sprite=pygame.sprite.Group()
        for i in range(5):
            horse = Horse(0, 100*i,i+1)
            moving_sprite.add(horse)
        running = True
        while running:
            for event in pygame.event.get():
                pygame.quit()
                sys.exit()
            display_surface.fill(('gray'))
            moving_sprite.draw(display_surface)
            moving_sprite.update(0.2)
            pygame.display.flip()
            clock.tick(60)
pygame.init()
my_game=GameHorse()
my_game.main()
