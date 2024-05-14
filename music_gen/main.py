import datetime
import sys

from music21 import *
from brown import BrownNoise
from config import *
from pink import PinkNoise
from white import WhiteNoise


# https://labs.la.utexas.edu/gilden/files/2016/04/Gardner-WhiteBrownFractalMusic.pdf
# for the details of the fractal music generation algorithm.


def generate(color) -> stream.Stream:
    stream1 = stream.Stream()
    stream1.append(meter.TimeSignature('4/4'))

    total_measures = 0
    measure_duration = 0.0
    while total_measures < Total_Measures:
        while measure_duration < Measure_Duration:
            n = color.next()
            measure_duration += n.duration.quarterLength
            if measure_duration > Measure_Duration:
                # If the note exceeds the measure, we split it into two notes
                split = n.splitAtDurations()
                for n in split:
                    stream1.append(n)
            else:
                stream1.append(n)
        total_measures += 1
        measure_duration -= Measure_Duration

    return stream1


def get_pitch_list(first_group: int, last_group: int):
    pitch_list = []
    for i in range(first_group, last_group + 1):
        pitch_list.append('C' + str(i))
        pitch_list.append('C' + str(i) + '#')
        pitch_list.append('D' + str(i))
        pitch_list.append('D' + str(i) + '#')
        pitch_list.append('E' + str(i))
        pitch_list.append('F' + str(i))
        pitch_list.append('F' + str(i) + '#')
        pitch_list.append('G' + str(i))
        pitch_list.append('G' + str(i) + '#')
        pitch_list.append('A' + str(i))
        pitch_list.append('A' + str(i) + '#')
        pitch_list.append('B' + str(i))
    return pitch_list


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python main.py [white|brown|pink]')
        sys.exit(1)

    white = WhiteNoise(get_pitch_list(4, 5), [0.25, 0.5, 1.0, 2.0, 4.0])
    brown = BrownNoise('C4', 0.5)
    pink = PinkNoise(get_pitch_list(1, 7), [0.25, 0.5, 0.5, 1.0, 1.0, 2.0, 2.0, 4.0], 10, 3)

    if sys.argv[1] == 'white':
        white_stream = generate(white)
        white_stream.insert(0, metadata.Metadata())
        white_stream.metadata.title = 'White Noise' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        white_stream.show()
    elif sys.argv[1] == 'brown':
        brown_stream = generate(brown)
        brown_stream.insert(0, metadata.Metadata())
        brown_stream.metadata.title = 'Brown Noise' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        brown_stream.show()
    elif sys.argv[1] == 'pink':
        pink_stream = generate(pink)
        pink_stream.insert(0, metadata.Metadata())
        pink_stream.metadata.title = 'Pink Noise' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        pink_stream.show()
    else:
        print('Usage: python main.py [white|brown|pink]')
        sys.exit(1)
