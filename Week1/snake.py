import pygame
import random
from pygame.locals import *


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Square, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((0, 200, 255))
        # self.rect = self.surf.get_rect()
        self.pos = [x, y]

i=1
j=0
size=1

pygame.init()
width=800
height=600
screen = pygame.display.set_mode((width, height))
 
snake = [Square(40, 40)]
food=Square(random.randint(0,width/20-1)*20,random.randint(0,height/20-1)*20)

# Use blit to put something on the screen

screen.blit(snake[0].surf, tuple(snake[0].pos))

screen.blit(food.surf, tuple(food.pos))

# Update the display using flip
pygame.display.flip()




gameOn = True
# Our game loop
while gameOn:
    # for loop through the event queue
    pygame.time.Clock().tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False
    keys = pygame.key.get_pressed()
    for p in range(size):
        snake[p].surf.fill((0, 0, 0))
        screen.blit(snake[p].surf, tuple(snake[p].pos)) # Remove old snake[0]
        snake[p].surf.fill((0, 200, 255))
        
    food.surf.fill((255,0,0))
    screen.blit(food.surf, tuple(food.pos))
    

    
    for p in range(size-1,0,-1):
        snake[p].pos[0] = snake[p-1].pos[0]
        snake[p].pos[1] = snake[p-1].pos[1]
    snake[0].pos[0] += 20*i
    snake[0].pos[1] += 20*j

    if keys[K_w] or keys[K_UP] and j!=1:
        i=0
        j=-1
    if keys[K_a] or keys[K_LEFT] and i!=1:
        i=-1
        j=0
    if keys[K_s] or keys[K_DOWN] and j!=(-1):
        i=0
        j=1
    if keys[K_d] or keys[K_RIGHT] and i!=(-1) :
        i=1
        j=0

    #game end by edge
    if(snake[0].pos[0]>width-20):
        gameOn=False
    if(snake[0].pos[0]<0):
        gameOn=False
    if(snake[0].pos[1]<0):
        gameOn=False
    if(snake[0].pos[1]>height-20):
    #if(snake[0].pos==580 and j==1)
        gameOn=False

    #game end by eatings itself
    for p in range(1,size):
        if(snake[0].pos==snake[p].pos):
            gameOn=False
            
    #eatings growings
    if(snake[0].pos==food.pos):
        snake.append(Square(snake[size-1].pos[0]-i*20,snake[size-1].pos[1]-j*20))
        size+=1
        snake_body=[]
        for k in range(size):   
            snake_x=snake[k].pos[0]
            snake_y=snake[k].pos[1]
            snake_body.append(int(snake_y*width/400)+int(snake_x/20))
        food_map=[f for f in range(int(height/20-1)*int(width/20-1)) if f not in snake_body]
        food_pos=random.choice(food_map)
        food=Square((food_pos%int(width/20))*20,int(food_pos/width*20)*20)


    for p in range(size):
        screen.blit(snake[p].surf, tuple(snake[p].pos)) # Put new snake[0]
    screen.blit(food.surf, tuple(food.pos))
    # Update the display using flip
    pygame.display.flip()
print(size)
pygame.quit()