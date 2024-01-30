import pygame
import random

pygame.init()

screen_width = 1600
screen_height = 885
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Simple Pygame Game - Aviator Accend")

clock = pygame.time.Clock()

# three classes
# at least 1 includes animation when an obj moves
# enable control of obj thru key presses for at least 1 class
class Background(pygame.sprite.Sprite):
	def __init__(self, x, y, flipx):
		super().__init__()
		self.x = x
		self.y = y
		self.speed = 2
		self.image = pygame.image.load("sky.jpeg")
		self.rect = self.image.get_rect(center = (self.x, self.y))
		self.image = pygame.transform.flip(self.image, flipx, False)
	def move(self):
		if self.rect.centerx < -960:
			self.x = 4800
			self.rect.center = (self.x,self.y)
		self.x -= self.speed
		self.rect.center = (self.x,self.y)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.x = 160
		self.y = 442.5
		self.speed = 10
		# self.image = pygame.image.load("plane.png").convert_alpha()
		self.image = pygame.transform.scale(pygame.image.load("plane.png").convert_alpha(), (100, 100))
		self.image = pygame.transform.flip(self.image, True, False)
		self.rect = self.image.get_rect(center = (self.x, self.y))
	def accend(self):
		# self.image = pygame.transform.rotate(self.image, 1)
		self.rect.y -= self.speed
	def descend(self):
		# self.image = pygame.transform.rotate(self.image, -1)
		self.rect.y += self.speed
	def collide(self):
		if pygame.sprite.collide_rect(self, bomb):
			# self.image = pygame.image.load("boom.jpg").convert_alpha()
			self.image = pygame.transform.scale(pygame.image.load("boom.jpg").convert_alpha(), (100, 100))
			self.kill()

class Bomb(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.x = 1590
		self.y = random.randint(100, 870)
		self.speed = 4
		# self.image = pygame.image.load("bomb.jpg").convert_alpha()
		self.image = pygame.transform.scale(pygame.image.load("bomb.jpg").convert_alpha(), (50, 50))
		self.rect = self.image.get_rect(center = (self.x, self.y))
	def move(self):
		self.x -= self.speed
		self.rect.center = (self.x,self.y)
	def relocate(self):
		self.x = 1590
		self.y = random.randint(100, 870)
		self.rect.center = (self.x, self.y)

class Parachute(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.x = 1590
		self.y = random.randint(100, 870)
		self.speed = 4
		# self.image = pygame.image.load("parachute.png").convert_alpha()
		self.image = pygame.transform.scale(pygame.image.load("parachute.png").convert_alpha(), (50, 50))
		self.rect = self.image.get_rect(center = (self.x, self.y))
	def move(self):
		self.x -= self.speed
		self.rect.center = (self.x,self.y)
	def relocate(self):
		self.x = 1590
		self.y = random.randint(100, 870)
		self.rect.center = (self.x, self.y)



# collision detction
# utilize .colliderect() method in at least 1 class to determine if an obj has made contact w/ another obj

# sprite grp
# use at least 1 Group from the pygame.sprite to organize & manage sprites

# pygame.sprite.spritecollide() func to detect if an obj makes contact w/ any other objs stored in the grp

# game loop

# winning/losing conditions
# define clear goal to achieve victory
# mechanics for which the player can lose
		
background = pygame.sprite.Group()
background.add(Background(960, 442.5, False))
background.add(Background(2880, 442.5, True))
background.add(Background(4800, 442.5, False))

bomb = Bomb()

people = pygame.sprite.Group()
for i in range(5):
	people.add(Parachute())

player = Player()

npcs = pygame.sprite.Group()
npcs.add(bomb)
npcs.add(people)

all_sprites = pygame.sprite.Group()
all_sprites.add(background)
all_sprites.add(bomb)
all_sprites.add(people)
all_sprites.add(player)

while player.alive():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	
	pygame.sprite.spritecollide(player, people, True)

	for b in background:
		b.move()
	
	for x in npcs:
		x.move()
		if x.x < 0:
			x.relocate()

	player.collide()
	
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		player.accend()
	if keys[pygame.K_DOWN]:
		player.descend()
	
	all_sprites.draw(screen)

	pygame.display.update()

	clock.tick(60)

print("YOU DIED")