#Mouse motion capture
import pygame

MAX_WIDTH = 640
MAX_HEIGHT = 480

x = 0  # Variable to hold mouse abcissa
y = 0  # Variable to hold mouse ordinate
running = 1 
color = 0,0,0  # Background color 

screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))


while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEMOTION :   # Event to check if mouse has been moved
        x,y = event.pos
        print "Mouse at (",x,",",y,")"           # Mouse co-ordinates
    
    screen.fill(color)
    pygame.display.flip()

pygame.display.quit()
