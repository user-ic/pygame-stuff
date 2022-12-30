import sys
import pygame




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

    ball = pygame.image.load("assets\intro_ball.gif")
    ballrect = ball.get_rect()

    color = (255,0,0)

    while True:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == ord ( "q" )): 
                sys.exit()
            # elif event.type == pygame.KEYDOWN and event.key == ord ( "w" ): 
            #     speed[1] = -speed[1]
            # elif event.type == pygame.KEYDOWN and event.key == ord ( "a" ): 
            #     speed[1] = -speed[1]
            # elif event.type == pygame.KEYDOWN and event.key == ord ( "s" ): 
            #     speed[1] = -speed[1]
            # elif event.type == pygame.KEYDOWN and event.key == ord ( "d" ): 
            #     speed[1] = -speed[1]                
            elif event.type == pygame.KEYDOWN and event.key == ord ( "r" ): 
                speed[0] = -speed[0]
                speed[1] = -speed[1]
                break
                

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
