import pygame
import neat
import sys
import os
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
GRAVITY = 0.1
player_pos = [100, 200]
player_size = 25
player_accel_y = 0
player_velo_y = 0

score = 0

num_pipes = 0;
pipeX = []
pipeY = []
pipeS = []

game_over = False

YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

myFont = pygame.font.SysFont("monospace", 35)

BACKGROUND_COLOUR = (55, 235, 52)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def jump(player_pos, player_velo_y, player_accel_y):
    global y
    global velo_y
    global accel_y
    
    y = player_pos[1]
    velo_y = player_velo_y
    accel_y = player_accel_y

    accel_y += GRAVITY
    velo_y += accel_y
    y += velo_y
  
def detct_hit(pipeX, pipeY, pipeS, player_pos, player_size, game_over):
    for i in range(num_pipes):
        if player_pos[0]+player_size > pipeX[i] and player_pos[0]+player_size < pipeX[i] + 70 or player_pos[0]-player_size > pipeX[i] and player_pos[0]-player_size < pipeX[i] + 70:
            if player_pos[1]-player_size < pipeS[i]:
                game_over = True
            elif player_pos[1]+player_size > pipeS[i]+200:
                game_over = True
    return game_over

while True:
    while not game_over:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN :
                player_accel_y = 0
                player_velo_y = -10

        screen.fill(BACKGROUND_COLOUR)

        clock.tick(30)

        player_pos[1] = jump(player_pos, player_velo_y, player_accel_y)
        player_pos[1] = y
        player_velo_y = velo_y
        player_accel_y = accel_y

        if player_pos[1]-(player_size) < 0:
            player_pos[1] = 0+player_size+1
            player_velo_y = 0
            player_accel_y = 0

        if player_pos[1]+(player_size) >= HEIGHT:
            player_pos[1] = HEIGHT-player_size-1
            player_velo_y = 0
            player_accel_y = 0
            game_over = True

        if num_pipes <= 1:
            pipeX.append(500*(num_pipes+1))
            pipeS.append(random.randint(150, 350))
            num_pipes += 1   

        for i in range(num_pipes):
            pipeX[i] -= 5
            pygame.draw.rect(screen, GREEN, (round(pipeX[i]), 0, 70, pipeS[i]))
            pygame.draw.rect(screen, GREEN, (round(pipeX[i]), round(pipeS[i]+200), 70, HEIGHT))
            if pipeX[i] < -70:
                score += 1
                pipeX[i] = WIDTH + 70
                pipeS[i] = random.randint(150, 350)

        pygame.draw.circle(screen, YELLOW, (round(player_pos[0]), round(player_pos[1])), player_size)
        text = "Score:" + str(score)
        label = myFont.render(text, 1 , YELLOW)
        screen.blit(label, (WIDTH-200, 40))
        pygame.display.update()
        game_over = detct_hit(pipeX, pipeY, pipeS, player_pos, player_size, game_over)
        

    while game_over:
        pygame.display.update()
        screen.fill(BLUE)
        text = "Game Over Click the Mouse to Restart"
        label = myFont.render(text, 1 , YELLOW)
        screen.blit(label, (WIDTH-775, round(HEIGHT/2)))
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             if event.type == pygame.MOUSEBUTTONDOWN :
                game_over = False
                score = 0
                player_velo_y = 0
                player_accel_y = 0
                player_pos[1] = 200
                if num_pipes > 0:
                    pipeX.pop(0)
                    pipeS.pop(0)
                    pipeX.pop(0)
                    pipeS.pop(0)
                    num_pipes = 0

