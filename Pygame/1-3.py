import pygame

width = input("Enter screen width: ")
height = input("Enter screen height: ")

screen = pygame.display.set_mode((width,height))
running = 1

while running:
    event = pygame.event.poll()  # Catch events and store them in a variable 
    if event.type == pygame.QUIT: # Check if the event if of a QUIT type
        running = 0 # End loop by falsifying the while loop condition

pygame.display.quit()
