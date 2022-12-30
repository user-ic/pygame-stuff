# make sample6 into oop -> class Player

import pygame
import sys

pygame.init()

my_font = pygame.font.SysFont('Comic Sans MS', 18)
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Jumping in PyGame")
BACKGROUND = pygame.image.load("assets/background.png")

color = (255,0,0)


class Player:

    def __init__(self):
        self.facing_right = True
        self.__jumping = False

        self.y_gravity = 1
        self.jump_height = 20
        self.y_velocity = self.jump_height

        self.standing_surface = pygame.transform.scale(pygame.image.load("assets/mario_standing.png"), (48, 64))
        self.jumping_surface = pygame.transform.scale(pygame.image.load("assets/mario_jumping.png"), (48, 64))

        self.surface = self.standing_surface
        self.rectangle = self.surface.get_rect(center=(400, 660))   

    def changeDirection(self, moveRight: bool):
        self.facing_right = moveRight   
        self.standing_surface = pygame.transform.flip(self.standing_surface, 1, 0)
        self.jumping_surface = pygame.transform.flip(self.jumping_surface, 1, 0)

    def move(self, keys_pressed):
        if keys_pressed[pygame.K_DOWN]: 
            self.rectangle = self.rectangle.move([0, 4])  
        elif keys_pressed[pygame.K_UP]: 
            self.rectangle = self.rectangle.move([0, -4])  
        if keys_pressed[pygame.K_LEFT]:
            self.rectangle = self.rectangle.move([-4, 0])  
        elif keys_pressed[pygame.K_RIGHT]: 
            self.rectangle = self.rectangle.move([4, 0])  

        if keys_pressed[pygame.K_SPACE]:
            self.__jumping = True
        
        self.__updateSurface()

    def __updateSurface(self):        
        if self.__jumping:
            self.y_velocity -= self.y_gravity
            
            if self.y_velocity < -self.jump_height:
                self.__jumping = False
                self.y_velocity = self.jump_height
                
            self.surface = self.jumping_surface
            
            self.rectangle = self.rectangle.move([0, -self.y_velocity])  
        else:
            self.surface = self.standing_surface

player = Player()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == ord ( "q" )): 
            pygame.quit()
            sys.exit()        

        pressed_left = event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT
        pressed_right = event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT

        if (pressed_left or pressed_right) and player.facing_right != pressed_right: 
            player.changeDirection(pressed_right)     

    keys_pressed = pygame.key.get_pressed()

    player.move(keys_pressed)

    SCREEN.blit(BACKGROUND, (0, 0))  
    SCREEN.blit(player.surface, player.rectangle)
    text_surface = my_font.render(f'ballrect=({player.rectangle.centerx} , {player.rectangle.centery})', False, color)       
    SCREEN.blit(text_surface, (20,20))

    pygame.display.update()
    CLOCK.tick(60)