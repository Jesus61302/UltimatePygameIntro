import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score = current_time // 1000
    score_surf = test_font.render(f"Score: {score}", False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    # pygame.draw.rect(screen, '#c0e8ec', score_rect)
    # pygame.draw.rect(screen,'#c0e8ec', score_rect, 10)
    screen.blit(score_surf,score_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
pygame.display.set_caption("Runner")
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_status = 0
start_time = 0

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

# score_surf = test_font.render('score: ' , False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft = (800,300))

snail_x_pos = 600
snail_y_pos = 265

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_status == 1:
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20        
        
        if game_status == 0:
            if event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    snail_rect.left = 800
                    start_time = pygame.time.get_ticks()
                    game_status = 1
                       
    if game_status == 1:
        screen.blit(ground_surf, (0,300))
        screen.blit(sky_surf,(0,0))
        display_score()

        snail_rect.left -= 5
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300 : player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        #collisions
        if snail_rect.colliderect(player_rect):
            game_status = 0

    elif game_status == 0:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)

    pygame.display.update()
    clock.tick(60)

