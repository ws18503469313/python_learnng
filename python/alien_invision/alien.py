
import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	 
	def __init__(self, setting, screen):
		super().__init__()
		self.screen = screen
		self.setting = setting

		self.image = pygame.image.load("images/alien.png")
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		self.x += (self.setting.alien_speed * self.setting.alien_move_direction)
		self.rect.x = self.x
	
	def check_edge(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
