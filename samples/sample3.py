import sys
import pygame


#    down\up\left\right movement



def main():
    pygame.init()
    pygame.font.init() 
    
    my_font = pygame.font.SysFont('Comic Sans MS', 18)

    size = (width, height) = (600, 540)
    # 2 pixi
    speed = [1, 1]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("assets\intro_ball.gif")
    ballrect = ball.get_rect()

    color = (255,0,0)
    moveBall = False

    while True:
                                           
        keys = pygame.key.get_pressed() 
       
        if keys[pygame.K_DOWN]: 
            ballrect = ballrect.move([0, 1])  
        elif keys[pygame.K_UP]: 
            ballrect = ballrect.move([0, -1])  
        if keys[pygame.K_LEFT]: 
            ballrect = ballrect.move([-1, 0])  
        elif keys[pygame.K_RIGHT]: 
            ballrect = ballrect.move([1, 0])  

        for event in pygame.event.get():            
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == ord ( "q" )): 
                sys.exit() 


        pygame.time.wait(1)

        screen.fill(black)
        screen.blit(ball, ballrect)
        
        text_surface = my_font.render(f'ballrect=({ballrect.centerx} , {ballrect.centery})', False, color)       
        screen.blit(text_surface, (20,20))

        # draw rectangle
        pygame.draw.rect(screen, color, ballrect, width=1)
        pygame.display.flip()


if __name__ == "__main__":
    main()
