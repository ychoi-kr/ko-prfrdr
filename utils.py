from functools import reduce

def joinseq(*seq):
    return '|'.join(sorted(set(reduce(lambda x, y: x + y, [x.split('|') for x in seq]))))

