import random

class BattleShip:
	def __init__(self, x=5, y=5):
		self.X = x
		self.Y = y
		self.ocean = [['^' for i in xrange(x)] for i in xrange(y)]
		self.ship = self.ocean

	def is_inbounds(self, x, y):
		try:
			test = self.ocean[x][y]
			return True
		except IndexError:
			return False

	def add_random_ships(self, number_of_ships=5):
		c = 0
		while c < number_of_ships:
			randX = random.randint(0, self.X-1)
			randY = random.randint(0, self.Y-1)
			if self.ocean[randX][randY] != 'S':
				self.ocean[randX][randY] = 'S'
				c += 1
		

	def add_ship(self, x, y):
   	    if self.is_inbounds(x,y):
		    self.ship[x][y] = 'S'

	def fire(self, x, y):
   		if self.is_inbounds(x,y):
			if self.ship[x][y] == 'S':
				self.ocean[x][y] = 'X'
				return True
			else:
				self.ocean[x][y] == 'O'
				return False

	'''
	Used for testing only...
	'''
	def print_ocean(self):
		for x in self.ocean:
			print x
		
