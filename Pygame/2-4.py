#Making a simple moving color bar
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
barheight = 124                             # Height of the color bar            

#Initializing the colors of the color bar
barcolor = []
for i in range(1,63):
    barcolor.append((0,0,i*4))   # Inserting color elements into the list
for i in range(1,63):
    barcolor.append((0,0,255 - i*4))  # Inserting color elements into the list

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    
    
    screen.fill(color)
    for i in range(0,barheight):
        startposition = 0,y+i
        endposition = MAX_WIDTH-1,y+i
        pygame.draw.line(screen,barcolor[i],startposition,endposition)  # Try using pygame.draw.aaline and notice the difference in speeds!
    
    y += direction
    
    if y + barheight > MAX_HEIGHT-1 or y < 0 :
        direction *= -1
    
    pygame.display.flip()
    #time.sleep(0.005)
pygame.display.quit()
