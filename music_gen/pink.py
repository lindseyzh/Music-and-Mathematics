from music21 import note, duration
from rand import choice


class PinkNoise:
    def __init__(self, pitch_list, duration_list, bits_number):
        self.pitch_list = pitch_list
        self.duration_list = duration_list
        self.bits_number = bits_number
        self.index = -1

        self.pitch_part = (len(pitch_list) - 1) // self.bits_number + 1
        self.pitch_dices = []
        for i in range(self.bits_number):
            self.pitch_dices.append(0)
        self.duration_part = (len(duration_list) - 1) // self.bits_number + 1
        self.duration_dices = []
        for i in range(self.bits_number):
            self.duration_dices.append(0)

        # print(self.bits_number)
        # print(self.pitch_part)
        # print(self.duration_part)

    def next_pitch(self):
        cur_index = self.index
        prev_index = cur_index - 1

        for i in range(self.bits_number):
            if prev_index & (1 << i) != cur_index & (1 << i):
                self.pitch_dices[i] = choice([j for j in range(self.pitch_part)])

        # print(self.pitch_dices)
        return self.pitch_list[sum(self.pitch_dices)]

    def next_duration(self):
        # cur_index = self.index
        # prev_index = cur_index - 1
        #
        # for i in range(self.bits_number):
        #     if prev_index & (1 << i) != cur_index & (1 << i):
        #         self.duration_dices[i] = choice([j for j in range(self.duration_part)])
        #
        # return self.duration_list[sum(self.duration_dices)]
        return 0.5

    def next(self) -> note.Note:
        self.index += 1
        if self.index == 2 ** self.bits_number:
            self.index = 0
        res = note.Note(self.next_pitch())
        res.duration = duration.Duration(self.next_duration())
        return res
