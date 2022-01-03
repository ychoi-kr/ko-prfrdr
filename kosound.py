import re

CONSONANTS = "ㄱㄲㄳㄴㄵㄶㄷㄸㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅃㅄㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
FIRST_CONSONANTS = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
VOWELS = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
FINAL_CONSONANTS = "ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"


def splitsound(s):
    ret = ''
    chars = [c for c in s]
    for c in chars:
        if re.match('[가-힣]', c):
            v = ord(c) - 0xAC00
            ret += FIRST_CONSONANTS[v // (28 * 21)]
            ret += VOWELS[v // 28 % 21]
            #ret += FINALC[v % 28]
            ret += ([''] + [c for c in FINAL_CONSONANTS])[v % 28]

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

