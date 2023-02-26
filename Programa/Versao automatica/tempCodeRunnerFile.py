new_pitch = random.choices(pitchesArray(), weights = None, k = 1)[0]

i = interval.Interval(pitch.Pitch('C'), new_pitch)
merged_parts.transpose(i, inPlace = True)