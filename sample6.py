import pygame
import sys

pygame.init()

my_font = pygame.font.SysFont('Comic Sans MS', 18)

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Jumping in PyGame")

X_POSITION, Y_POSITION = 400, 660

jumping = False

Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

STANDING_MARIO = pygame.transform.scale(pygame.image.load("assets/mario_standing.png"), (48, 64))
JUMPING_MARIO = pygame.transform.scale(pygame.image.load("assets/mario_jumping.png"), (48, 64))
CURRENT_MARIO = STANDING_MARIO
BACKGROUND = pygame.image.load("assets/background.png")

color = (255,0,0)
mario_rect = CURRENT_MARIO.get_rect(center=(X_POSITION, Y_POSITION))

while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == ord ( "q" )): 
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_DOWN]: 
        mario_rect = mario_rect.move([0, 10])  
    elif keys_pressed[pygame.K_UP]: 
        mario_rect = mario_rect.move([0, -10])  
    if keys_pressed[pygame.K_LEFT]:
        mario_rect = mario_rect.move([-10, 0])  
    elif keys_pressed[pygame.K_RIGHT]: 
        mario_rect = mario_rect.move([10, 0])  

    if keys_pressed[pygame.K_SPACE]:
        jumping = True

    SCREEN.blit(BACKGROUND, (0, 0))
    
    if jumping:
        Y_VELOCITY -= Y_GRAVITY
        
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
            
        CURRENT_MARIO = JUMPING_MARIO
        
        mario_rect = mario_rect.move([0, -Y_VELOCITY])  
    else:
        CURRENT_MARIO = STANDING_MARIO

    SCREEN.blit(CURRENT_MARIO, mario_rect)

    text_surface = my_font.render(f'ballrect=({mario_rect.centerx} , {mario_rect.centery})', False, color)       
    SCREEN.blit(text_surface, (20,20))

    pygame.display.update()
    CLOCK.tick(60)