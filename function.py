import pygame
from constants import *
from random import randint as rnd
def Show(Surface,Snake,food):
    for sq in Snake:
        pygame.draw.rect(Surface,(255,255,255),(sq[0]*TITLE_SIZE,sq[1]*TITLE_SIZE,TITLE_SIZE,TITLE_SIZE),1)
    pygame.draw.circle(Surface,(255,0,0),(food[0]*TITLE_SIZE,food[1]*TITLE_SIZE),10)
def update(Snake, direction,food,alive):
    if direction=="RIGHT":
        if Snake[-1][0]+1>(WS[1]//TITLE_SIZE)-1:
            Snake.append([0, Snake[-1][1]])
        else:
            Snake.append([Snake[-1][0]+1, Snake[-1][1]])
    elif direction=="LEFT":
        if Snake[-1][0]-1<0:
            Snake.append([(WS[1]//TITLE_SIZE)-1, Snake[-1][1]])
        else:
            Snake.append([Snake[-1][0] - 1, Snake[-1][1]])
    elif direction=="UP":
        if Snake[-1][1]-1<0:
            Snake.append([Snake[-1][0], (WS[0]//TITLE_SIZE)-1])
        else:
            Snake.append([Snake[-1][0], Snake[-1][1] - 1])
    elif direction=="DOWN":
        if Snake[-1][1]+1>(WS[1]//TITLE_SIZE)-1:
            Snake.append([Snake[-1][0], 0])
        else:
            Snake.append([Snake[-1][0], Snake[-1][1]+1])

    if food not in Snake:
        Snake.pop(0)
    else:
        food = generate_food(Snake)

    if Snake[-1] in Snake[:-1]:
        alive=False
    return Snake,food,alive

def generate_food(snake):
    food = [rnd(0,(WS[0]//TITLE_SIZE)-1),rnd(0,WS[1]//TITLE_SIZE)]
    while food in snake:
        food = [rnd(0,(WS[0]//TITLE_SIZE)-1),rnd(0,WS[1]//TITLE_SIZE)]
    return food

