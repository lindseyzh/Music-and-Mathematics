import datetime
from music21 import *
from music_gen.brown import BrownNoise
from music_gen.config import *
from music_gen.pink import PinkNoise
from music_gen.white import WhiteNoise


# Here we leverage this assumption:
# As the slides provide no method to randomly generate the duration of a note,
# we exploit the same generate method with pitch.


def generate(color) -> stream.Stream:
    stream1 = stream.Stream()
    stream1.append(meter.TimeSignature('4/4'))

    total_measures = 0
    while total_measures < Total_Measures:
        measure_duration = 0.0
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

    return stream1


if __name__ == '__main__':
    white = WhiteNoise(['C4', 'C4#', 'D4', 'D4#', 'E4', 'F4', 'F4#', 'G4', 'G4#', 'A4', 'A4#', 'B4',
                        'C5', 'C5#', 'D5', 'D5#', 'E5', 'F5', 'F5#', 'G5', 'G5#', 'A5', 'A5#', 'B5'],
                       [0.25, 0.5, 1.0, 2.0, 4.0])
    brown = BrownNoise('C5', 0.5)
    pink = PinkNoise(['C4', 'C4#', 'D4', 'D4#', 'E4', 'F4', 'F4#', 'G4', 'G4#', 'A4', 'A4#', 'B4',
                      'C5', 'C5#', 'D5', 'D5#', 'E5', 'F5', 'F5#', 'G5', 'G5#', 'A5', 'A5#', 'B5'],
                     [0.25, 0.5, 0.5, 1.0, 1.0, 2.0, 4.0], 6)

    # white_stream = generate(white)
    # white_stream.insert(0, metadata.Metadata())
    # white_stream.metadata.title = 'White Noise' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # white_stream.show()

    # brown_stream = generate(brown)
    # brown_stream.insert(0, metadata.Metadata())
    # brown_stream.metadata.title = 'Brown Noise' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # brown_stream.show()

    pink_stream = generate(pink)
    pink_stream.insert(0, metadata.Metadata())
    pink_stream.metadata.title = 'Pink Noise' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pink_stream.show()
