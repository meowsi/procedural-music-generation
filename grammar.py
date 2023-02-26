from common_imports import *
from settings import *
from duration_lib import *
from analyze import *

os.chdir('C:\\Users\\Meow\\Documents\\Codes\\USP\\IC Musica')


def generateSong(_id, _key, ts, mm):
	melody_part = stream.Part(id = 'melodia')
	melody_part.insert(0, instrument.Piano())
	melody_part.insert(0, key.KeySignature(_key.ks))
	melody_part.timeSignature = ts
	
	harmony_part = stream.Part(id = 'harmonia')
	harmony_part.insert(0, instrument.Piano())
	harmony_part.insert(0, key.KeySignature(_key.ks))
	harmony_part.insert(0, clef.BassClef())
	harmony_part.timeSignature = ts

	score = stream.Score(id = _id)
	std_duration = float(ts.numerator) / float(ts.denominator)
	index = 0

	# s = converter.parseFile('Tema.musicxml')
	
	# measure_qty = len(s.parts[0].getElementsByClass(stream.Measure))
	
	# for m in s.parts[0].getElementsByClass(stream.Measure):
	# 	part.repeatAppend(m, 1)
	

	# current_note = _key.key_scale[0]
	# part.repeatAppend(current_note, 1)

	# intro
	# for i in range(0, 5):
	# 	variable_duration = random.choices([True, False], weights = [0.2, 0.8], k = 1)[0]

	# 	if variable_duration == True:
	# 		new_duration = setDuration(duration.Duration(std_duration)).quarterLength
	# 		times = setTimes(new_duration, std_duration)
	# 		current_note = generateElem(current_note, new_duration, times, part)
		
	# 	elif variable_duration == False:
	# 		current_note = generateElem(current_note, std_duration, 1, part)

	A_melody = generatePhrase('A', ts, _key)
	A_harmony = generateHarmony('alto', _key, ts)
	A_melody = joinMelodyAndHarmony(A_melody, A_harmony, ts)
	A_index = analyze(A_melody, A_harmony)
	# print('A_index:', A_index)


	B_melody = generatePhrase('B', ts, _key)
	B_harmony = generateHarmony('alto', _key, ts)
	B_melody = joinMelodyAndHarmony(B_melody, B_harmony, ts)
	B_index = analyze(B_melody, B_harmony)
	# print('B_index:', B_index)


	C_melody = generatePhrase('C', ts, _key)
	C_harmony = generateHarmony('alto', _key, ts)
	C_melody = joinMelodyAndHarmony(C_melody, C_harmony, ts)
	C_index = analyze(C_melody, C_harmony)
	# print('C_index:', C_index)

	D_melody = generatePhrase('C', ts, _key)
	D_harmony = generateHarmony('alto', _key, ts)
	D_melody = joinMelodyAndHarmony(D_melody, D_harmony, ts)
	D_index = analyze(D_melody, D_harmony)
	# print('D_index:', D_index)


	intro_part = stream.Part(id = 'melodia')
	intro_part.insert(0, key.KeySignature(_key.ks))
	intro_part.timeSignature = ts

	intro_len = len(A_melody.getElementsByClass(stream.Measure))
	r = note.Rest()
	r.duration.quarterLength = 4
	print("A", end = '')
	for n in A_melody.flat.getElementsByClass(['Note', 'Rest', 'Chord', expressions.TextExpression]):
		melody_part.repeatAppend(n, 1)
	for m in range(0, intro_len):
		harmony_part.repeatAppend(r, 1)

	for n in A_melody.flat.getElementsByClass(['Note', 'Rest', 'Chord', expressions.TextExpression]):
		melody_part.repeatAppend(n, 1)
	for h in A_harmony.flat.getElementsByClass(['Note', 'Rest', 'Chord', expressions.TextExpression]):
		harmony_part.repeatAppend(h, 1)


	for i in range(0, 10):
		add_phrase = random.choices(['A', 'B', 'C', 'D'], weights = [0.25, 0.25, 0.25, 0.25], k = 1)[0]
		
		if (add_phrase == 'A'):
			print("A", end = '')
			for n in A_melody.flat.getElementsByClass(['Note', 'Rest', 'Chord', expressions.TextExpression]):
				melody_part.repeatAppend(n, 1)
			for h in A_harmony.flat.getElementsByClass(['Note', 'Rest', 'Chord', expressions.TextExpression]):
				harmony_part.repeatAppend(h, 1)

			index = index + A_index
		
		elif (add_phrase == 'B'):
			print("B", end = '')
			for n in B_melody.flat.getElementsByClass(['Note', 'Rest', 'Chord', expressions.TextExpression]):
				melody_part.repeatAppend(n, 1)
			for h in B_harmony.flat.getElementsByClass(['Note', 'Rest', 'Chord', expressions.TextExpression]):
				harmony_part.repeatAppend(h, 1)

			index = index + B_index
		
		elif (add_phrase == 'C'):
			print("C", end = '')
			for n in C_melody.flat.getElementsByClass(['Note', 'Rest', 'Chord', expressions.TextExpression]):
				melody_part.repeatAppend(n, 1)
			for h in C_harmony.flat.getElementsByClass(['Note', 'Rest', 'Chord', expressions.TextExpression]):
				harmony_part.repeatAppend(h, 1)

			index = index + C_index

		elif (add_phrase == 'D'):
			print("D", end = '')
			for n in D_melody.flat.getElementsByClass(['Note', 'Rest', 'Chord', expressions.TextExpression]):
				melody_part.repeatAppend(n, 1)
			for h in D_harmony.flat.getElementsByClass(['Note', 'Rest', 'Chord', expressions.TextExpression]):
				harmony_part.repeatAppend(h, 1)

			index = index + D_index
		
		
		# add_theme = random.choices([True, False], weights = [0.2, 0.8], k = 1)[0]
		# if add_theme == True:
		# 	print('*')
		# 	for elem in s.flat.notes:
		# 		part.repeatAppend(elem, 1)

	score.insert(0, melody_part)
	score.insert(0, harmony_part)
	score.insert(0, mm)

	print('\nindex:', index)
	song = Song(score, index)
	
	return song



