
import pygame

def drawRobot(screen,x,y):
	# draw robot body (square)
        pygame.draw.rect(screen,BLUE, (x,y,robotSize,robotSize))
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

robotSpeed = 5
robotSize = 40

joysticks = []
for i in range(pygame.joystick.get_count()):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        joysticks.append(joystick)
        print(f"found joystick: {joystick.get_name()}({joystick.get_id()})")


