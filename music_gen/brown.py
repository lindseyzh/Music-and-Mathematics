from music21 import note, duration
from rand import rand, choice

pitches_list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
pitch_bias_dict = {
    -3: 0.1,
    -2: 0.2,
    -1: 0.2,
    0: 0.2,
    1: 0.2,
    2: 0.2,
    3: 0.1,
}


class BrownNoise:
    def __init__(self, cur_pitch: str, cur_duration: float):
        self.cur_pitch = cur_pitch
        self.cur_duration = cur_duration

    def next_pitch(self):
        cur_pitch = self.cur_pitch
        if len(cur_pitch) == 2:
            index = pitches_list.index(cur_pitch[0])
            group = int(cur_pitch[1])
        else:
            index = pitches_list.index(cur_pitch[0] + cur_pitch[2])
            group = int(cur_pitch[1])

        index += rand(pitch_bias_dict, 0.1)
        if index < 0:
            index += 12
            group -= 1
        elif index > 11:
            index -= 12
            group += 1

        # We check the range of the pitch, but we don't prevent
        # the pitch from going out of the range.
        assert (1 <= group <= 7) or \
               (group == 8 and index <= 0) or \
               (group == 0 and index >= 9)

        next_pitch = pitches_list[index]
        if len(next_pitch) == 1:
            next_pitch += str(group)
        else:
            next_pitch = next_pitch[0] + str(group) + next_pitch[1]

        self.cur_pitch = next_pitch
        return next_pitch

    def next_duration(self) -> float:
        # cur_duration = self.cur_duration
        # if cur_duration == 0.25:
        #     next_duration = cur_duration * 2 ** choice([0, 1])
        # elif cur_duration == 4.0:
        #     next_duration = cur_duration * 2 ** rand({-1: 0.8, 0: 0.2}, 0.1)
        # else:
        #     next_duration = cur_duration * 2 ** choice([-1, 0, 1])
        # self.cur_duration = next_duration
        # return next_duration
        return 0.5

    def next(self) -> note.Note:
        res = note.Note(self.next_pitch())
        res.duration = duration.Duration(self.next_duration())
        return res
