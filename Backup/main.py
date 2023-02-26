from common_imports import *
from grammar import *
from keys_lib import *


################### Escolha do mood e da key ######################

# --- Thayer's model --- #
# Exuberance: calm-energy
# Contentment: calm-tiredness
# Frantic/Anxious: tense-energy
# Depression: tense-tiredness

mood = 'contentment'

if mood == 'contentment':
	mode = 'maior natural'
	mm = tempo.MetronomeMark('adagio')
elif mood == 'depression':
	mode = 'menor natural'
	mm = tempo.MetronomeMark('adagio')
elif mood == 'exuberance':
	mode = 'maior natural'
	mm = tempo.MetronomeMark('allegro')
elif mood == 'frantic':
	mode = 'menor natural'
	mm = tempo.MetronomeMark('allegro')

_key = C(mode)
ts = meter.TimeSignature('4/4')



melody = generateMelody('soprano', _key, ts, 100)
harmony = generateHarmony('alto', _key, ts, 50)


#################### Juntando as duas partes #####################

melody_len = len(melody.getElementsByClass(stream.Measure))
harmony_len = len(harmony.getElementsByClass(stream.Measure))

if melody_len > harmony_len:
	melody = melody.measures(0, harmony_len)
else:
	harmony = harmony.measures(0, melody_len)


merged_parts = stream.Score(id = 'Demo')

merged_parts.insert(0, mm)
merged_parts.insert(0, melody)
merged_parts.insert(0, harmony)

#new_pitch = random.choices(pitchesArray, weights = None, k = 1)[0]

#i = interval.Interval(pitch.Pitch('C'), new_pitch)
#merged_parts.transpose(i, inPlace = True)
merged_parts.show()