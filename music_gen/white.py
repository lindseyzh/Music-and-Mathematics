from music21 import note, duration
from rand import choice


class WhiteNoise:
    def __init__(self, pitch_list, duration_list):
        self.pitch_list = pitch_list
        self.duration_list = duration_list

    def next_pitch(self):
        return choice(self.pitch_list)

    def next_duration(self):
        return choice(self.duration_list)

    def next(self) -> note.Note:
        res = note.Note(self.next_pitch())
        res.duration = duration.Duration(self.next_duration())
        return res
