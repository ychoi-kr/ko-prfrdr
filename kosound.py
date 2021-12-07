import re


FIRSTC = [c for c in "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"]
VOWEL = [c for c in "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"]
FINALC = [''] + [c for c in "ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"]


def splitsound(s):
    ret = ''
    chars = [c for c in s]
    for c in chars:
        if re.match('[가-힣]', c):
            v = ord(c) - 0xAC00
            ret += FIRSTC[v // (28 * 21)]
            ret += VOWEL[v // 28 % 21]
            ret += FINALC[v % 28]
        else:
            ret += c
    return ret


def hasfinalconsonant(c):
    return len(splitsound(c)) == 3


if __name__ == '__main__':
    print(splitsound('쓩'))
    print(splitsound('아버지 가방에 들어가신다.'))
    print(hasfinalconsonant('응'))
    print(hasfinalconsonant('애'))

