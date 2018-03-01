import pygame
import intersects
import random


# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
A = (186, 212, 255)
B = (49, 66, 94)
GRAY= (136, 255, 104)
D = (56, 107, 42)
E =(22, 33, 48)
F =(84, 64, 102)
# Sound effect
click = pygame.mixer.music.load("sounds/click.ogg")
theme = pygame.mixer.music.load("sounds/theme.ogg")
yell = pygame.mixer.Sound("sounds/yell.ogg")
thunder = pygame.mixer.Sound("sounds/thunder.ogg")

#images
terror = pygame.image.load("terror.png")

# Make a player
player1 = [200, 150, 25, 25]
vel1 = [0, 0]
player1_speed = 5
score1 = 0

# make walls

wall1 =  [300, 275, 400, 25]
wall2 =  [195, 200, 200, 25]
wall3 =  [100, 100, 25, 200]
wall4 =  [350, 100, 25, 200]
wall5 =  [425, 100, 25, 200]
wall6 =  [100, 500, 25, 200]
wall7 =  [250, 500, 25, 200]
wall8 =  [500, 300, 25, 250] 
wall9 =  [350, 100, 25, 200] 
wall10 =  [425, 200,400, 25]
wall11 =  [0,445,400, 25]

walls = [wall1, wall2, wall3, wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11]
# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [380, 240, 25, 25]
coin3 = [150, 175, 25, 25]
coin4 = [475, 235, 25, 25]
coin5 = [0, 500, 25, 25]
coins = [coin1, coin2, coin3,coin4,coin5]

case = 1 
# Game loop
pygame.mixer.music.play(-1)
win = False
over = False
done = False
bad = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if left:
        vel1[0] = -player1_speed
    elif right:
        vel1[0] = player1_speed
    else:
        vel1[0] = 0

    if up:
        vel1[1] = -player1_speed
    elif down:
        vel1[1] = player1_speed
    else:
        vel1[1] = 0
        
        
    # Game logic (Check for collisions, update points, etc.)
    mouse_pos = pygame.mouse.get_pos()
    
    player1 = [mouse_pos[0], mouse_pos[1], 25, 25]
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player1[1] += vel1[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = w[1] + w[3]


    ''' get block edges (makes collision resolution easier to read) '''
    left = player1[0]
    right = player1[0] + player1[2]
    top = player1[1]
    bottom = player1[1] + player1[3]
    
    # Drawing code
    if intersects.rect_rect(wall1, player1):
        bad = True 
        color = GREEN
    else:
        color = RED

    if intersects.rect_rect(wall2, player1):
        bad = True 
        color = GREEN
    else:
        color = RED

    if intersects.rect_rect(wall3, player1):
        bad = True 
        color = GREEN
    else:
        color = RED

    if intersects.rect_rect(wall4, player1):
        bad = True 
        color = WHITE
    else:
        color = RED

    if intersects.rect_rect(wall5, player1):
        bad = True 
        color = WHITE
    else:
        color = RED

    if intersects.rect_rect(wall6, player1):
        bad = True 
        color = WHITE
    else:
        color = RED

    if intersects.rect_rect(wall7, player1):
        bad = True 
        color = WHITE
    else:
        color = RED

    if intersects.rect_rect(wall8, player1):
        bad = True 
        color = WHITE
    else:
        color = RED

    if intersects.rect_rect(wall9, player1):
       bad = True 
       color = WHITE
    else:
        color = RED

    if intersects.rect_rect(wall10, player1):
       bad = True 
       color = WHITE
    else:
        color = RED

    if intersects.rect_rect(wall11, player1):
        bad = True 
        
        color = WHITE
    else:
        color = RED
        ''' if the block is moved out of the window, nudge it back on. '''
        if left < 0:
            player1[0] = 0
        elif right > WIDTH:
            player1[0] = WIDTH - player1[2]

        if top < 0:
            player1[1] = 0
        elif bottom > HEIGHT:
            player1[1] = HEIGHT - player1[3]

    ''' get the coins '''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        print("sound!")
        
    if len(coins) == 0:
        win = True
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player1)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)

    if case == 1:
        pygame.draw.rect(screen, color, [wall1[0], wall1[1],wall1[2],wall1[3]])
        pygame.draw.rect(screen, color, [wall2[0], wall2[1],wall2[2],wall2[3]])
        pygame.draw.rect(screen, color, [wall3[0], wall3[1],wall3[2],wall3[3]])
        pygame.draw.rect(screen, color, [wall4[0], wall4[1],wall4[2],wall4[3]])
        pygame.draw.rect(screen, color, [wall5[0], wall5[1],wall5[2],wall5[3]])
        pygame.draw.rect(screen, color, [wall6[0], wall6[1],wall6[2],wall6[3]])
        pygame.draw.rect(screen, color, [wall7[0], wall7[1],wall7[2],wall7[3]])
        pygame.draw.rect(screen, color, [wall8[0], wall8[1],wall8[2],wall8[3]])
        pygame.draw.rect(screen, color, [wall9[0], wall9[1],wall9[2],wall9[3]])
        pygame.draw.rect(screen, color, [wall10[0], wall10[1],wall10[2],wall10[3]])
        pygame.draw.rect(screen, color, [wall11[0], wall11[1],wall11[2],wall11[3]])
        pygame.draw.rect(screen, WHITE, [player1[0], player1[1], player1[2], player1[3]])

    if win:
        pygame.mixer.music.pause()
        pygame.draw.rect(screen, GREEN, [0,0,800,600])
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, BLACK)
        screen.blit(text, [400, 200])
        text1 = font.render("Score:" + str(score1) , 1, BLACK)
        screen.blit(text1, [0, 0])
    
    if over:
        pygame.mixer.music.pause()
        pygame.draw.rect(screen, RED, [0,0,800,600])
        font = pygame.font.Font(None, 48)
        text = font.render("GAME OVER!", 1, BLACK)
        text1 = font.render("Score:" + str(score1), 1, BLACK)
        screen.blit(text, [400, 200])
        screen.blit(text1, [0, 0])
       
        
        
        

    if bad == True:
        screen.blit(terror ,(0,0))
        yell.play()

    
        pygame.mixer.music.pause()
        over == True
   
        
    
    
        
       
        
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()

    pygame.draw.rect(screen, WHITE, player1)
    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
