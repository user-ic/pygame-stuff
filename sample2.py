import sys
import pygame

'''
    stop\start movement
'''


def main():
    pygame.init()
    pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    my_font = pygame.font.SysFont('Comic Sans MS', 18)

    size = width, height = 400, 340
    # 2 pixi
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("intro_ball.gif")
    ballrect = ball.get_rect()

    color = (255,0,0)
    moveBall = False

    while True:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == ord ( "q" )): 
                sys.exit()              
            elif event.type == pygame.KEYDOWN and event.key == ord ( "r" ):                
                moveBall = True 
                speed[0] = -speed[0]
                speed[1] = -speed[1]
                break           
            elif event.type == pygame.KEYDOWN and event.key == ord ( "o" ):                 
                moveBall = True 
                break                
            elif event.type == pygame.KEYDOWN and event.key == ord ( "p" ):                
                moveBall = False                 
                break                
        
        if moveBall:
            ballrect = ballrect.move(speed)  

        # left right move in relation to x
        # top bottom move in relation to y

        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]


        pygame.time.wait(300)

        screen.fill(black)
        screen.blit(ball, ballrect)
        
        text_surface = my_font.render(f'left={ballrect.left}  right={ballrect.right}  top={ballrect.top}  bottom={ballrect.bottom}', False, color)
       
        screen.blit(text_surface, (20,20))

        # draw rectangle
        pygame.draw.rect(screen, color, ballrect, width=1)
        pygame.display.flip()


if __name__ == "__main__":
    main()