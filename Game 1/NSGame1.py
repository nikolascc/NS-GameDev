import pygame
import time
import random

# initialize screen & colours
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,200,0)
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('NS Game 1')

# set clock & speed
clock = pygame.time.Clock()
clock.tick(60)

# load images into the game
background_img = pygame.image.load('firstscreen.png')
otherbit = pygame.image.load('otherbit.png')

class Score:
	# this class creates score objects
	def __init__(self, x, y):
		self.number = 0
		self.x = x
		self.y = y
		self.font = pygame.font.SysFont(None, 25)
	
	def render(self):
		self.score = self.font.render(str(self.number), True, red)
		gameDisplay.blit(self.score,(self.x,self.y))
		
	def change(self, num):
		self.number += num

class Text:
	# this class creates text objects
	def __init__(self, content, x, y):
		self.content = content
		self.x = x
		self.y = y
		font = pygame.font.SysFont(None,25)
		self.text = font.render(self.content, True, green)
	
	def render(self):
		gameDisplay.blit(self.text,(self.x,self.y))

class Energy_Block:
	# this class creates an energy block
	def __init__(self, image, x, y):
		self.x = x
		self.y = y
		self.image = image

	def render(self):
		gameDisplay.blit(self.image,(self.x, self.y))
	
	def changePos(self):
		self.x = random.randrange((SCREEN_WIDTH/2)+10, SCREEN_WIDTH-40)
		self.y = random.randrange(10, (SCREEN_HEIGHT/2)+20)

	def position(self):
		return self.x, self.y

def handle_clicks():
	print('clicked!')
	clickx, clicky = pygame.mouse.get_pos()
	#if clickx >= energyBlock1.position()[0] and clickx <= (energyBlock1.position()[0]+30) and clicky >= energyBlock1.position()[1] and clicky <= (energyBlock1.position()[1]+30):
	#	print('handled click!')
	return clickx, clicky

def handle_keys():
	# this function handles all keyboard input
	
	key = pygame.key.get_pressed()
	

def main():
	# main function
	
	# initializations
	clickerScore = Score((SCREEN_WIDTH/2)+70, SCREEN_HEIGHT/1.65)
	energyText = Text('Energy: ', (SCREEN_WIDTH/2), (SCREEN_HEIGHT/1.65))
	blockx = random.randrange((SCREEN_WIDTH/2)+10, SCREEN_WIDTH-30)
	blocky = random.randrange(10, (SCREEN_HEIGHT/2)+20)
	energyBlock1 = Energy_Block(otherbit,blockx,blocky)
	energyBlock2 = Energy_Block(otherbit,blockx,blocky)
	energyBlock3 = Energy_Block(otherbit,blockx,blocky)
	
	# fill background
	background = pygame.Surface(gameDisplay.get_size())
	background = background.convert()
	background.fill(white)
	#line = pygame.draw.line(gameDisplay, black, (0, SCREEN_WIDTH/2), (SCREEN_HEIGHT, SCREEN_WIDTH/2), 1)
	
	##### GAME LOOP #####
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				click = handle_clicks()
				if click[0] >= energyBlock1.position()[0] and click[0] <= (energyBlock1.position()[0]+30) and click[1] >= energyBlock1.position()[1] and click[1] <= (energyBlock1.position()[1]+30):
					clickerScore.change(3)
					energyBlock1.changePos()
			pygame.display.update()
			gameDisplay.blit(background,(0,0))
			pygame.draw.line(gameDisplay, black, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT/1.7), 2)
			pygame.draw.line(gameDisplay, black, (0, SCREEN_HEIGHT/1.7), (SCREEN_WIDTH, SCREEN_HEIGHT/1.7), 2)
			handle_keys()
			clickerScore.render()
			energyText.render()
			energyBlock1.render()

# call functions here
main()