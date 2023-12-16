import pygame
#BGMを付けるためのライブラリのimport
from pygame  import mixer
pygame.init()
#スクリーンを表示するやt
screen = pygame.display.set_mode((800,600))
screen.fill((150,150,150))
running =True
#表示名を変更することができる
pygame.display.set_caption('invaders Games')



#player
img = pygame.image.load('player.png')
#X、y座標
PX=370
PY=480
playerX_change=0
def player(x,y):
    screen.blit(img,(PX,PY))



#音をならすやつ
mixer.Sound('laser.wav').play()
while running:
    #クロで上書きすることで残像を消す事ができる
    screen.fill((0,0,0))
    
    #文字のフォントを設定
    font = pygame.font.SysFont('ko',100)
    message = font.render('Hello world',False,(255,255,255))
    #HEllo worldの表示
    screen.blit(message,(240,50))
    #戦闘機の設置
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                playerX_change = -1.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            #if event.key == pygame.K_SPACE:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    PX += playerX_change  
    if PX <=0:
        PX = 0
    if PX  >736:
        PX = 736                    
    player(PX,PY)
    pygame.display.update()