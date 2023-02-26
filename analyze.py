from common_imports import *
import uuid

song_list = []

class Song:
    def __init__(self, score, index):
        self.score = score
        self.index = index

def analyze(melody, harmony):
    melody_notes = []
    harmony_notes = []
    index = 0

    for n in melody.flat.getElementsByClass('Note'):
        if n.name not in melody_notes:
            melody_notes.append(n.name)
    
    for elem in harmony.flat.getElementsByClass(['Note', 'Chord']):
        if isinstance(elem, chord.Chord):
            # print('elem is chord\n')
            for n in elem:
                if n.name not in harmony_notes:
                    harmony_notes.append(n.name)
        
        elif isinstance(elem, note.Note):
            if elem.name not in harmony_notes:
                harmony_notes.append(elem.name)
    
    # print('melodia:', end = ' ')
    for unique_note in melody_notes:
        # print(unique_note, end = ' ')
        if unique_note not in harmony_notes:
            index = index + 1

    # print('\nharmonia:', end = ' ')
    for unique_note in harmony_notes:
        # print(unique_note, end = ' ')
        if unique_note not in melody_notes:
            index = index + 1

    # print('\n')
    return index


def findIndex(e):
    return e.index


def choose_best_songs(new):
    global song_list

    if len(song_list) < 10:
        song_list.append(new)
        song_list.sort(key=findIndex)
        for i in song_list:
            print(i.index, end=' ')
        print('\n')
    else:
        old = song_list[-1]

        if old.index > new.index:
            song_list.pop()
            song_list.append(new)
        song_list.sort(key=findIndex)
        for i in song_list:
            print(i.index, end=' ')
        print('\n')

    
def save_best_songs():
    global song_list
    for item in song_list:
        filename = str(uuid.uuid4())
        item.score.write("midi", filename + ".mid")