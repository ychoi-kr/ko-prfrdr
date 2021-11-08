#!/usr/bin/env python

# https://github.com/DanManN/pass2act

import sys
import spacy
#import pattern.en

from pass2act.pass2act import pass2act



#nlp = spacy.load('en')
nlp = spacy.load("en_core_web_sm")
prev = ''
acts = ''
while True:
    s=input('\n').strip()
    if s == 'q':
        break
    elif s == '':
        continue
    elif s =='t':
        spacy.displacy.serve([nlp(prev), nlp(acts)], style='dep')
    else:
        prev = s
        acts = pass2act(s)
        print(acts)