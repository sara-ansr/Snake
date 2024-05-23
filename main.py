import pygame
import sys
from init import *
from constants import *
from function import *

direction="RIGHT"
clock=pygame.time.Clock()
food = generate_food(Snake)
alive=True
while alive:
    game_display.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP and direction!="DOWN":
                direction="UP"
            elif event.key==pygame.K_DOWN and direction!="UP":
                direction="DOWN"
            elif event.key==pygame.K_RIGHT and direction!="LEFT":
                direction="RIGHT"
            elif event.key==pygame.K_LEFT and direction!="RIGHT":
                direction="LEFT"
    Snake,food,alive=update(Snake, direction,food, alive)
    Show(game_display,Snake,food)
    pygame.display.update()
    clock.tick(5)