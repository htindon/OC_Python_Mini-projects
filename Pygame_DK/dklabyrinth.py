import pygame
from pygame.locals import *

from classes import *
from constants import *

'''
Donkey Kong Labyrinth Game
A game in which the player has to move DK through a labyrinth in order to reach bananas

Python Script
Files : dklabyrinth.py, classes.py, constants.py, n1, n2 + images
'''

pygame.init()

window = pygame.display.set_mode((window_size, window_size))

# Loading images
menu_bg = pygame.image.load(menu_bg_img)
window.blit(menu_bg, (0,0))

icon = pygame.image.load(icon_img)
pygame.display.set_icon(icon)
pygame.display.set_caption(window_title)

pygame.display.flip()

'''
This is the main loop. Upon leaving the menu, the player enters the game loop, upon living the game, the player re-enters the menu loop etc.
'''
value = 1
menu_loop_value = 1
game_loop_value = 0
while value:
    for event in pygame.event.get():
        if event.type == QUIT:
            value = 0
    # Menu loop
    while menu_loop_value:
        window.blit(menu_bg, (0,0))
        pygame.display.flip()

    # Game loop
    
    
