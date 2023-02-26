from common_imports import *
import settings


class MyDuration:
	def __init__(self, value):
		self.quarter = duration.Duration('quarter')
		self.half = duration.Duration('half')
		self.whole = duration.Duration('whole')
		self.eighth = duration.Duration('eighth')
		self.sixteenth = duration.Duration('16th')

		if value == 'whole':
			self.durations_array = [self.half, self.quarter, self.eighth, self.sixteenth]
		
		elif value == 'half':
			self.durations_array = [self.whole, self.quarter, self.eighth, self.sixteenth]

		elif value == 'quarter':
			self.durations_array = [self.half, self.eighth, self.whole, self.sixteenth]

		elif value == 'eighth':
			self.durations_array = [self.sixteenth, self.quarter, self.half, self.whole]

		elif value == '16th':
			self.durations_array = [self.eighth, self.quarter, self.half, self.whole]

		self.weights = [0.35, 0.35, 0.20, 0.10]


def setDuration(standard):
	info = MyDuration(standard.type)
	set_duration = random.choices(info.durations_array.copy(), weights = info.weights, k = 1)[0]
	current = set_duration

	return current