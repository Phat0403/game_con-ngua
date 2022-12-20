import pygame,sys
class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x, pox_y) :
        super().__init__()
        
        self.sprites=[]
        self.sprites.append(pygame.image.load('D:\python\python dang nhap\Main login\ice-horse-run-01.png'))
        self.sprites.append(pygame.image.load('D:\python\python dang nhap\Main login\ice-horse-run-02.png'))
        self.sprites.append(pygame.image.load('D:\python\python dang nhap\Main login\ice-horse-run-03.png'))
        self.sprites.append(pygame.image.load('D:\python\python dang nhap\Main login\ice-horse-run-04.png'))
        self.sprites.append(pygame.image.load('D:\python\python dang nhap\Main login\ice-horse-run-05.png'))
        self.sprites.append(pygame.image.load('D:\python\python dang nhap\Main login\ice-horse-run-06.png'))
        self.sprites.append(pygame.image.load('D:\python\python dang nhap\Main login\ice-horse-run-07.png'))

        self.current_sprite=0
        self.image=self.sprites[self.current_sprite]
        self.rect=self.image.get_rect(topleft=(pos_x,pox_y))
    
    def update(self,speed):
        self.rect.x+=1
       
        self.current_sprite+=speed
        if self.current_sprite>= len(self.sprites):
            self.current_sprite=0
        self.image=self.sprites[int(self.current_sprite)]


moving_sprite=pygame.sprite.Group()
player=Player(0,200)
moving_sprite.add(player)
pygame.init()
screen=pygame.display.set_mode((925,500))
pygame.display.set_caption('Ngua')
clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        
            
    screen.fill(('gray'))
    moving_sprite.draw(screen)
    moving_sprite.update(0.2)
    pygame.display.flip()
    clock.tick(60)