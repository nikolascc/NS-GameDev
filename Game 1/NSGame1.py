import pygame
import time
import random
import math

# initialize screen & colours
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,255)
cyan = (0, 255, 255)
firebrick = (178, 38, 34)
orange_red = (255, 69, 0)
light_slate_gray = (119, 136, 153)
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('NS Game 1')

# set clock & speed
clock = pygame.time.Clock()
clock.tick(60)

# load images into the game
background_img = pygame.image.load('firstscreen.png')
otherbit = pygame.image.load('otherbit.png')
metalmesh = pygame.image.load('metalmesh.png')

class Player:
	# this class creates the player object
	def __init__(self, hull, energy):
		self.hull = hull
		self.energy = energy
		self.color = black

	def render(self):
		pygame.draw.circle(gameDisplay, self.color, (int((SCREEN_WIDTH*0.08)),int((SCREEN_HEIGHT*0.42))), 50, 5)

	def attack(self):
		print("Player Attacked!")

	def changeHull(self, num):
		self.hull += num

	def changeEnergy(self, num):
		self.energy += num

class Enemy:
	# this class creates the enemy object
	def __init__(self, hull):
		self.hull = hull
		self.enemyRect = pygame.Rect(SCREEN_WIDTH/2.75, SCREEN_HEIGHT/9, 75, 75)
		#self.pointList = [(0,3()), (,), (,)]

	def render(self):
		#pygame.draw.polygon(gameDisplay, red, )
		pygame.draw.rect(gameDisplay, red, self.enemyRect, 5)

	def changeHull(self, num):
		self.hull += num

class TriangleEnemy:
	def __init__(self, a):
		self.a = a
		self.pointList = [(50,((3*(self.a))*math.sqrt(3))), (3*(self.a),50), (-3*(self.a),50)]
		#self.pointList = [(0,50), (30,0), (-30,0)]

	def render(self):
		pygame.draw.polygon(gameDisplay, red, self.pointList, 5)

class Button:
	# this class creates button objects
	def __init__(self, color, text, left, top, width, height):
		self.color = color
		#self.background_color = background_color
		self.text = text
		self.left = left
		self.top = top
		self.width = width
		self.height = height

class ActionButton(Button):
	# this class inherits from the Button class and creates the Attack Button object
	def __init__(self, color, text, left, top, width, height):
		Button.__init__(self, color, text, left, top, width, height)
		self.buttonRect = pygame.Rect(self.left, self.top, self.width, self.height)
		self.backgroundRect = pygame.Rect(self.left-3, self.top-3, self.width+6, self.height+6)
		self.attackButtonText = Text(self.text, red, self.left+(self.width/2)-75, self.top+(self.height/2)-10, 50)
		self.cooldown = False

	def render(self):
		pygame.draw.rect(gameDisplay, black, self.backgroundRect, 0)
		pygame.draw.rect(gameDisplay, self.color, self.buttonRect, 0)
		self.attackButtonText.render()

	def changeCooldown(self, flag):
		self.cooldown = flag

class Score:
	# this class creates score objects
	def __init__(self, number, x, y, background=False):
		self.number = number
		self.x = x
		self.y = y
		self.font = pygame.font.SysFont(None, 25)
		self.background = background
		if self.background == True:
			if self.number >= 100:
				self.scoreRect = pygame.Rect(self.x-3, self.y-3, 35, 23)
			else:
				self.scoreRect = pygame.Rect(self.x-3, self.y-3, 23, 23)

	def render(self):
		self.score = self.font.render(str(self.number), True, red)
		if self.background == True:
			pygame.draw.rect(gameDisplay, white, self.scoreRect, 0)
			if self.number >= 100:
				self.scoreRect = pygame.Rect(self.x-3, self.y-3, 35, 23)
			else:
				self.scoreRect = pygame.Rect(self.x-3, self.y-3, 23, 23)
		gameDisplay.blit(self.score,(self.x,self.y))

	def change(self, num):
		self.number += num

	def modify(self, num):
		self.number = num

class Text:
	# this class creates text objects
	def __init__(self, content, color, x, y, size, background=False):
		self.content = content
		self.color = color
		self.x = x
		self.y = y
		self.size = size
		font = pygame.font.SysFont(None,self.size)
		self.text = font.render(self.content, True, self.color)
		self.background = background
		if self.background == True:
			self.textRect = pygame.Rect(self.x-3, self.y-3, 71, 23)
	
	def render(self):
		if self.background == True:
			pygame.draw.rect(gameDisplay, white, self.textRect, 0)
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
	return clickx, clicky

