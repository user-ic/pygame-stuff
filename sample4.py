import sys
import pygame


#    down\up\left\right movement



def main():
    pygame.init()
    pygame.font.init() 
    
    my_font = pygame.font.SysFont('Comic Sans MS', 18)

    size = (width, height) = (600, 540)
    # 2 pixi
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("intro_ball.gif")
    ballrect = ball.get_rect()

    color = (255,0,0)
    speed = [0, 0]
    moveBack = False
    i = 0
    while True:
        if not moveBack:
            keys = pygame.key.get_pressed() 
        
            if keys[pygame.K_DOWN]: 
                speed = [0, 1]
                ballrect = ballrect.move([0, 1])  
            elif keys[pygame.K_UP]: 
                speed = [0, -1]
                ballrect = ballrect.move([0, -1])  
            if keys[pygame.K_LEFT]:
                speed = [-1, 0]    
                ballrect = ballrect.move([-1, 0])  
            elif keys[pygame.K_RIGHT]: 
                speed = [1, 0]    
                ballrect = ballrect.move([1, 0])  
                
            if keys[pygame.K_SPACE]: 
                i+=1
                ballrect = ballrect.move(speed)  
                if(i > 100):
                    i = 0
                    moveBack = True

            for event in pygame.event.get():            
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == ord ( "q" )): 
                    sys.exit() 
        else:
            i+=1
            ballrect = ballrect.move([-speed[0],-speed[1]]) 
            if(i > 100):
                i = 0
                moveBack = False


        pygame.time.wait(1)

        screen.fill(black)
        screen.blit(ball, ballrect)      
        
        text_surface = my_font.render(f'ballrect=({ballrect.centerx} , {ballrect.centery})', False, color)       
        screen.blit(text_surface, (20,20))

        # draw rectangle
        pygame.draw.rect(screen, color, ballrect, width=1)
        pygame.display.flip()

        # if moveBack:
        #     pygame.time.wait(1500)
        #     ballrect = ballrect.move([-speed[0],-speed[1]])  
        #     moveBack = False

if __name__ == "__main__":
    main()
