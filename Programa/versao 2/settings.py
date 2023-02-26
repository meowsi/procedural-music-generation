# Variaveis globais
duration_changes = 0
std_note_weights = [0.08, 0.12, 0.25, 0.10, 0.25, 0.12, 0.08]
dif_note_weights = [[0.1, 0.4, 0.25, 0.1, 0.07, 0.05, 0.03], [0.15, 0.1, 0.35, 0.2, 0.1, 0.07, 0.03], [0.07, 0.15, 0.1, 0.35, 0.2, 0.08, 0.05]]


def setScales(_1, _2, _3, _4, _5, _6, _7, _1up, _2up, _3up, _4up, _5up, _6up, _7up):
	
	arr_notes = [_1, _2, _3, _4, _5, _6, _7, _1up, _2up, _3up, _4up, _5up, _6up, _7up]

	first_partition = [_1,   _2,   _3,   _4,   _5,   _6,   _7  ]
	last_partition  = [_1up, _2up, _3up, _4up, _5up, _6up, _7up]
	
	for i in range(0, 3):
		arr_notes[i].scale = first_partition.copy()
		arr_notes[i].weights = dif_note_weights[i].copy()

	for i in range(3, 11):
		arr_notes[i].scale = []
		arr_notes[i].weights = std_note_weights.copy()
		index = i - 3
		for j in range(0, 7):
			arr_notes[i].scale.append(arr_notes[index])
			index = index + 1
	
	index = 0
	for i in range(11, 14):
		arr_notes[i].scale = last_partition.copy()
		arr_notes[i].weights = dif_note_weights[::-1][index][::-1]
		index = index + 1