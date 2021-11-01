# tt = list()

# with open('ko_speech_level.txt') as f:
    # for line in f.readlines()[1:]:
        # hasipsio, haeyo, haera, hae = tuple(map(lambda x: x + '.', line.rstrip().split(',')))
        # for x in [hasipsio, haera, haeyo]:
            # if x != '.' and hae != '.':
                # tt.append((x, hae))

# stc = input()

# for src, dst in tt:
    # stc = stc.replace(src, dst)

# print()
# print(stc)
import convert_speech_level

sentence = input()
print()
print(convert_speech_level.hae(sentence))