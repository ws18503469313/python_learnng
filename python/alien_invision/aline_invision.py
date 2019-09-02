import sys, pygame

from setting import Setting
from ship import Ship
from alien import Alien
from game_start import GameStart
from button import Button
from scoreboard import Scoreboard
import game_fun as gf

from pygame.sprite import Group


def run_game():
	pygame.init()
	# load the init setting
	setting = Setting()
	# load the screen
	screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
	# set the title for the game window
	pygame.display.set_caption("alien invision")
	# init a ship
	ship = Ship(screen, setting)
	# init a bullet group
	bullets = Group()
	aliens = Group()
	gf.create_group_alien(setting, screen, aliens, ship)
	
	start = GameStart(setting)
	
	play = Button(setting, screen, "START")
	
	score_board = Scoreboard(setting, screen, start)
	while True:
		gf.check_event(ship, setting, screen, bullets, start, play, aliens)
		# print(" state is :"+ str(start.game_active))
		if start.game_active:
			ship.update()
			bullets.update()
			# remove the disappered bullet
			gf.update_bullets(bullets, aliens, ship, start, score_board)
			gf.update_aliens(aliens,setting, ship, bullets, start, score_board)
			# repaint
		gf.update_screen(setting, screen, ship, bullets, aliens, play, start, score_board)
		
		
		
run_game()


