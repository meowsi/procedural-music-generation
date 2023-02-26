from os import *
import random
import settings
import keys_lib
import duration_lib
from numpy.random import choice
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
EXEMPLO: se x é um mood triste, H deriva as harmonias do campo MENOR
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

# Escolher o tom
humor = 'triste'

if humor == 'feliz':
	modo = 'maior natural'
elif humor == 'triste':
	modo = 'menor natural'

array_tom = [keys_lib.Do(modo), keys_lib.Re(modo)]
tom = random.choices(array_tom, weights = None, k = 1)
tom = tom[0]

# Definir a nota inicial como a primeira nota da escala (padrão em composição)
nota = tom.escala[0]

# Criar a partitura
stream1 = stream.Stream()
p1 = stream.Part()
p2 = stream.Part()
	

######## Parte 1: soprano ########

for i in range(0, 200):
	#nota.addLyric(nota.pitch.spanish, lyricNumber = 0) #lyricNumber 0 p/ subs lyric anterior

	opcoes = [nota, note.Rest()]
	elem = random.choices(opcoes, weights = [0.8, 0.2], k = 1)
	elem = elem[0]

	p1.repeatAppend(elem, 1) #deepcopy de nota
	
	nota_aleatoria = random.choices(tom.escala, weights = nota.array_pesos, k = 1)
	nota = nota_aleatoria[0]

stream1.append(p1)


######## Parte 2: contralto ########

escala_contralto = [note.Note(), note.Note(), note.Note(), note.Note(), note.Note(), note.Note(), note.Note()]

for i in range (0, 7):
	tom.escala[i].transpose("-P8", inPlace = True)

nota2 = tom.escala[0]

for i in range(0, 200):
	# nota2.addLyric(nota2.pitch.nameWithOctave, lyricNumber = 0) #lyricNumber 0 p/ subs lyric anterior

	nota_ou_pausa = [nota2, note.Rest()]
	elem = random.choices(nota_ou_pausa, weights = [0.6, 0.4], k = 1)
	elem = elem[0]

	#elem.duration = duration_lib.setDuration('quarter', elem.duration.type)
	p2.repeatAppend(elem, 1) #deepcopy de nota
	
	nota_aleatoria = random.choices(tom.escala, weights = nota.array_pesos, k = 1)
	nota2 = nota_aleatoria[0]


stream1.append(p2)


stream1.show()

k = stream1.analyze('key')
i = interval.Interval(k.tonic, pitch.Pitch('D#'))
m2 = stream1.transpose(i)
#m2.show()