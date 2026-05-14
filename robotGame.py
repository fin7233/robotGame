
import pygame

def drawRobot(screen,x,y,colour):
	# draw robot body (square)
        pygame.draw.rect(screen,colour, (x,y,robotSize,robotSize))
        # draw robot eyes (circles)
        pygame.draw.circle(screen,WHITE,(x+10,y+10),5)
        pygame.draw.circle(screen,WHITE,(x+30,y+10),5)
        

pygame.init()
pygame.joystick.init()


SCREENWIDTH = 1280
SCREENHEIGHT = 800
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("Lesson 6 - Controllers")


WHITE = (255,255,255)
BLUE = (0,0,255)
PURPLE = (128,64,192)

robotX = SCREENWIDTH // 2
robotY = SCREENHEIGHT // 2

robotColour = BLUE
robotSpeed = 15
robotSize = 40

joysticks = []
for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        joysticks.append(joystick)
        print(f"found joystick: {joystick.get_name()}({joystick.get_id()})")


running = True
clock = pygame.time.Clock()


while running:
        for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 0:
                                robotColour = (255,0,0)
                        elif event.button == 1:
                                robotColour = (0,255,0)
                        elif event.button == 2:
                                robotColour = BLUE
                if event.type == pygame.QUIT:
                        running = False
                
        if joysticks:
                joystick = joysticks[0]
                # comment
                dx = joystick.get_axis(0) * robotSpeed
                dy = joystick.get_axis(1) * robotSpeed
                # 
                robotX = max(0,min(SCREENWIDTH - robotSize, robotX + dx))
                robotY = max(0,min(SCREENHEIGHT - robotSize, robotY + dy))
                #
                screen.fill(PURPLE)
                drawRobot(screen,robotX,robotY,robotColour)
                pygame.display.flip()
                clock.tick(60)

pygame. quit()