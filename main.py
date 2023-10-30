from pygame.locals import *
import pygame, sys
from random import randint as ri

""" see instructions file """

# setup pygame
pygame.init()
main_clock =pygame.time.Clock()

# setup window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_DIMENSIONS = (WINDOW_WIDTH, WINDOW_HEIGHT)

window_surface = pygame.display.set_mode( WINDOW_DIMENSIONS, 0, 32)
pygame.display.set_caption("Game Time!")

# speed
MOVE_SPEED = 10

# colours = as tuples to match RGB encoding system
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# player and food
food_counter = 0
NEW_FOOD = 40
FOOD_SIZE = 20
NUM_FOOD = 20

player = pygame.Rect(300, 100, 50, 50)
foods = []

for food in range(NUM_FOOD):
    foods.append(
        pygame.Rect(
            ri(0, WINDOW_WIDTH - FOOD_SIZE),
            ri(0, WINDOW_HEIGHT - FOOD_SIZE),
            FOOD_SIZE, FOOD_SIZE
            )
        )
#end for

# reset direction vars
move_left = False
move_down = False
move_right = False
move_up = False


exit = False
while not exit:
    
    for event in pygame.event.get():
        
        # check the event type
        if event.type == pygame.quit:
            
            pygame.QUIT()
            sys.exit()
            
        elif event.type == KEYDOWN:
            
            # which key?
            if event.key == K_LEFT or event.key == K_a:
                move_right = False
                move_left = True
            elif event.key == K_RIGHT or event.key == K_d:
                move_left = False
                move_right = True
            elif event.key == K_UP or event.key == K_w:
                move_down = False
                move_up = True    
            elif event.key == K_DOWN or event.key == K_s:
                move_up = False
                move_down = True
            #end if
            
        elif event.type == KEYUP:
            
            if event.key == K_ESCAPE:
                pygame.QUIT()
                sys.exit()
            elif event.key == K_LEFT or event.key == K_a:
                move_left = False
            elif event.key == K_RIGHT or event.key == K_d:
                move_right = False
            elif event.key == K_UP or event.key == K_w:
                move_up = False
            elif event.key == K_DOWN or event.key == K_s:
                move_down = False
            elif event.key == K_x:
                player.top = ri(0, WINDOW_HEIGHT - player.height)
            #end if

        elif event.type == MOUSEBUTTONUP:
            
            foods.append(
                pygame.Rect( event.pos[0], event.pos[1], FOOD_SIZE, FOOD_SIZE )
            )
        
        #end if
        
        # go over each food item and create RECT object in the food list
        food_counter += 1
        if food_counter == NEW_FOOD:
            food_counter = 0
            foods.append(
                pygame.Rect(
                    ri( 0, WINDOW_WIDTH - FOOD_SIZE ),
                    ri( 0, WINDOW_HEIGHT - FOOD_SIZE ),
                    FOOD_SIZE,
                    FOOD_SIZE
                    )
            )
        #end if
        
        window_surface.fill(WHITE)
        
        # adjust position of player RECT
        if move_down and player.bottom < WINDOW_HEIGHT:
            player.top += MOVE_SPEED
        elif move_up and player.top > 0:
            player.top -= MOVE_SPEED
        elif move_left and player.left > 0:
            player.left -= MOVE_SPEED
        elif move_right and player.right < WINDOW_WIDTH:
            player.right += MOVE_SPEED
        #end if
        
        # draw player
        pygame.draw.rect(window_surface, BLACK, player)
    
        # check collision
        for food in foods[:]:
            if player.colliderect(food):
                foods.remove(food)
            #end if
        #end for
        
        # draw food
        for food in range(len(foods)):
            pygame.draw.rect(window_surface, GREEN, foods[food])
        #end for
        
        pygame.display.update()
        main_clock.tick(40)
        
    #end for
    
#edn while