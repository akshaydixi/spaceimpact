# Title  : Space Impact 1.0
# Author : Akshay Dixit
# Email  : akshaydixi@gmail.com
#------------------------------
import pygame
import random
import time


MAX_WIDTH = 640    # width of game window
MAX_HEIGHT = 480   # Height of game window
BULLETSIZE = 16    # Width / Height of bullet
SPRITESIZE = 32    # Width / Height of spaceship and enemy



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
    



def Intersect (s1_x, s1_y,s2_x,s2_y):  # A simple intersection algorithm that checks of any overlap between sprites
    if ( s1_x > s2_x-BULLETSIZE ) and (s1_x < s2_x + BULLETSIZE ) and (s1_y > s2_y - BULLETSIZE) and (s1_y < s2_y + BULLETSIZE ):
        return 1
    else:
        return 0
        


pygame.init()   # Basic initialization
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))  # Create the game window
pygame.key.set_repeat(1,1)  
pygame.display.set_caption("Space Impact 1.0")  # The main window message
background = pygame.image.load("data/background.jpg") # The background image 

enemies = []  # A list that will contain all enemy entities

x = 0

for i in range(10):
    enemies.append(Sprite(50*x + 50, 50, 'data/invader.jpg'))  # Populating the enemies list with enemy entities
    x+=1

spaceship = Sprite( 20, 400, "data/spaceship.png") # Loading the spaceship
ourbullet = Sprite( 0, 500, "data/ourbullet.png")    # Loading the bullets. Note that both enemy and our bullets are set to be off the window screen.
enemybullet = Sprite( 0, 500, "data/enemybullet.png")# Thus they are not seen by the player and will only be seen when certain events occur.

running = 1    # Main game loop flag
enemyspeed = 3 # Maintains how fast the enemy will move. You can modify this to change the difficulty. 

while running:
    screen.blit(background,(0,0))  # Set the background
    for i in range(len(enemies)):
        enemies[i].x += enemyspeed # Update enemy position
        enemies[i].render() # Display the enemy
        
    if enemies[len(enemies) - 1].x > MAX_WIDTH - SPRITESIZE:  # If enemies are going off the screen , reverse direction
        enemyspeed = -3
        for i in range(len(enemies)): # And move them forward also
            enemies[i].y += 5
   
    if enemies[0].x < SPRITESIZE: # Same here. If going off the screen, reverse direction
        enemyspeed = 3
        for i in range(len(enemies)): # Move forward again
            enemies[i].y += 5
    
    if ourbullet.y < MAX_HEIGHT and ourbullet.y > 0: # If our bullet is in the game window, keep it moving upwards 
        ourbullet.render()
        ourbullet.y -= 5
    
    if enemybullet.y >= MAX_HEIGHT and len(enemies) > 0:  # If there is no enemy bullet in the game window and there are enemies left
        randomenemyindex = random.randint(0,len(enemies)-1) # Select a random enemy and move the enemy bullet to its position
        randomenemy = enemies[randomenemyindex]
        enemybullet.x = randomenemy.x
        enemybullet.y = randomenemy.y
        
    if Intersect(spaceship.x , spaceship.y, enemybullet.x, enemybullet.y): # If spaceship intersects with enemy bullet, end game
        running = 0
    
    for i in range(0,len(enemies)-1):  
        if Intersect(ourbullet.x, ourbullet.y, enemies[i].x, enemies[i].y): # If our bullet intersects with enemy bullet,
            del enemies[i]                                                  # Delete the enemy 
    if len(enemies) == 0:              # If no more enemies remaining, end game
        running = 0
    
    event = pygame.event.poll()  # Catch events
    if event.type == pygame.QUIT:
        running = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and spaceship.x < MAX_WIDTH - BULLETSIZE: # Move the ship to the right
            spaceship.x += 5
        if event.key == pygame.K_LEFT and spaceship.x > SPRITESIZE: # Move the ship to the left
            spaceship.x -= 5
        if event.key == pygame.K_SPACE: # Move the bullet into position so it starts moving ( gives the feeling of shooting a bullet )
            ourbullet.x = spaceship.x
            ourbullet.y = spaceship.y
        if event.key == pygame.K_ESCAPE: # End game if Escape key is pressed    
            running = 0
                
    enemybullet.render() 
    enemybullet.y += 5 # Keep the enemy bullet moving downwards
    spaceship.render() # Display the spaceship
    pygame.display.flip() # Write onto the screen! This is very important!
     # A small delay for persistence of human vision
pygame.display.quit()                
exit()
