
from random import choice, randint
from sheep import Sheep
from grass import Grass
from world import World
from colors import SHEEP_COLORS


# Parametros da simulacao
SIM_WIDTH = 800
SIM_HEIGHT = 600
FOOD_SIZE = 5  # precisa ser um multiplo comum de SIM_WIDTH e SIM_HEIGHT
N_AGENTS = 1
FOOD_ENERGY = 10
TIME_TO_GROWTH = 400
FLAT_WORLD = True
MUTATION = 1
SPEED = 4
ENERGY = 20
REPRODUCTION_ENERGY = 40

class Simulation:

	def __init__(self,
		width=800, height=600,
		food_size = 5, n_agents = 1, caption = 'Mundo das ovelhas',
		food_energy = 10, time_to_growth = 400, flat = False,
		mutation = 1, speed = 4, energy = 20, reproduction_energy = 40):

		self.width = width
		self.height = height
		self.food_size = food_size
		self.n_agents = n_agents
		self.sheeps = list()
		self.foods = list()
		self.world = World(width, height, caption, flat)
		self.mutation = mutation

		# Instancia os recursos
		for x in range(0, self.world.width, food_size):
			for y in range(0, self.world.height, food_size):
				self.foods.append(Grass(x, y, food_size, food_energy, time_to_growth))

		# Instancia os agentes
		for i in range(N_AGENTS):
			self.sheeps.append(
				Sheep(
					randint(0,self.world.width),
					randint(0,self.world.height),
					#random(width),
					#random(height),
					choice(SHEEP_COLORS),
					speed,
					energy,
					reproduction_energy

				)
			)


	def draw(self):
		#background(0)

		for food in self.foods:
			food.update(self.world)

		for sheep in self.sheeps:
			sheep.update(self.world, self.sheeps, self.foods, self.mutation)

	def run(self):
		while not self.world.done:
			#print('LOOP')
			self.world.event_loop()
			self.world.clear()
			#self.world.ellipse(300,300,100,100, (0,255,0))
			self.draw()
			self.world.tick()
			if len(self.sheeps) > 30000:
				self.world.done = True
		self.world.end()


def main():
	simulation = Simulation(
		SIM_WIDTH, SIM_HEIGHT, FOOD_SIZE, N_AGENTS, 'MUNDO DAS OVELHAS',
		FOOD_ENERGY, TIME_TO_GROWTH, FLAT_WORLD,
		MUTATION, SPEED, ENERGY, REPRODUCTION_ENERGY)
	simulation.run()

if __name__ == "__main__":
	main()
