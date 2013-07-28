# Draw Pikachu onto the screen
import pygame
MAX_WIDTH = 600
MAX_HEIGHT = 600


class Sprite:  # The basic building block of each entity 
    def __init__(self,xpos,ypos,filename):  # This function will run each time a Sprite object is created
        self.x = xpos   
        self.y = ypos
        self.bitmap = pygame.image.load(filename)  # loading the image
        self.bitmap.set_colorkey((0,0,0))  # Setting black to be transparent
    
    def set_position(self,xpos,ypos):
        self.x = xpos
        self.y = ypos
       
    def render(self): 
        screen.blit(self.bitmap, (self.x,self.y))  # To draw the sprite onto the screen

pikachu = Sprite(0,0,"pikachu.png")

running = 1 
color = 200,200,200            # Background color 

screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))
x = 0
y = 0

while running:
    
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEMOTION:
        x,y = event.pos
    
    screen.fill(color)
    pikachu.render()
    pygame.display.flip()

pygame.display.quit()
