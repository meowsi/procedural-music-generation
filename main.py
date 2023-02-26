from common_imports import *
from grammar import *
from keys_lib import *


# --- Thayer's model --- #
# Exuberance: calm-energy
# Contentment: calm-tiredness
# Frantic/Anxious: tense-energy
# Depression: tense-tiredness

mood = 'depression'

if mood == 'contentment':
	mode = 'maior natural'
	mm = tempo.MetronomeMark('adagietto')
elif mood == 'depression':
	mode = 'menor natural'
	mm = tempo.MetronomeMark('adagietto')
elif mood == 'exuberance':
	mode = 'maior natural'
	mm = tempo.MetronomeMark('allegro')
elif mood == 'frantic':
	mode = 'menor natural'
	mm = tempo.MetronomeMark('allegro')

_key = C(mode)
ts = meter.TimeSignature('4/4')

for i in range(0, 5000):
	song = generateSong('demo', _key, ts, mm)
	choose_best_songs(song)

save_best_songs()
# song.show('midi')


#new_pitch = random.choices(pitchesArray, weights = None, k = 1)[0]

# i = interval.Interval(pitch.Pitch('C'), new_pitch)
# song.transpose(i, inPlace = True)
# song.show()