def handle_keys():
	# this function handles all keyboard input
	key = pygame.key.get_pressed()

def main():
	# main function

	# initializations
	clickerScore = Score(0, (SCREEN_WIDTH/1.5)+70, SCREEN_HEIGHT/1.65, True)
	energyText = Text('Energy: ', green, (SCREEN_WIDTH/1.5), (SCREEN_HEIGHT/1.65), 25, True)
	healthText = Text('Health: ', green, (SCREEN_WIDTH/2), (SCREEN_HEIGHT/1.65), 25, True)
	blockx = random.randrange((SCREEN_WIDTH/2)+10, SCREEN_WIDTH-30)
	blocky = random.randrange(10, (SCREEN_HEIGHT/2)+20)
	energyBlock1 = Energy_Block(otherbit,blockx,blocky)
	energyBlock2 = Energy_Block(otherbit,blockx,blocky)
	energyBlock3 = Energy_Block(otherbit,blockx,blocky)
	enemy = Enemy(100)
	player = Player(100, 0)
	healthScore = Score(player.hull, (SCREEN_WIDTH/2)+65, (SCREEN_HEIGHT/1.65), True)
	enemyHullPoints = Score(enemy.hull, SCREEN_WIDTH/2.75, (SCREEN_HEIGHT/9)-20)
	attackButton = ActionButton(orange_red, "ATTACK", int(SCREEN_WIDTH*0.0125), int(SCREEN_HEIGHT/1.5), 200, 100)
	shieldButton = ActionButton(cyan, "SHIELDS", int(SCREEN_WIDTH*0.2125), int(SCREEN_HEIGHT/1.5), 200, 100)
	renderableObjects = [player, enemy, healthScore, enemyHullPoints, attackButton, shieldButton, clickerScore, energyText, healthText, energyBlock1]
	time = 0
	second = 0
	shieldTime = 0
	
	
	# fill background
	background = pygame.Surface(gameDisplay.get_size())
	background = background.convert()
	background.fill(white)
	
	##### GAME LOOP #####
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				click = handle_clicks()
				if click[0] >= energyBlock1.position()[0] and click[0] <= (energyBlock1.position()[0]+30) and click[1] >= energyBlock1.position()[1] and click[1] <= (energyBlock1.position()[1]+30):
					player.changeEnergy(3)
					clickerScore.modify(player.energy)
					energyBlock1.changePos()
				elif attackButton.buttonRect.collidepoint(click):
					if player.energy >= 10:
						player.changeEnergy(-10)
						clickerScore.modify(player.energy)
						enemy.changeHull(-10)
						enemyHullPoints.modify(enemy.hull)
						print("Attacked enemy!")
					else:
						print("Not enough energy!")
				elif shieldButton.buttonRect.collidepoint(click):
					if player.energy >= 10 and shieldButton.cooldown == False:
						shieldButton.changeCooldown(True)
						player.changeEnergy(-10)
						clickerScore.modify(player.energy)
						player.color = cyan
						shieldTime = time
						print("Shields raised!")
					else:
						if shieldButton.cooldown == True:
							print("Shields cooling down!")
						else:
							print("Not enough energy!")

		pygame.display.update()
		gameDisplay.blit(background,(0,0))
		gameDisplay.blit(metalmesh,(0, SCREEN_HEIGHT/1.7))
		gameDisplay.blit(metalmesh,(500, SCREEN_HEIGHT/1.7))
		gameDisplay.blit(metalmesh,(1000, SCREEN_HEIGHT/1.7))
		pygame.draw.line(gameDisplay, light_slate_gray, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT/1.7), 16)
		pygame.draw.line(gameDisplay, light_slate_gray, (0, SCREEN_HEIGHT/1.7), (SCREEN_WIDTH, SCREEN_HEIGHT/1.7), 16)
		pygame.draw.line(gameDisplay, black, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT/1.7), 10)
		pygame.draw.line(gameDisplay, black, (0, SCREEN_HEIGHT/1.7), (SCREEN_WIDTH, SCREEN_HEIGHT/1.7), 10)
		
		# Render all objects in renderableObjects list
		for object in renderableObjects:
			object.render()
		
		handle_keys()
		
		# returns the player's shields to normal after 3 seconds
		if time == shieldTime + 180:
			player.color = black
		if time == shieldTime + 360:
			shieldButton.cooldown = False
			
		time += 1
		if time%60 == 0:
			second += 1
			print(second)
			#time = 0
		clock.tick(60)

# call functions here
main()