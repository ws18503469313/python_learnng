import pygame

from pygame.sprite import Sprite
class Ship(Sprite):
	#init a ship to the screen
	def __init__(self, screen, setting):
		super().__init__()
		self.screen = screen
		self.image = pygame.image.load("images/alien.jpg")
		# rect == Rectangle (chang fang xing)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.setting = setting
		# init the position of this ship
		self.rect.centerx = self.screen_rect.centerx
		self.center = float(self.rect.centerx)
		self.rect.bottom = self.screen_rect.bottom
		
		self.move_right = False
		self.move_left = False
		
		
		
		
	# repaint
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	# update the x, y of this ship
	def update(self):
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.center += self.setting.ship_speed
		if self.move_left and self.rect.left > 0:
			self.center -= self.setting.ship_speed
		
		self.rect.centerx = self.center
	
	def put_center(self):
		self.center = self.screen_rect.centerx
	
	
	
	
	
	
	
	
	
	
	
	
	
	
