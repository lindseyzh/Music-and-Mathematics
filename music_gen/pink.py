from music21 import note, duration
from rand import choice


class PinkNoise:
    def __init__(self, pitch_list, duration_list, pitch_bits, duration_bits):
        self.pitch_list = pitch_list
        self.duration_list = duration_list
        self.pitch_bits = pitch_bits
        self.duration_bits = duration_bits
        self.pitch_index = -1
        self.duration_index = -1

        self.pitch_dices = []
        for i in range(self.pitch_bits):
            self.pitch_dices.append(0)

        self.duration_dices = []
        for i in range(self.duration_bits):
            self.duration_dices.append(0)

        # print(self.bits_number)
        # print(self.pitch_part)
        # print(self.duration_part)

    def next_pitch(self):
        cur_index = self.pitch_index
        prev_index = cur_index - 1
        pitch_part = (len(self.pitch_list) - 1) // self.pitch_bits + 1

        for i in range(self.pitch_bits):
            if prev_index & (1 << i) != cur_index & (1 << i):
                self.pitch_dices[i] = choice([j for j in range(pitch_part)])

        return self.pitch_list[sum(self.pitch_dices)]

    def next_duration(self):
        cur_index = self.duration_index
        prev_index = cur_index - 1
        duration_part = (len(self.duration_list) - 1) // self.duration_bits + 1

        for i in range(self.duration_bits):
            if prev_index & (1 << i) != cur_index & (1 << i):
                self.duration_dices[i] = choice([j for j in range(duration_part)])

        return self.duration_list[sum(self.duration_dices)]

    def next(self) -> note.Note:
        self.pitch_index += 1
        if self.pitch_index == 2 ** self.pitch_bits:
            self.pitch_index = 0
        self.duration_index += 1
        if self.duration_index == 2 ** self.duration_bits:
            self.duration_index = 0
        res = note.Note(self.next_pitch())
        res.duration = duration.Duration(self.next_duration())
        return res
