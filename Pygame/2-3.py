#Moving things around
import pygame
import time    # Needed for the delay

MAX_WIDTH = 640
MAX_HEIGHT = 480

screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

running = 1
y = 0                                       # Displacement of line along y - axis                
direction = 1                               # Direction of motion  (  1 : Down , -1 : Up )
color = 0,0,0                               # Background color
linecolor = 0,0,255                         # Line color


while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    
    startposition = 0,y
    endposition  = MAX_WIDTH-1,y
    
    
    screen.fill(color)
    pygame.draw.line(screen,linecolor,startposition,endposition)   # 
    pygame.display.flip()   # Draw onto the screen! This is very important
    time.sleep(0.005)
    #Update y for the next iteration
    y += direction
    if y == 0 or y == MAX_HEIGHT-1 :     # Check if hitting window limits
        direction = direction * -1       # Invert the direction of motion
     
pygame.display.quit()
