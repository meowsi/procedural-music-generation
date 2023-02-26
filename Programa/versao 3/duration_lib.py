from music21 import *
import random
import settings
from numpy.random import choice

class MyDuration:
	def __init__(self, value):
		self.quarter = duration.Duration('quarter')
		self.half = duration.Duration('half')
		self.whole = duration.Duration('whole')
		self.eighth = duration.Duration('eighth')
		self.sixteenth = duration.Duration('16th')

		if value == 'whole':
			self.durations_array = [self.whole, self.half, self.quarter, self.eighth, self.sixteenth]
		
		elif value == 'half':
			self.durations_array = [self.half, self.whole, self.quarter, self.eighth, self.sixteenth]

		elif value == 'quarter':
			self.durations_array = [self.quarter, self.half, self.eighth, self.whole, self.sixteenth]

		elif value == 'eighth':
			self.durations_array = [self.eighth, self.sixteenth, self.quarter, self.half, self.whole]

		elif value == '16th':
			self.durations_array = [self.sixteenth, self.eighth, self.quarter, self.half, self.whole]

		self.weights = [0.65, 0.125, 0.125, 0.07, 0.03]


def setDuration(standard, current):
	
	if current.type != standard.type:
		if settings.duration_changes >= 3:
			aux = standard.type
			settings.duration_changes = 0
		else:
			aux = current.type
			settings.duration_changes = settings.duration_changes + 1

	else:
		aux = standard.type
		settings.duration_changes = 0
	
	info = MyDuration(aux)
	set_duration = random.choices(info.durations_array.copy(), weights = info.weights, k = 1)
	current = set_duration[0]

	return current

