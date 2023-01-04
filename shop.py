import pygame,sys
import time
pygame.init()

screen = pygame.display.set_mode((1200,800))
#load background
pygame.display.set_caption("Shop")
background = pygame.image.load('D:\Visual studio code\Hourse racing\Betcoin\Background.png').convert() 


#create class button
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

#font for betting box
base_font = pygame.font.Font(None,32)

coin_current = 100
#create button
item1 = pygame.image.load("D:\Visual studio code\Hourse racing\pygame\image\signup.png").convert()
item2 = pygame.image.load("D:\Visual studio code\Hourse racing\pygame\image\login.png").convert()
#back = pygame.image.load("item1.png").convert_alpha()
coin = pygame.image.load("D:\Visual studio code\Hourse racing\Betcoin\coin.png").convert_alpha()
cost1 = pygame.image.load("D:\Visual studio code\Hourse racing\Betcoin\cost1.png").convert_alpha()
cost2 = pygame.image.load("D:\Visual studio code\Hourse racing\Betcoin\cost2.png").convert_alpha()
cost1_1 = pygame.image.load("D:\Visual studio code\Hourse racing\Betcoin\cost1_1.png").convert_alpha()
cost2_1 = pygame.image.load("D:\Visual studio code\Hourse racing\Betcoin\cost2_1.png").convert_alpha()
#scale
background = pygame.transform.scale(background,(1200,800))
item1 = pygame.transform.scale(item1,(300,350))
item2 = pygame.transform.scale(item2,(300,350))
coin = pygame.transform.scale(coin,(50,50))
cost1 = pygame.transform.scale(cost1,(200,100))
cost2 = pygame.transform.scale(cost2,(200,100))
cost1_1 = pygame.transform.scale(cost1_1,(100,50))
cost2_1 = pygame.transform.scale(cost2_1,(100,50))
#create Button instance
cost1_button = Button(250, 600,cost1 , 0.5)
cost2_button = Button(850,600, cost2, 0.5)
#attention


#loop
run = True
while run:
    
    screen.blit(background,(0,0))
    screen.blit(item1, (150,200))
    screen.blit(item2, (750,200))
    screen.blit(coin, (1150,0))
    temp = int(coin_current)
    count1 = 0
    count2 = 0
    if cost1_button.draw(screen) and count1 == 0:
        coin_current = str(temp-10)
    if cost2_button.draw(screen) and count2 == 0:
        coin_current = str(temp-20)
    if temp < 10:
        screen.blit(cost1_1,(250,600))
        count1 += 1
    if temp < 20:
        screen.blit(cost2_1,(850,600))
        count2 +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    coin_surface = base_font.render(str(coin_current), True, (255,255,255))
    screen.blit(coin_surface,(1120,14))


    pygame.display.update()