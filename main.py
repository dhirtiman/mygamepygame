import pygame
import os

WIDTH, HEIGHT = 900, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("nunu")

WHITE = (255, 255, 255)
BLACK = (0,0,0)

BORDER = pygame.Rect(WIDTH/2 - 5,0,10,HEIGHT)

FPS = 60
VEL = 5

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 95, 80

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceshipyelo.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceshipred.png'))




YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)


def draw_window(red , yellow):
    WIN.fill((WHITE))
    pygame.draw.rect(WIN,BLACK,BORDER)

    WIN.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    pygame.display.update()


def yellow_handle_movement(keys_pressed , yellow):
    if keys_pressed[pygame.K_w] and yellow.y - VEL > -17 : #UP
            yellow.y -=VEL
    if keys_pressed[pygame.K_a] and yellow.x -VEL > 0 :   #LEFT
            yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x +VEL + yellow.width -16 < BORDER.x:   #RIGHT
            yellow.x += VEL
    if keys_pressed[pygame.K_s] and yellow.y +VEL + yellow.height -16 < HEIGHT-23:   #DOWN
            yellow.y += VEL

def red_handle_movement(keys_pressed , red):
     
    if keys_pressed[pygame.K_UP] and red.y - VEL > -17 : #UP
            red.y -=VEL
    if keys_pressed[pygame.K_LEFT] and red.x -VEL > BORDER.x+7 :   #LEFT
            red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x -VEL < WIDTH-red.width+15 :   #RIGHT
            red.x += VEL
    if keys_pressed[pygame.K_DOWN] and red.y +VEL + red.height -16 < HEIGHT-23:   #DOWN
            red.y += VEL
     

def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        
        



        draw_window(red, yellow)

    pygame.quit()


if __name__ == "__main__":
    main()
