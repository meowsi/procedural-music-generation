from common_imports import *
from settings import *
from duration_lib import *

os.chdir('C:\\Users\\Meow\\Documents\\Codes\\USP\\IC Musica')

############################ Gramatica 1 ############################

def generatePhrase(_id, ts, chosen_key):
	phrase = stream.Stream(id = _id)
	std_duration = float(ts.numerator) / float(ts.denominator)
	current_note = chosen_key.key_scale[0]
	# measure_qty = random.randint(3, 5)

	te = expressions.TextExpression("Frase " + _id)
	phrase.insert(0, te)

	for i in range(0, 10):
		variable_duration = random.choices([True, False], weights = [0.2, 0.8], k = 1)[0]

		if variable_duration == True:
			new_duration = setDuration(duration.Duration(std_duration)).quarterLength
			times = setTimes(new_duration, std_duration)
			current_note = generateElem(current_note, new_duration, times, phrase)
		
		elif variable_duration == False:
			current_note = generateElem(current_note, std_duration, 1, phrase)

	return phrase

def generateMelody(_id, chosen_key, ts, num_elements):
	part = stream.Part(id = _id)
	part.insert(0, key.KeySignature(chosen_key.ks))
	part.timeSignature = ts
	std_duration = float(ts.numerator) / float(ts.denominator)

	s = converter.parseFile('Tema.musicxml')
	
	measure_qty = len(s.parts[0].getElementsByClass(stream.Measure))
	
	# for m in s.parts[0].getElementsByClass(stream.Measure):
	# 	part.repeatAppend(m, 1)
	

	current_note = chosen_key.key_scale[0]
	part.repeatAppend(current_note, 1)

	# intro
	for i in range(0, 5):
		variable_duration = random.choices([True, False], weights = [0.2, 0.8], k = 1)[0]

		if variable_duration == True:
			new_duration = setDuration(duration.Duration(std_duration)).quarterLength
			times = setTimes(new_duration, std_duration)
			current_note = generateElem(current_note, new_duration, times, part)
		
		elif variable_duration == False:
			current_note = generateElem(current_note, std_duration, 1, part)

	A = generatePhrase('A', ts, chosen_key)
	B = generatePhrase('B', ts, chosen_key)
	C = generatePhrase('C', ts, chosen_key)

	for i in range(5, 10):
		add_phrase = random.choices(['A', 'B', 'C'], weights = None, k = 1)[0]
		if (add_phrase == 'A'):
			part.repeatAppend(A, 1)
		elif (add_phrase == 'B'):
			part.repeatAppend(B, 1)
		elif (add_phrase == 'C'):
			part.repeatAppend(C, 1)
		
		# add_theme = random.choices([True, False], weights = [0.2, 0.8], k = 1)[0]
		# if add_theme == True:
		# 	print('*')
		# 	for elem in s.flat.notes:
		# 		part.repeatAppend(elem, 1)


	handleErrors(part, ts)
	return part


############################ Gramatica 2 ############################

def generateHarmony(_id, chosen_key, ts, num_elements):
	part = stream.Part(id = _id)
	# part.insert(0, instrument.Violoncello())
	part.insert(0, key.KeySignature(chosen_key.ks))
	part.insert(0, clef.BassClef())
	part.timeSignature = ts
	std_duration = float(ts.numerator) / float(ts.denominator)

	cur_elem = note.Rest()
	cur_elem.duration.quarterLength = 4.0
	part.repeatAppend(cur_elem, 1)

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
				harmonize = random.choices([True, False], weights = [0.1, 0.9], k = 1)[0]
				if harmonize == True:
					chord.duration = duration.Duration(std_duration)
					cur_elem = chord
					part.repeatAppend(cur_elem, 1)
				
				else:
					for n in chord.arpeggio:
						n.duration = duration.Duration(std_duration)
						cur_elem = n
						part.repeatAppend(cur_elem, 1)
				
				my_rest = note.Rest()
				my_rest.duration = setDuration(duration.Duration('whole'))
				part.repeatAppend(my_rest, 1)


		elif object == 'Rest':
			my_rest = note.Rest()
			my_rest.duration = setDuration(duration.Duration('whole'))
			part.repeatAppend(my_rest, 1)
	

	
	handleErrors(part, ts)
	return part