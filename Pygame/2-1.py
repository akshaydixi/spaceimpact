#Draw a simple cross onto the screen using lines 
import pygame

MAX_WIDTH = 640
MAX_HEIGHT = 480

screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

running = 1
color = 0,0,0                               # Background color
linecolor = 0,0,255                         # Line color
startposition1 = 0,0                        # Top left corner
endposition1 = MAX_WIDTH-1,MAX_HEIGHT-1     # Bottom right corner
startposition2 = MAX_WIDTH-1,0              # Top right corner
endposition2 = 0,MAX_HEIGHT-1               # Bottom left corner

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    
    screen.fill(color)
    pygame.draw.line(screen,linecolor,startposition1,endposition1)   # Faster but appears jaggedy   
    pygame.draw.aaline(screen,linecolor,startposition2,endposition2) # Slower due to anti-aliasing, but gives a smoother line 
    pygame.display.flip()   # Draw onto the screen! This is very important
    
pygame.display.quit()
