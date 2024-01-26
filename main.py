import pygame

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
		self.x = 150
		self.y = 442.5
		self.image = pygame.image.load("plane.png").convert_alpha()
		self.rect = self.image.get_rect(center = (self.x, self.y))
		# self.image = pygame.transform.scale(self.image, (100, 100)) # make smaller - IT'S JUST POOFING IT >:(



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

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(background)
all_sprites.add(player)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	for b in background:
		b.move()
	
	all_sprites.draw(screen)

	pygame.display.update()

	clock.tick(60)