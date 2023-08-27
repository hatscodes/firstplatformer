import pygame

#playform
platform_x =  0
platform_y = 400
platform_width = 880
platform_lenght = 100

#player
player_x = 0
player_y = 0
player_width = 20
player_leght = 20
player_speed = 10
#colors
white = (255,255,255)
blue =(0,0,200)
red=(255,0,0)
pygame.init()
run = True
#screen
screen = pygame.display.set_mode((720,480))
pygame.display.set_caption("platformer")
#misc
fps_limit = pygame.time.Clock()
gravity = True
while run:
    screen.fill((blue))
    #assets
    player=pygame.Rect(player_x,player_y,player_width,player_leght)
    pygame.draw.rect(screen,red,player)

    platform = pygame.Rect(platform_x,platform_y,platform_width,platform_lenght)
    pygame.draw.rect(screen,white,platform)
    #collisons
    if player.colliderect(platform) == False:
        player_y += 1
    if player.colliderect(platform) == True:
        player_y = player_y
    #controls
    key = pygame.key.get_pressed()

    if key[pygame.K_d] == True:
        player_x += player_speed
    if key[pygame.K_w] == True:
        player_y -= 3
    if key[pygame.K_a] == True:
        player_x -= player_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    fps_limit.tick(60)
print(player_y)
pygame.quit()