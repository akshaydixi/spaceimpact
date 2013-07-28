#Draw a simple cross onto the screen using lines of varying color / intensity
import time   # Needed for the delay
import pygame

MAX_WIDTH = 640
MAX_HEIGHT = 480

screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

running = 1
color = 0,0,0                           # Background color
linecolorx = 0                          # Line color element
startposition1 = 0,0                    # Top left corner
endposition1 = MAX_WIDTH-1,MAX_HEIGHT-1 # Bottom right corner
startposition2 = MAX_WIDTH-1,0          # Top right corner
endposition2 = 0,MAX_HEIGHT-1           # Bottom left corner
increment = 1                           # Line color updater
while running:
    linecolorx += increment
    if linecolorx == 255: 
        increment = -1
    if linecolorx == 0: 
        increment = +1
        
    linecolor = linecolorx,linecolorx,linecolorx # Create a new linecolor everytime 
    
    
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    
    screen.fill(color)
    pygame.draw.line(screen,linecolor,startposition1,endposition1)   # Faster but appears jaggedy   
    pygame.draw.aaline(screen,linecolor,startposition2,endposition2) # Slower due to anti-aliasing, but gives a smoother line 
    pygame.display.flip() # Draw onto the screen. This is very important!
    time.sleep(0.002)  # A small delay to help with persistence of vision for human eyes
    
pygame.display.quit()
