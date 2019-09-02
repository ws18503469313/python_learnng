
class GameStart():
	
	def __init__(self, setting):
		self.setting = setting
		self.restart()
		self.game_active = False
		self.game_times =1
		
		self.score = 0
		self.level = 1
		self.max_score = 0
		
	def restart(self):
		self.ships_left = self.setting.ship_limit
		self.score = 0
		self.level = 1
