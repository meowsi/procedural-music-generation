from common_imports import *

# Variaveis globais
duration_changes = 0
std_note_weights = [0.08, 0.12, 0.25, 0.10, 0.25, 0.12, 0.08]
dif_note_weights = [[0.1, 0.4, 0.25, 0.1, 0.07, 0.05, 0.03], [0.15, 0.1, 0.35, 0.2, 0.1, 0.07, 0.03], [0.07, 0.15, 0.1, 0.35, 0.2, 0.08, 0.05]]


def setKeyScale(self):
	self.key_scale = [self._1, self._2, self._3, self._4, self._5, self._6, self._7, self._8, self._9, self._10, self._11, self._12, self._13, self._14]

def setNoteScales(self):
	arr = self.key_scale
	first_partition = [arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6]]
	last_partition  = [arr[7], arr[8], arr[9], arr[10], arr[11], arr[12], arr[13]]
	
	for i in range(0, 3):
		arr[i].scale = first_partition.copy()
		arr[i].weights = dif_note_weights[i].copy()

	for i in range(3, 11):
		arr[i].scale = []
		arr[i].weights = std_note_weights.copy()
		index = i - 3
		for j in range(0, 7):
			arr[i].scale.append(arr[index])
			index = index + 1
	
	index = 0
	for i in range(11, 14):
		arr[i].scale = last_partition.copy()
		arr[i].weights = dif_note_weights[::-1][index][::-1]
		index = index + 1


def setChords(self):
	_1 = self._1.transpose('-P8')
	_2 = self._2.transpose('-P8')
	_3 = self._3.transpose('-P8')
	_4 = self._4.transpose('-P8')
	_5 = self._5.transpose('-P8')
	_6 = self._6.transpose('-P8')
	_7 = self._7.transpose('-P8')
	_8 = self._8.transpose('-P8')
	_9 = self._9.transpose('-P8')
	_10 = self._10.transpose('-P8')
	_11 = self._11.transpose('-P8')
	_12 = self._12.transpose('-P8')
	_13 = self._13.transpose('-P8')
	_14 = self._14.transpose('-P8')

	self.I = chord.Chord([_1, _3, _5])
	self.I7 = chord.Chord([_1, _3, _5, _7])
	self.ii = chord.Chord([_2, _4, _6])
	self.ii7 = chord.Chord([_2, _4, _6, _8])
	self.iii = chord.Chord([_3, _5, _7])
	self.IV = chord.Chord([_4, _6, _8])
	self.V = chord.Chord([_5, _7, _9])
	self.V7 = chord.Chord([_5, _7, _9, _11])
	self.vi = chord.Chord([_6, _8, _10])
	self.vii = chord.Chord([_7, _9, _11])

	self.I.arpeggio = [_1, _3, _5]
	self.I7.arpeggio = [_1, _3, _5, _7]
	self.ii.arpeggio = [_2, _4, _6]
	self.ii7.arpeggio = [_2, _4, _6, _8]
	self.iii.arpeggio = [_3, _5, _7]
	self.IV.arpeggio = [_4, _6, _8]
	self.V.arpeggio = [_5, _7, _9]
	self.V7.arpeggio = [_5, _7, _9, _11]
	self.vi.arpeggio = [_6, _8, _10]
	self.vii.arpeggio = [_7, _9, _11]

	p1 = [self.I, self.IV, self.V]
	p2 = [self.I, self.vi, self.IV, self.V]
	p3 = [self.ii7, self.V7, self.I7]

	self.progressions = [p1, p2, p3]

def setTimes(new_duration, std_duration):
	if new_duration > std_duration*2:
		times = random.choices([1, 2], weights = [0.9, 0.1], k = 1)[0]
	elif new_duration > std_duration:
		times = random.choices([1, 2], weights = [0.5, 0.5], k = 1)[0]
	elif new_duration < std_duration:
		times = random.choices([1, 2, 3, 4], weights = None, k = 1)[0]

	return times


def generateElem(cur_note, duration, times, part):
	for i in range(0, times):
		elem = random.choices([note.Note(), note.Rest()], weights = [0.8, 0.2], k = 1)[0]
		
		if isinstance(elem, note.NotRest):
			cur_note = random.choices(cur_note.scale.copy(), weights = cur_note.weights, k = 1)[0]
			cur_note.duration.quarterLength = duration
			part.repeatAppend(cur_note, 1)
		else:
			cur_rest = note.Rest()
			cur_rest.duration.quarterLength = duration
			cur_note.duration.quarterLength = duration
			part.repeatAppend(cur_rest, 1)

	return cur_note



def handleErrors(part, ts):
	part.makeMeasures(ts, inPlace = True)
	len_part = len(part.getElementsByClass(stream.Measure))

	measure_duration = (float(ts.numerator) / float(ts.denominator)) / 0.25

	try:
		last_elem = part.measure(-1).getElementsByClass(['Note', 'Rest', 'Chord'])[-1]
	except:
		part = part.measures(0, len_part-1)
		last_elem = part.measure(-1).getElementsByClass(['Note', 'Rest', 'Chord'])[-1]
	
	highest_time = part.measure(-1).highestTime
	difference = measure_duration - highest_time

	last_elem.duration.quarterLength = last_elem.duration.quarterLength + difference

	return part



# this function makes harmony and melody have the same size
def joinMelodyAndHarmony(melody, harmony, ts):

	measure_duration = (float(ts.numerator) / float(ts.denominator)) / 0.25
	
	harmony_highest_time = harmony.measure(-1).highestTime
	melody_highest_time = melody.measure(-1).highestTime
	difference = melody_highest_time - harmony_highest_time

	len_melody = len(melody.getElementsByClass(stream.Measure))
	len_harmony = len(harmony.getElementsByClass(stream.Measure))

	
	# here we're fetching the last note/chord/rest of both parts
	melody_last_elem = melody.measure(-1).getElementsByClass(['Note', 'Rest'])[-1]
	harmony_last_elem = harmony.measure(-1).getElementsByClass(['Note', 'Rest', 'Chord'])[-1]

	
	# in this case, we'll cut the melody in order to be the same size as the harmony
	if len_melody > len_harmony:
		
		melody = melody.measures(0, len_harmony)
		melody = handleErrors(melody, ts)


	# we can't cut the harmony so as to preserve the progressions, so we'll extend the melody instead
	elif len_melody < len_harmony:
		
		amount_of_measures_to_add = len_harmony - len_melody
		melody.repeatAppend(stream.Measure(), amount_of_measures_to_add)
		melody_last_elem.duration.quarterLength = melody_last_elem.duration.quarterLength + amount_of_measures_to_add*measure_duration + difference

	return melody



pitchesArray = [pitch.Pitch("A"), pitch.Pitch("B"), pitch.Pitch("C"), pitch.Pitch("D"), pitch.Pitch("E"),
				pitch.Pitch("F"), pitch.Pitch("G"), pitch.Pitch("A#"), pitch.Pitch("B#"), pitch.Pitch("C#"),
				pitch.Pitch("D#"), pitch.Pitch("E#"), pitch.Pitch("F#"), pitch.Pitch("G#")]