
import os
import sys
import pygame as pg
from colors import BROWN, GREEN

class World:
	def __init__(self,width=800, height=600, CAPTION = 'Mundo das ovelhas', flat = False):
		self.width = width
		self.height = height
		self. flat = flat
		self.fps = 1 #60
		self.done = False
		os.environ['SDL_VIDEO_CENTERED'] = '1'
		pg.init()
		pg.display.set_caption(CAPTION)
		pg.display.set_mode((self.width,self.height))
		self.screen = pg.display.get_surface()
		self.keys = pg.key.get_pressed()
		self.clock = pg.time.Clock()

	def tick(self):
		pg.display.update()
		#self.clock.tick(self.fps)  # tempo de espera por frame se for muito rápido

	def event_loop(self):
		"""
		One event loop. Never cut your game off from the event loop.
		Your OS may decide your program has hung if the event queue is not
		accessed for a prolonged period of time.
		"""
		for event in pg.event.get():
			if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
					self.done = True
			elif event.type in (pg.KEYUP, pg.KEYDOWN):
				self.keys = pg.key.get_pressed()

	def clear(self):
 		""" limpa a tela com cor de terra (planta comida)
 		"""
 		self.screen.fill(BROWN)

	def ellipse(self, x, y, xsize, ysize, color):
		pg.draw.ellipse(self.screen, color, (x,y,xsize,ysize))

	def rect(self, x, y, xsize, ysize, color):
		pg.draw.rect(self.screen, color, (x,y,xsize,ysize))

	def end(self):
		pg.quit()
		sys.exit()
