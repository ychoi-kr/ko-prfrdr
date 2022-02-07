def joinseq(*seq):
    return '|'.join([x.strip('|') for x in seq])