def generatePhrase(_id, ts, _key):
	phrase = stream.Stream(id = _id)
	std_duration = float(ts.numerator) / float(ts.denominator)
	current_note = _key.key_scale[0]

	te = expressions.TextExpression("Frase " + _id)
	phrase.insert(0, te)

	for i in range(0, 15):
		variable_duration = random.choices([True, False], weights = [0.2, 0.8], k = 1)[0]

		if variable_duration == True:
			new_duration = setDuration(duration.Duration(std_duration)).quarterLength
			times = setTimes(new_duration, std_duration)
			current_note = generateElem(current_note, new_duration, times, phrase)
		
		elif variable_duration == False:
			current_note = generateElem(current_note, std_duration, 1, phrase)

	phrase = handleErrors(phrase, ts)
	return phrase


def generateHarmony(_id, _key, ts):
	harmony = stream.Stream(id = _id)
	
	std_duration = float(ts.numerator) / float(ts.denominator)

	chord_progression = random.choices(_key.progressions.copy(), weights = None, k = 1)[0]

	for chord in chord_progression:
		harmonize = random.choices([True, False], weights = [0.1, 0.9], k = 1)[0]
		if harmonize == True:
			random_duration = random.choices(['True', 'False'], weights = [0.7, 0.3], k = 1)[0]
			if random_duration == 'True':
				chord.duration = duration.Duration('whole')
			else:
				chord.duration = duration.Duration(std_duration)
			cur_elem = chord
			harmony.repeatAppend(cur_elem, 1)
		
		else:
			for n in chord.arpeggio:
				n.duration = duration.Duration(std_duration)
				if n == chord.arpeggio[-1]:
					random_duration = random.choices(['True', 'False'], weights = [0.7, 0.3], k = 1)[0]
					if random_duration == 'True':
						n.duration = duration.Duration('whole')
				
				cur_elem = n
				harmony.repeatAppend(cur_elem, 1)
		
		rest = random.choices([True, False], weights = [0.3, 0.7], k = 1)[0]
		if rest == True:
			my_rest = note.Rest()
			rest_duration = setDuration(duration.Duration(std_duration)).quarterLength
			my_rest.duration = setDuration(duration.Duration(rest_duration))
			harmony.repeatAppend(my_rest, 1)
	
	harmony = handleErrors(harmony, ts)
	return harmony