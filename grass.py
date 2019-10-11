from colors import GREEN, BROWN
from random import randint

class Grass:
	
	def __init__(self, x, y, grass_size, energy = 10, time_to_growth = 400):
		self.x = x
		self.y = y
		self.size = grass_size
		self.energy = energy
		self.eaten = False
		self.color = GREEN
		self.time = 0
		self.time_to_growth = time_to_growth

	def eated(self):
		self.eaten = True
		self.color = BROWN
	
	def growth(self):
		if randint(0,100) < 3 and self.time >= self.time_to_growth:
			self.time = 0
			self.eaten = False
			self.color = GREEN
	
	def update(self, world):
		if not self.eaten:
			world.rect(self.x, self.y, self.size, self.size, self.color)
		if self.eaten: # só conta o tempo de crescimento se a planta tiver sido comida
			self.time += 1
		self.growth()
