import pygame, sys, button, giaodien2

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
                    giaodien2.option_horse()
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
        
pygame.init()
load_bg()
pygame.quit()





