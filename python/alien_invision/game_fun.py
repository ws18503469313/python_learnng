import sys, pygame

from bullet import Bullet
from alien import Alien
from time import sleep

# do sth when event ocur
def check_event(ship, setting, screen, bullets, start, play, aliens):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_event_keydown(event, ship, setting, screen, bullets)
			elif event.type == pygame.KEYUP:
				check_event_keyup(event, ship)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				check_play_button(setting, ship, start, play, aliens, bullets, mouse_x, mouse_y)
				# print("setting's time :"+ str(setting.ship_limit))
				# print("screen's time :"+ str(ship.setting.ship_limit))

def check_play_button(setting, ship, start, play, aliens, bullets, mouse_x, mouse_y):
	if play.rect.collidepoint(mouse_x, mouse_y) and not start.game_active:
		pygame.mouse.set_visible(False)
		
		aliens.empty()
		bullets.empty()
		create_group_alien(setting, ship.screen, aliens, ship)
		ship.put_center()
		
		# print("game start===================")
		start.game_active = True
		if start.ships_left == play.setting.ship_limit :
			print("game first start")
		else:
			start.game_times += 1
			print("game strat at times of :" + str(start.game_times))
		start.restart()
		setting.init_dynamic_settings()
		
		
	


def check_event_keydown(event, ship, setting, screen, bullets):
	if event.key == pygame.K_RIGHT:
		ship.move_right = True
	elif event.key == pygame.K_LEFT:
		ship.move_left = True	
	elif event.key == pygame.K_SPACE:
		if len(bullets) < setting.bullet_allowed :
			bullet = Bullet(setting, screen, ship)
			bullets.add(bullet)
		
def check_event_keyup(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.move_right = False
	elif event.key == pygame.K_LEFT:
		ship.move_left = False	
		
#repaint the screen			
def update_screen(settings, screen, ship, bullets, aliens, play, start, score_board):
	if not start.game_active :
		play.draw_button()
	else:
		screen.fill(settings.bg_color)
		ship.blitme()
		for bullet in bullets.sprites():
			bullet.draw_bullet()
		aliens.draw(screen)
		score_board.show_score()
	## repaint operation must do when everything else is down
	pygame.display.flip()
			
def update_bullets(bullets, aliens, ship, start, score_board):
	for bullet in bullets.copy():
		if bullet.rect.y < 0:
			bullets.remove(bullet)
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions :
		start.score += start.setting.alien_point
		score_board.prep_score()
	check_max_score(start, score_board)
	if len(aliens) == 0:
		setting = ship.setting
		
		start.level += 1
		score_board.prep_level()
		
		print("=========================game is update===================")
		print("self.ship_speed =" + str(setting.ship_speed))
		print("self.bullet_speed "+ str(setting.bullet_speed))
		print("self.alien_speed" + str(setting))
		setting.update_leve()
		
		print("self.ship_speed =" + str(setting.ship_speed))
		print("self.bullet_speed "+ str(setting.bullet_speed))
		print("self.alien_speed" + str(setting))
		bullets.empty()
		create_group_alien(ship.setting, ship.screen, aliens, ship)
		
	
	

#create a group of alien	
# def create_aliens(setting, screen, aliens):
	# avaliable_space_x = setting.screen_width
	# alien = Alien(setting, screen)
	# alien_width = alien.rect.width
	# alien_num = int(avaliable_space_x / ( alien_width* 2))
	# for i in range(alien_num) :
		# alien = Alien(setting, screen)
		
		# alien.x = alien_width + alien_width * 2 * i
		# alien.rect.x = alien.x
		# aliens.add(alien)
# get the num of a line capacity
def get_alien_nums(setting, alien):
	avaliable_space_x = setting.screen_width
	return int(avaliable_space_x / ( alien.rect.width* 2))
	
def get_alien_lines(setting, alien, ship):
	avaliable_space_y = setting.screen_height - alien.rect.height * 2 - ship.rect.height
	alien_lines = int( avaliable_space_y / ( alien.rect.height * 2))
	return alien_lines
	
def create_alien(setting, screen, aliens, alien_num, alien_line, alien):
	
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	for line in range(alien_line):
		for one in range(alien_num):
			alien = Alien(setting, screen)
			alien.x = alien_width + alien_width * 2 * one
			alien.rect.x = alien.x
			alien.y = alien_height * 2 * line
			alien.rect.y = alien.y
			aliens.add(alien)
	
		
def create_group_alien(setting, screen, aliens, ship):
	alien = Alien(setting, screen)
	alien_num = get_alien_nums(setting, alien)
	alien_line = get_alien_lines(setting, alien, ship)
	create_alien(setting, screen, aliens, alien_num, alien_line, alien)
	
def update_aliens(aliens, setting, ship, bullets, start, score_board):
	check_if2_edge(setting, aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(setting, ship, aliens, bullets, start, score_board)
	check_alian_bottom(setting, ship, aliens, bullets, start, score_board)

def ship_hit(setting, ship, aliens, bullets, start, score_board):
	if start.ships_left > 0:
		
		sleep(1)
		start.ships_left -= 1
		aliens.empty()
		bullets.empty()
		ship.put_center()
		
		create_group_alien(setting, ship.screen, aliens, ship)
	else:
		start.game_active = False
		pygame.mouse.set_visible(True)
	score_board.prep_ship()	
	
	
	
#check is has one aline move to edge
def check_if2_edge(setting, aliens):
	for alien in aliens.sprites():
		if alien.check_edge():
			change_aliens_direction(setting, aliens)
			break

#change_aliens_direction and drop the aliens 
def change_aliens_direction(setting, aliens):
	for alien in aliens.sprites():
		alien.rect.y += setting.alien_drop_speed
	setting.alien_move_direction *= -1

def check_alian_bottom(setting, ship, aliens, bullets, start, score_board):
	screen_rect = ship.screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(setting, ship, aliens, bullets, start, score_board)


def check_max_score(start, score_board):
	if start.score > start.max_score:
		start.max_score = start.score
		score_board.prep_max_score()










