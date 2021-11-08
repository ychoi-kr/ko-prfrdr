noundict = {'i':'me', 'we':'us', 'you':'you', 'he':'him', 'she':'her', 'they':'them', 'them':'they', 'her':'she', 'him':'he', 'us':'we', 'me':'i'}

def nouninv(noun):
    n = noun.lower()
    if n in noundict:
        return noundict[n]
    return noun
