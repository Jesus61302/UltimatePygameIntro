import pygame
from sys import exit
from random import randint

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score = current_time // 1000
    score_surf = test_font.render(f"Score: {score}", False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    # pygame.draw.rect(screen, '#c0e8ec', score_rect)
    # pygame.draw.rect(screen,'#c0e8ec', score_rect, 10)
    screen.blit(score_surf,score_rect)
    return score

def obsticle_movement(obsticle_list):
    if obsticle_list:
        for obsticle_rect in obsticle_list:
            obsticle_rect.x -= 5
            if obsticle_rect.bottom == 300:
                screen.blit(snail_surf,obsticle_rect)
            else:
                screen.blit(fly_surf,obsticle_rect)
        obsticle_list = filter(lambda obsticle: obsticle.x < -50 , obsticle_list)

        return obsticle_list
    else: return []

def collisions(player,obsticles):
    if obsticles:
        for obsticle_rect in obsticles:
            if player.colliderect(obsticle_rect): return False
    return True


pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
pygame.display.set_caption("Runner")
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_status = 0
start_time = 0
score = 0

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

# score_surf = test_font.render('score: ' , False, (64,64,64))
# score_rect = score_surf.get_rect(center = (400,50))

#Obsticles
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft = (800,300))

snail_x_pos = 600
snail_y_pos = 265

fly_surf = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

obsticle_rect_list = []

#Player
player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#Intro Screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render("Pixel Runner", False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render("Press Space to Run", False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400,320) )


#Timer
obsticle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obsticle_timer,1500)

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
                    obsticle_rect_list.clear()
                    start_time = pygame.time.get_ticks()
                    game_status = 1
        
        if event.type == obsticle_timer and game_status:
            if randint(0,2):
               obsticle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100), 300))) 
            else:
                obsticle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100), 210))) 


    if game_status == 1:
        screen.blit(ground_surf, (0,300))
        screen.blit(sky_surf,(0,0))
        score = display_score()

        # snail_rect.left -= 5
        # if snail_rect.right < 0:
        #     snail_rect.left = 800
        # screen.blit(snail_surf, snail_rect)

        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300 : player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        #obsticle movement
        obsticle_movement(obsticle_rect_list)

        #collisions
        game_status = collisions(player_rect, obsticle_rect_list)

    elif game_status == 0:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        player_rect.midbottom = (80,300)
        player_gravity = 0

        score_message = test_font.render(f"Your score: {score}" ,False , (111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)

