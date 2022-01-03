import re
from functools import reduce

import kosound


def offset(c):
    return kosound.CONSONANTS.index(c) + 1

def join(seq):
    def join_two(a, b):
        if re.match('[가-히]', a[-1]) and not kosound.hasfinalconsonant(a[-1]) and b in kosound.CONSONANTS:
            return ''.join([a[:-1], chr(ord(a[-1]) + offset(b))])
        else:
            return ''.join([a, b])

    return reduce(join_two, seq)

