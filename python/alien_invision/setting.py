class Setting():
	
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		##ship move speed
		self.ship_speed = 1.2
		
		self.bullet_speed = 1.5
		self.bullet_width = 3
		self.bullet_height = 8
		self.bullet_color = 60, 60, 60
		self.bullet_allowed = 10
		
		
		self.alien_speed = 1
		self.alien_drop_speed = 88
		#left: -1, right: 1
		self.alien_move_direction = 1
		
		self.ship_limit = 3
		
		
		self.speed_scale = 1.1
		
		self.init_dynamic_settings()
		
		self.alien_point = 5
	
	def init_dynamic_settings(self):
		
		self.ship_speed_factor = 1.1
		
		self.bullet_speed_factor = 3
		
		self.alien_speed_factor = 1.1
		
		self.alien_point_factor = 5
		
	def update_leve(self):
		self.ship_speed *= self.ship_speed_factor
		self.bullet_speed *= self.bullet_speed_factor
		self.alien_speed *= self.alien_speed_factor
		self.alien_point += self.alien_point_factor
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
