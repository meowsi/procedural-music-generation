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
		self.thirtysecond = duration.Duration('32nd')

		if value == 'whole':
			self.durations_array = [self.whole, self.half, self.quarter, self.eighth, self.sixteenth, self.thirtysecond]
		
		elif value == 'half':
			self.durations_array = [self.half, self.whole, self.quarter, self.eighth, self.sixteenth, self.thirtysecond]

		elif value == 'quarter':
			self.durations_array = [self.quarter, self.half, self.eighth, self.whole, self.sixteenth, self.thirtysecond]

		elif value == 'eighth':
			self.durations_array = [self.eighth, self.sixteenth, self.quarter, self.thirtysecond, self.half, self.whole]

		elif value == '16th':
			self.durations_array = [self.sixteenth, self.eighth, self.thirtysecond, self.quarter, self.half, self.whole]

		elif value == '32nd':
			self.durations_array = [self.thirtysecond, self.sixteenth, self.eighth, self.quarter, self.half, self.whole]

		self.weights = [0.45, 0.2, 0.2, 0.07, 0.05, 0.03]


def setDuration(standard, current):
	settings.duration_changes

	#print(current)

	if settings.duration_changes >= 4:
		info = MyDuration(standard)
		settings.duration_changes = 0
	else:
		info = MyDuration(current)

	set_duration = random.choices(info.durations_array, weights = info.weights, k = 1)
	current = set_duration[0]
	if current != standard:
		settings.duration_changes = settings.duration_changes + 1

	return current