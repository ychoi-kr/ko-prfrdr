import re
from functools import reduce

from kosound import hasfinalconsonant

consonant = "ㄱㄲㄳㄴㄵㄶㄷㄸㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅃㅄㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"

def offset(c):
    return consonant.index(c) + 1

def join(seq):
    def join_two(a, b):
        if re.match('[가-히]', a[-1]) and not hasfinalconsonant(a[-1]) and b in consonant:
            return ''.join([a[:-1], chr(ord(a[-1]) + offset(b))])
        else:
            return ''.join([a, b])

    return reduce(join_two, seq)

