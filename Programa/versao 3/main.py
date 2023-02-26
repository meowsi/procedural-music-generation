from os import *
import random
import settings
import keys_lib
import duration_lib
from numpy.random import choice
import copy
from music21 import *

'''
--> Ideia fundamentada em MARKOV CHAIN e GRAMATICA
--> Os estados seguintes dependem do estado atual
--> Existem várias tabelas de probabilidade, a tabela a ser usada é decidida com base no estado atual
(Ver exemplo do JFlap)

--> Escolhe-se o mood x de acordo com a fase do jogo
--> A gramática da linguagem MELODIA PRINCIPAL se inicia

S (simbolo inicial da gramatica)
S -> HVRM
H: deriva todas as harmonias do mood x, escolhidas de forma aleatoria
EXEMPLO: se x é um sad, H deriva as harmonias do campo MENOR
H -> Am | Bm | Cm | Dm | A#m | B#m | C#m | ...

V: velocidade inicial, tambem de acordo com o mood
EXEMPLO: moods sombrios sao devagares e moods alegres sao rapidos
V -> 80bpm | 100bpm | 120bpm | ...

R: ritmo (ex: 4/4)

M: MELODIA PRINCIPAL. Objetos em geral, gerados aleatoriamente
M -> AO
A: altura
A -> crescente | descrescente | mudar a oitava
        45%          45%             10%

O: objetos em geral
O -> M | N | P | T | lambda (100% depois de n compassos percorridos, ou se o nivel acabar, etc) 
    20% 50% 25%  5%    0%
N -> seminima | minima | colcheia | semicolcheia | ...
P -> mesma logica, mas para as pausas
Quanto mais proximo do ritmo, maior a probabilidade
Se o ritmo é 4/4, a chance de seminima é grande

T: acrescenta o tema do mood/jogo, transposto para a harmonia selecionada
T -> transposto acima | transposto abaixo | original | ...


--> Depois de H, V e R serem decididos, uma gramatica auxiliar começa a rodar ao mesmo tempo que a outra
--> Ela acrescenta acordes, notas, ornamentos, etc. à melodia principal

G (simbolo inicial)
G -> GN | GV | GO | lambda
    90%   3%   7%     0%

N -> nota | pausa | A
      60%    10%   30%

O -> ornamentos diversos | mudar a oitava
A -> arpejo | acorde


--> A cada par de variaveis de melodia principal/gramatica auxiliar gerado, toca-se o offset atual da partitura

'''



######################## Escolha do mood e da key #########################

mood = 'happy'

if mood == 'happy':
	mode = 'maior natural'
elif mood == 'sad':
	mode = 'menor natural'

'''
array_tom = [keys_lib.C_key(mode), keys_lib.D_key(mode)]
tom = random.choices(array_tom, weights = None, k = 1)
tom = tom[0]
'''

tom = keys_lib.C_key(mode)


########################## Parte 1: soprano #########################

p1 = stream.Part(id = 'soprano')
p1.timeSignature = meter.TimeSignature('4/4')

cur_note = tom._1 # nota inicial = primeira nota da escala (padrão em composição)
elem = tom._1

for i in range(0, 100):
	#cur_note.addLyric(cur_note.pitch.spanish, lyricNumber = 0) #lyricNumber 0 p/ subs lyric anterior
		
	elem.duration = duration_lib.setDuration(duration.Duration('quarter'), cur_note.duration)
	cur_note.duration = elem.duration
	p1.repeatAppend(elem, 1)

	next_note = random.choices(cur_note.scale.copy(), weights = cur_note.weights, k = 1)
	next_note[0].duration = copy.deepcopy(cur_note.duration)
	cur_note = copy.deepcopy(next_note[0])

	op = [cur_note, note.Rest()]
	elem = random.choices(op, weights = [0.9, 0.1], k = 1)
	elem = elem[0]
	


p1.insert(0, key.KeySignature(tom.ks))
p1.makeMeasures(inPlace = True)




######################### Parte 2: contralto ############################

p2 = stream.Part(id = 'contralto')
p2.timeSignature = meter.TimeSignature('4/4')

nota2 = tom._1
cur_elem = note.Rest()
cur_elem.duration.quarterLength = 4.0

p2.repeatAppend(cur_elem, 2)
cur_elem.duration.quarterLength = 1.0

for i in range(0, 20):
	# nota2.addLyric(nota2.pitch.nameWithOctave, lyricNumber = 0) #lyricNumber 0 p/ subs lyric anterior

	options = ['Chord', 'Arpeggio', 'Rest']
	choice = random.choices(options, weights = [0.1, 0.6, 0.3], k = 1)
	choice = choice[0]

	if choice == 'Chord':
		result = random.choices(tom.progressions.copy(), weights = None, k = 1)
		result = result[0]
		size = len(result)
		for i in range(0, size):
			chord = result[i]
			if i == size-1:
				chord.duration.type = 'whole'
			chord.duration = duration_lib.setDuration(duration.Duration('quarter'), cur_elem.duration)
			cur_elem = chord
			p2.repeatAppend(cur_elem, 1)

	elif choice == 'Arpeggio':
		result = random.choices(tom.progressions.copy(), weights = None, k = 1)
		result = result[0]
		size1 = len(result)
		for i in range(0, size1):
			chord = result[i]

			size2 = len(chord.arpeggio)
			for i in range(0, size2):
				n = chord.arpeggio[i]
				if i == size2-1:
					n.duration.type = 'whole'
				p2.repeatAppend(n, 1)

	else:
		my_rest = note.Rest()
		my_rest.duration = duration_lib.setDuration(duration.Duration('whole'), duration.Duration('whole'))
		p2.repeatAppend(my_rest, 1) #deepcopy de elem
	

p2.insert(0, key.KeySignature(tom.ks))
p2.makeMeasures(inPlace = True)



#################### Juntando as duas partes #####################

p1_len = len(p1.getElementsByClass(stream.Measure))
p2_len = len(p2.getElementsByClass(stream.Measure))

if p1_len > p2_len:
	p1 = p1.measures(0, p2_len)
else:
	p2 = p2.measures(0, p1_len)

aux = stream.Measure()
#p1.measure().makeRests(fillGaps = True)

merged_parts = stream.Score(id = 'Demo')
merged_parts.insert(0, p1)
merged_parts.insert(0, p2)

merged_parts.show()

#k = stream1.analyze('key')
#i = interval.Interval(k.tonic, pitch.Pitch('D#'))
#m2 = stream1.transpose(i)
#m2.show()
