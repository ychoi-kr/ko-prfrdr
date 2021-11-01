
def convert(sentence, level):
    tt = list()

    with open('ko_speech_level.txt') as f:
        for line in f.readlines()[1:]:
            col = line.rstrip().split(',')  # hasipsio, haeyo, haera, hae
            if level == 'hasipsio':
                src_idx_list = [1, 2, 3]
                dst_idx = 0
            elif level == 'haeyo':
                src_idx_list = [0, 2, 3]
                dst_idx = 1
            elif level == 'haera':
                src_idx_list = [0, 1, 3]
                dst_idx = 2
            elif level == 'hae':
                src_idx_list = [0, 1, 2]
                dst_idx = 3
            
            for src_idx in src_idx_list:
                if col[src_idx] != '' and col[dst_idx] != '':
                    tt.append((col[src_idx], col[dst_idx]))
   
    for src, dst in tt:
        sentence = sentence.replace(src + '.', dst + '.')

    return sentence

def hasipsio(sentence):
    return convert(sentence, 'hasipsio')

def haeyo(sentence):
    return convert(sentence, 'haeyo')

def haera(sentence):
    return convert(sentence, 'haera')

def hae(sentence):
    return convert(sentence, 'hae')


if __name__ == '__main__':
    main()