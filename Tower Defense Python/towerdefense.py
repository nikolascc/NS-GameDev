import pygame
import time
import random

# initialize screen & colors
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,200,0)
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Tower Defense')

# set clock & speed
clock = pygame.time.Clock()
clock.tick(60)

#this line can load pngs into the game
#block = pygame.image.load('otherbit.png')

def handle_keys():
	# This function handles all user input
	key = pygame.key.get_pressed()

def main():
	# main function
	
	# fill background
	background = pygame.Surface(gameDisplay.get_size())
	background = background.convert()
	background.fill(white)
	
	##### EVENT LOOP #####
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			pygame.display.update()
			gameDisplay.blit(background,(0,0))
			handle_keys()

# call functions here
main()