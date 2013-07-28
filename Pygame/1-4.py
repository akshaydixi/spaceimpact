import pygame

width = input("Enter screen width: ")
height = input("Enter screen height: ")

running = 1
color = 255,0,0   # R,G,B values for color

screen = pygame.display.set_mode((width,height))

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    screen.fill(color)    # Set the background color
    pygame.display.flip() # Draw onto the screen! This is very important!
    
pygame.display.quit()
