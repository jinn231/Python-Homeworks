import pygame
import sys
import os
pygame.font.init()

WIDTH, HEIGHT = 800,500
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong Game")

# BG
BackGround = pygame.transform.scale(pygame.image.load(os.path.join("Image", "space.png")), (WIDTH,HEIGHT))

# WINNER_TEXT
WINNER = pygame.font.SysFont("mallanna", 40)

# frame per second move
FPS = 60

def update_window(ball,player1,player2,Middle_Bar):
    WINDOW.blit(BackGround, (0,0))
    pygame.draw.rect(WINDOW,(0,0,0), Middle_Bar)
    pygame.draw.ellipse(WINDOW, (255,255,255), ball)
    pygame.draw.rect(WINDOW,(255,255,255), player1)
    pygame.draw.rect(WINDOW,(255,255,255), player2)
    pygame.display.update()

def player1_handler(key_pressed,player):
    if key_pressed[pygame.K_w] and player.y > 0:
        player.y -= 5
    elif key_pressed[pygame.K_s] and player.y + WIDTH/2 < WIDTH:
        player.y += 5 
        
def player2_handler(key_pressed,player):
    if key_pressed[pygame.K_UP] and player.y > 0:
        player.y -= 5
    elif key_pressed[pygame.K_DOWN] and player.y + WIDTH/2 < WIDTH:
        player.y += 5 

def winner_window(text):
        winner_text = WINNER.render(text,1, (255,255,255))
        WINDOW.blit(winner_text,(WIDTH/2 - winner_text.get_width()/2, HEIGHT/2 - winner_text.get_height()))
        pygame.display.update()
        pygame.time.delay(5000)

def Game():
    ball = pygame.Rect(WIDTH/2 - 7.5, HEIGHT/2 - 7.5, 15, 15)
    player1 = pygame.Rect(5,HEIGHT/2 - 50, 10, 100)
    player2 = pygame.Rect(WIDTH - 10,HEIGHT/2 - 50, 10, 100)

    Middle_Bar = pygame.Rect(WIDTH/2 - 1.5, 0, 3, HEIGHT)

    clock = pygame.time.Clock()
    run = True

    # Ballon VELOCITY
    BALL_VEL_x = 5
    BALL_VEL_y = 5

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        ball.x += BALL_VEL_x
        ball.y += BALL_VEL_y

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            BALL_VEL_y *= -1 

        if player1.colliderect(ball):
            BALL_VEL_x *= -1
        if player2.colliderect(ball):
            BALL_VEL_x *= -1

        key_pressed = pygame.key.get_pressed()

        player1_handler(key_pressed,player1)
        player2_handler(key_pressed,player2)

        text = ""
        if ball.x > WIDTH:
            text= "PLAYER_1 WIN!"
        elif ball.x < 0:
            text = "PLAYER_2 WIN!"

        if text != "":
            winner_window(text)
            break

        update_window(ball,player1, player2, Middle_Bar)
    main()

def main():
    Game()
