# tt = list()

# with open('ko_speech_level.txt') as f:
    # for line in f.readlines()[1:]:
        # hasipsio, haeyo, haera, hae = tuple(map(lambda x: x + '.', line.split(',')))
        # for x in [hasipsio, haeyo, hae]:
            # if x != '.' and haera != '.':
                # tt.append((x, haera))

# stc = input()

# for src, dst in tt:
    # stc = stc.replace(src, dst)

# print()
# print(stc)

import convert_speech_level

sentence = input()
print()
print(convert_speech_level.haera(sentence))