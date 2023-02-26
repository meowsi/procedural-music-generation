from common_imports import *
from settings import *
from duration_lib import *


############################ Gramatica 1 ############################

def generateMelody(_id, chosen_key, ts, num_elements):
	part = stream.Part(id = _id)
	part.insert(0, key.KeySignature(chosen_key.ks))
	part.timeSignature = ts
	std_duration = float(ts.numerator) / float(ts.denominator)

	current_note = chosen_key.key_scale[0]

	for i in range(0, num_elements):
		variable_duration = random.choices([True, False], weights = [0.2, 0.8], k = 1)[0]

		if variable_duration == True:
			new_duration = setDuration(duration.Duration(std_duration)).quarterLength
			times = setTimes(new_duration, std_duration)
			current_note = generateElem(current_note, new_duration, times, part)
		
		elif variable_duration == False:
			current_note = generateElem(current_note, std_duration, 1, part)


	handleErrors(part, ts)
	return part


############################ Gramatica 2 ############################

def generateHarmony(_id, chosen_key, ts, num_elements):
	part = stream.Part(id = _id)
	part.insert(0, key.KeySignature(chosen_key.ks))
	part.insert(0, clef.BassClef())
	part.timeSignature = ts
	std_duration = float(ts.numerator) / float(ts.denominator)

	cur_elem = note.Rest()
	cur_elem.duration.quarterLength = 4.0
	part.insert(0, cur_elem)
	

	for i in range(0, num_elements):
		object = random.choices(['Chord', 'Arpeggio', 'Rest'], weights = [0.1, 0.6, 0.3], k = 1)[0]

		if object == 'Chord':
			chord_progression = random.choices(chosen_key.progressions.copy(), weights = None, k = 1)[0]

			for chord in chord_progression:
				chord.duration = setDuration(duration.Duration('quarter'))
				cur_elem = chord
				part.repeatAppend(cur_elem, 1)
			
		elif object == 'Arpeggio':
			chord_progression = random.choices(chosen_key.progressions.copy(), weights = None, k = 1)[0]

			for chord in chord_progression:
				for n in chord.arpeggio:
					n.duration = setDuration(duration.Duration('whole'))
					cur_elem = n
					part.repeatAppend(cur_elem, 1)

		elif object == 'Rest':
			my_rest = note.Rest()
			my_rest.duration = setDuration(duration.Duration('whole'))
			part.repeatAppend(my_rest, 1)
		
	
	handleErrors(part, ts)
	return part