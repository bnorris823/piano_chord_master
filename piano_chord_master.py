
import argparse
import time
import random
import subprocess

def get_arguments():

    parser = argparse.ArgumentParser(description="python piano chord practice")
    parser.add_argument("--keys", nargs="+", help="list of chords to include", required=False)
    parser.add_argument("--types", nargs="+", help="major or minor", required=False)
    parser.add_argument("--positions", nargs="+", help="hand position", required=False)
    parser.add_argument("--interval", help="time in between chords", required=False, type=int)

    return parser.parse_args()

def get_notes(chord, chord_type, pos):

    notes_dict = {'C': ['C,E,G', 'G,C,E', 'E,G,C'],
                   'C#': ['C#,F,Ab', 'Ab,C#,F', 'F,Ab,C#'],
                   'Db': ['Db,F,Ab', 'Ab,Db,F', 'F,Ab,Db'],
                   'D': ['D,F#,A', 'A,D,F#', 'F#,A,D'],
                   'D#': ['D#,G,Bb', 'Bb,D#,G', 'G,Bb,D#'],
                   'Eb': ['Eb,G,Bb', 'Bb,Eb,G', 'G,Bb,Eb'],
                   'E': ['E,Ab,B', 'B,E,Ab', 'Ab,B,E'],
                   'F': ['F,A,C', 'C,F,A', 'A,C,F'],
                   'F#': ['F#,Bb,C#', 'C,F,A', 'A,C,F'],
                   'Gb': ['Gb,Bb,C#', 'C#,Gb,Bb', 'Bb,C#,Gb'],
                   'G': ['G,B,D', 'D,G,B', 'B,D,G'],
                   'G#': ['G#,C,Eb', 'Eb,G#,C', 'C,Eb,G#'],
                   'Ab': ['Ab,C,Eb', 'Eb,Ab,C', 'Eb,C,Ab'],
                   'A': ['A,C#,E', 'E,A,C#', 'C#,E,A'],
                   'A#': ['A#,D,F', 'F,A#,D', 'D,F,A#'],
                   'Bb': ['Bb,D,F', 'F,Bb,D', 'D,F,Bb'],
                   'B': ['B,Eb,F#', 'F#,B,Eb', 'F#,Eb,B'],
                   'Cm': ['C,Eb,G', 'G,C,Eb', 'Eb,G,C'],
                   'C#m': ['C#,E,Ab', 'Ab,C#,E', 'E,Ab,C#'],
                   'Dbm': ['Db,E,Ab', 'Ab,Db,E', 'E,Ab,Db'],
                   'Dm': ['D,F,A', 'A,D,F', 'F,A,D'],
                   'D#m': ['D#,F#,Bb', 'Bb,D#,F#', 'F#,Bb,D#'],
                   'Ebm': ['Eb,F#,Bb', 'Bb,Eb,F#', 'F#,Bb,Eb'],
                   'Em': ['E,G,B', 'B,E,G', 'G,B,E'],
                   'Fm': ['F,Ab,C', 'C,F,Ab', 'Ab,C,F'],
                   'F#m': ['F#,A,C#', 'C,F,Ab', 'Ab,C,F'],
                   'Gbm': ['Gb,A,C#', 'C#,Gb,A', 'A,C#,Gb'],
                   'Gm': ['G,Bb,D', 'D,G,Bb', 'Bb,D,G'],
                   'G#m': ['G#,B,Eb', 'Eb,G#,B', 'B,Eb,G#'],
                   'Abm': ['Ab,B,Eb', 'Eb,Ab,B', 'D,C,Ab'],
                   'Am': ['A,C,E', 'E,A,C', 'C,E,A'],
                   'A#m': ['A#,C#,F', 'F,A#,C#', 'C#,F,A#'],
                   'Bbm': ['Bb,C#,F', 'F,Bb,C#', 'C#,F,Bb'],
                   'Bm': ['B,D,F#', 'F#,B,D', 'F#,D,B'],
                   }
    if pos == '':
        pos_num = 0
    elif pos == 'mid':
        pos_num = 1
    else:
        pos_num = 2

    try:
        notes = notes_dict[f"{chord}{chord_type}"][pos_num]
        return notes
    except Exception:
        return ''


def get_random_chord(chords: list, types: list, positions: list, used_chords:list):
    combined_chord = 'X'

    found = False
    while not found:
        chord = random.choice(chords)
        chord_type = random.choice(types)
        pos = random.choice(positions)

        notes = get_notes(chord, chord_type, pos)

        combined_chord = f"{chord}{chord_type} {pos}        {notes}"
        if combined_chord not in used_chords:
            found = True

    return combined_chord

def main(keys: list, types: list, positions: list, interval:int):

    black_keys = ['Ab', 'Bb', 'Db', 'Eb', 'Gb', 'A#', 'C#', 'D#', 'F#', 'G#']
    white_keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    default_types = ['', 'm', 'M7', '7', 'm7']
    default_positions = ['', 'mid', 'bwk']
    default_time = 15

    print(keys)

    final_chords = []
    if keys == ['white']:
        final_chords = white_keys
    elif keys == ['black']:
        final_chords = black_keys
    else:
        final_chords = white_keys + black_keys

    final_types = [chord_type for chord_type in default_types if chord_type in types]
    final_positions = [pos for pos in default_positions if pos in positions]
    if interval is not None:
        final_time = interval
    else:
        final_time = default_time

    print(f"chords: {final_chords}")
    print(f"types: {final_types}")
    print(f"positions: {final_positions}")
    print(f"time: {final_time}")
    print('*******************')

    used_chords = []

    stop = None

    while stop is None:
        chord = get_random_chord(final_chords, final_types, final_positions, used_chords)
        used_chords.append(chord)
        print(chord)
        print()
        user_input = subprocess.call(f'read -t {final_time}', shell=True)
        if user_input is 0:
            stop = 'stop'





if __name__ == "__main__":
    args = get_arguments()
    if args.types is None:
        args.types = []

    if args.positions is None:
        args.positions = []

    if args.keys is None:
        args.keys = []


    main(args.keys, args.types, args.positions, args.interval)
