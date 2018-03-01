# Imports
import pygame


# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Game Stages Demo"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Fonts
MY_FONT = pygame.font.Font(None, 50)


# stages
START = 0
PLAYING = 1
END = 2


def setup():
    global block_pos, block_vel, size, stage, time_remaining, ticks
    
    block_pos = [375, 275]
    block_vel = [0, 0]
    size = 50

    stage = START
    time_remaining = 10
    ticks = 0


# Game loop
setup()
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    
            elif stage == PLAYING:
                if event.key == pygame.K_LEFT:
                    block_vel[0] -= 2
                elif event.key == pygame.K_RIGHT:
                    block_vel[0] += 2
                elif event.key == pygame.K_UP:
                    block_vel[1] -= 2
                elif event.key == pygame.K_DOWN:
                    block_vel[1] += 2
                    
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()


    # Game logic
    if stage == PLAYING:
        ''' move block '''
        block_pos[0] += block_vel[0]
        block_pos[1] += block_vel[1]

        ''' end game on wall collision '''
        if block_pos[0] < 0 or block_pos[0] > 950 or \
           block_pos[1] < 0 or block_pos[1] > 650:
            stage = END
            

    ''' timer stuff '''
    if stage == PLAYING:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END
            ''' and other stuff could happen here too '''
            
    
    # Drawing code
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [block_pos[0], block_pos[1], size, size]) 

    ''' timer text '''
    timer_text = MY_FONT.render(str(time_remaining), True, WHITE)
    screen.blit(timer_text, [50, 50])
    
    ''' begin/end game text '''
    if stage == START:
        text1 = MY_FONT.render("Block", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to play.)", True, WHITE)
        screen.blit(text1, [350, 150])
        screen.blit(text2, [225, 200])
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window on quit
pygame.quit()
