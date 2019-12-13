import pygame
import sys
import random
import Pipe_Class

GREEN = (0, 200, 0)

"""class Pipes:
    def __init__(self, tempX, tempY, tempS):
        self.x = tempX
        self.y = tempY
        self.s = tempS

    def draw():
        pygame.draw.rect(screen, GREEN, (round(x), round(y)), 30, s)"""

pygame.init()

WIDTH = 800
HEIGHT = 600
GRAVITY = 0.1
player_pos = [100, 200]
player_size = 25
speed_vaues = [0, 0]
player_accel_y = 0
player_velo_y = 0

num_pipes = 0;
pipeX = []
pipeY = []

game_over = False

YELLOW = (255, 255, 0)
BACKGROUND_COLOUR = (55, 235, 52)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

#pipes.append( Pipes(WIDTH/2, 0, 50))

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

def pipe_spawn(num_pipes, pipeX, pipeY):
    if num_pipes <= 2:
        pipeX.append(random.randint(0, WIDTH))
        pipeY.append(0)
        num_pipes += 1
        pipe_spawn(num_pipes, pipeX, pipeY)

def pipe_move(pipeX):
    pipeX += 5
    
pipe_spawn(num_pipes, pipeX, pipeY)

while not game_over:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN :
            player_accel_y = 0
            player_velo_y = -10
            print("done")


    screen.fill(BACKGROUND_COLOUR)

    clock.tick(30)

    player_pos[1] = jump(player_pos, player_velo_y, player_accel_y)
    player_pos[1] = y
    player_velo_y = velo_y
    player_accel_y = accel_y
    #player_velo_y = speed_values[0]
    #player_accel_y = speed_values[1]

    if player_pos[1]-(player_size) < 0:
        player_pos[1] = 0+player_size+1
        player_velo_y = 0
        player_accel_y = 0

    if player_pos[1]+(player_size) >= HEIGHT:
        player_pos[1] = HEIGHT-player_size-1
        player_velo_y = 0
        player_accel_y = 0

   #for i in pipes:
       # Pipes.draw()

    for i in range(num_pipes):
        pygame.draw.rect(screen, GREEN, (round(pipeX[0]), rounnd(pipeY[1])), 30, 100)


    pygame.draw.circle(screen, YELLOW, (round(player_pos[0]), round(player_pos[1])), player_size)

    pygame.display.update()


