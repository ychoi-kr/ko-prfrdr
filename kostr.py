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


def concat(*seq):
    def concat_two(a, b):
        if re.match('[ㄱ-ㅎ]', a[-1]) and re.match('[ㅏ-ㅣ]', b):
            #return chr(ord('가') + (ord(b) - ord('ㅏ')) * (len(kosound.FINAL_CONSONANTS) + 1))
            return ''.join([
                    a[:-1],
                    chr(
                        ord('가')
                        + (kosound.FIRST_CONSONANTS.find(a[-1]) * len(kosound.VOWELS) * (len(kosound.FINAL_CONSONANTS)+1))
                        + ((len(kosound.FINAL_CONSONANTS) + 1) * (ord(b) - ord('ㅏ')))
                    )
                    ])
        elif re.match('[가-히]', a[-1]) and not kosound.hasfinalconsonant(a[-1]) and b in kosound.CONSONANTS:
            return ''.join([a[:-1], chr(ord(a[-1]) + kosound.FINAL_CONSONANTS.find(b) + 1)])
        else:
            return ''.join([a, b])

    return reduce(concat_two, seq)


if __name__ == '__main__':
    print("concat('ㄱ', 'ㅏ')", concat('ㄱ', 'ㅏ'))
    print("concat('가', 'ㄴ')", concat('가', 'ㄴ'))
    print("concat('가바', 'ㄴ')", concat('가바', 'ㄴ'))
    print("concat('ㄱ', 'ㅏ', 'ㄱ')", concat('ㄱ', 'ㅏ', 'ㄱ'))
    print("concat('ㄱ', 'ㅏ', 'ㄴ')", concat('ㄱ', 'ㅏ', 'ㄴ'))
    print("concat('ㄱ', 'ㅏ', 'ㄷ')", concat('ㄱ', 'ㅏ', 'ㄷ'))
    print("concat('ㄱ', 'ㅏ', 'ㄹ')", concat('ㄱ', 'ㅏ', 'ㄹ'))
    print("concat('나ㅃ', 'ㅡ', '다')", concat('나ㅃ', 'ㅡ', '다'))
