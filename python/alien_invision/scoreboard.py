
import pygame.font
from pygame.sprite import Group

from ship import Ship
class Scoreboard():
	
	def __init__(self, setting, screen, start):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.setting = setting 
		self.start = start
	
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		
		self.prep_score()
		
		self.prep_max_score()
		
		self.prep_level()
		
		self.prep_ship()
		
	def prep_score(self):
		score_str = str(self.start.score)
		self.score_image = self.font.render(score_str, True,
											self.text_color,
											self.setting.bg_color)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
	
	def prep_max_score(self):
		max_score_str = str(self.start.max_score)
		self.max_score_image = self.font.render(max_score_str, True,
												self.text_color,
												self.setting.bg_color)
		self.max_score_rect = self.max_score_image.get_rect()
		self.max_score_rect.centerx = self.screen_rect.centerx
		self.max_score_rect.top = self.score_rect.top
		
	
	def prep_level(self):
		
		self.level_image = self.font.render(str(self.start.level), True,
											self.text_color,
											self.setting.bg_color)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right - 20
		self.level_rect.top = self.score_rect.top + 35
	
	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.max_score_image, self.max_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)

	def prep_ship(self):
		ships = Group()
		for i in range(self.start.ships_left):
			one = Ship(self.screen, self.setting)
			one.rect.x = 10 + i * one.rect.width
			one.rect.y = 10
			ships.add(one)
		self.ships = ships















