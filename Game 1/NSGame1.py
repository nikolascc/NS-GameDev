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

class Player:
	# this class creates the player object
	def __init__(self, health, shields, energy, attack):
		self.health = health
		self.shields = shields
		self.energy = energy
		self.attack = attack
	
	def render(self):
		pygame.draw.circle(gameDisplay, black, (int((SCREEN_WIDTH*0.125)),int((SCREEN_HEIGHT*0.35))), 50, 2)	

	def attack(self):
		print("Player Attacked!")
	
	def changeHealth(self, num):
		self.health += num
	
	def changeShields(self, num):
		self.shields += num
	
	def changeEnergy(self, num):
		self.energy += num
	
	def changeAttack(self, num):
		self.attack += num

class Button:
	# this class creates button objects
	def __init__(self, color, text, left, top, width, height):
		self.color = color
		self.text = text
		self.left = left
		self.top = top
		self.width = width
		self.height = height

class AttackButton(Button):
	# this class inherits from the Button class and creates the Attack Button object
	def __init__(self, color, text, left, top, width, height):
		Button.__init__(self, color, text, left, top, width, height)
		self.buttonRect = pygame.Rect(self.left, self.top, self.width, self.height)
		self.attackButtonText = Text(self.text, red, self.left+16, self.top+18)
	
	def render(self):
		pygame.draw.rect(gameDisplay, self.color, self.buttonRect, 5)
		self.attackButtonText.render()

class Score:
	# this class creates score objects
	def __init__(self, number, x, y):
		self.number = number
		self.x = x
		self.y = y
		self.font = pygame.font.SysFont(None, 25)
	
	def render(self):
		self.score = self.font.render(str(self.number), True, red)
		gameDisplay.blit(self.score,(self.x,self.y))
		
	def change(self, num):
		self.number += num
	
	def modify(self, num):
		self.number = num

class Text:
	# this class creates text objects
	def __init__(self, content, color, x, y):
		self.content = content
		self.color = color
		self.x = x
		self.y = y
		font = pygame.font.SysFont(None,25)
		self.text = font.render(self.content, True, self.color)
	
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
	clickerScore = Score(0, (SCREEN_WIDTH/2)+70, SCREEN_HEIGHT/1.65)
	energyText = Text('Energy: ', green, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/1.65))
	blockx = random.randrange((SCREEN_WIDTH/2)+10, SCREEN_WIDTH-30)
	blocky = random.randrange(10, (SCREEN_HEIGHT/2)+20)
	energyBlock1 = Energy_Block(otherbit,blockx,blocky)
	energyBlock2 = Energy_Block(otherbit,blockx,blocky)
	energyBlock3 = Energy_Block(otherbit,blockx,blocky)
	player = Player(100, 100, 0, 1)
	attackButton = AttackButton(black, "ATTACK", int(SCREEN_WIDTH*0.1125), int(SCREEN_HEIGHT/1.5), 100, 50)
	
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
					#clickerScore.change(3)
					player.changeEnergy(3)
					clickerScore.modify(player.energy)
					energyBlock1.changePos()
			pygame.display.update()
			gameDisplay.blit(background,(0,0))
			pygame.draw.line(gameDisplay, black, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT/1.7), 2)
			pygame.draw.line(gameDisplay, black, (0, SCREEN_HEIGHT/1.7), (SCREEN_WIDTH, SCREEN_HEIGHT/1.7), 2)
			player.render()
			attackButton.render()
			handle_keys()
			clickerScore.render()
			energyText.render()
			energyBlock1.render()

# call functions here
main()