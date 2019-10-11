
from colors import WHITE, YELLOW
from random import randrange, random, uniform, randint
from math import ceil
import copy

class Sheep:

	def __init__(self, x, y, sheep_color = WHITE, speed = 4, energy = 20, reproduction_energy = 40):
		self.x = x
		self.y = y
		self.size = 8
		self.speed = speed
		self.energy = energy
		self.color = sheep_color
		self.reproduction_energy = reproduction_energy
		self.energy_comsumption = {
			'move': 1,
			'reproduction': self.reproduction_energy*.6
		}

	def mutation(self):
		""" gera uma mutação aleatória na velocidade e energia necessária para reprodução
		"""
		self.color = (randint(1, 255), randint(1, 255), randint(1, 255))
		self.speed += randint(-1,1)
		self.reproduction_energy = int(self.reproduction_energy * uniform(0.5, 2))
		self.reproduction_energy = 3 if self.reproduction_energy < 3 else self.reproduction_energy

		self.energy_comsumption = {
			'move': 1,
			'reproduction': self.reproduction_energy*.6}

		print("Mutação >> Vel: {} Rep: {}".format(self.speed, self.reproduction_energy))

	def move(self, world):
		""" Faz a ovelha se movimentar
		de acordo com sua velocidade em
		uma direcao aleatoria.

		Se a ovelha ultrapassar os limites
		da tela, ela sera renderizada do
		lado oposto ao qual ela ultrapassou
		os limites.
		Porém se o mundo for plano, ela não cruzará as barreriras.
		"""
		dx = 0 if self.speed == 0 else randint(-self.speed, self.speed)
		dy = 0 if self.speed == 0 else randint(-self.speed, self.speed)
		self.x += dx
		self.y += dy
		self.fix_position(world)
		# quanto + rápido e mais "gordo" (energia), mais energia consome
		if not(dx == 0 and dy == 0):
			denergy = int(round(self.energy_comsumption['move'] * (abs(dx) + abs(dy)) * self.energy/100))
			#print("denergy : ",denergy)  # para debug
			if denergy > 0:
				self.energy = self.energy - denergy
			else:
				self.energy = self.energy - 1

		world.ellipse(self.x, self.y, self.size, self.size, self.color)

	def fix_position(self, world):
		""" Mantem a ovelha dentro
		do campo de visao, a operacao
		de modulo na posicao da ovelha
		faz ela se manter dentro das posicoes
		posiveis do janela.
		"""
		if world.flat: # mundo terraplanista : não cruza bordas
			if self.x >= world.width:
				self.x = world.width - 1
			elif self.x < 0:
				self.x  = 0

			if self.y >= world.height:
				self.y = world.height - 1
			elif self.y < 0:
				self.y = 0
		else: # mundo circular : ai passar de um lado vai para o lado oposto
			if self.x >= world.width:
				self.x %= world.width
			elif self.x < 0:
				self.x  += world.width

			if self.y >= world.height:
				self.y %= world.height
			elif self.y < 0:
				self.y += world.height

	def die(self, sheeps):
		""" Se a energia da ovelha
		chegar a zero ela morre. Ou seja,
		sai da lista de ovelhas vivas.
		"""
		if self.energy <= 0:
			sheeps.remove(self)

	def reproduce(self, sheeps, mutation):
		""" A ovelha se reproduz se
		chegar no limiar de energia necessario
		para reproducao.
		"""
		if self.energy >= self.reproduction_energy:
			self.energy -= self.energy_comsumption['reproduction']
			self.energy = self.energy / 2
			newsheep = copy.deepcopy(self)
			# E se adicionarmos uma mutacao?
			if randint(0, 100) < mutation:
				newsheep.mutation()
			sheeps.append(newsheep)

	def try_eat(self, world, foods):
		""" A ovelha tenta se alimentar, se a posicao em
		que ela estiver for a posicao de uma comida disponivel,
		ela come.
		"""
		food_rows = int(world.height/foods[0].size)
		x_scale = int(self.x/foods[0].size)
		y_scale = int(self.y/foods[0].size)
		food = foods[x_scale * food_rows + y_scale]
		if not food.eaten:
			self.energy += food.energy
			food.eated()

	def update(self, world, sheeps, foods,mutation):
		self.move(world)
		self.try_eat(world,foods)
		self.reproduce(sheeps,mutation)
		self.die(sheeps)
