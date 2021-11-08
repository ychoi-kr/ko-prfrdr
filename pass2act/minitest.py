#!/usr/bin/env python
import sys
import spacy
import pattern.en as en
import re
from sklearn.metrics import confusion_matrix
from matrix_plot import plot_confusion_matrix
import numpy as np
import matplotlib.pyplot as plt



nlp = spacy.load('en')



def pass_act_detect(doc):
    parse = nlp(doc)
    newdoc = ''
    for sent in parse.sents:  # no meaning, test only take one sentence at a time.

        # Init parts of sentence to capture:
        subjpass = ''
        subj = ''
        verb = ''
        verbaspect = ''
        verbtense = ''
        adverb = {'bef':'', 'aft':''}
        part = ''
        prep = ''
        agent = ''
        aplural = False
        advcltree = None
        aux = list(list(nlp('. .').sents)[0]) # start with 2 'null' elements
        xcomp = ''
        punc = '.'
        # Analyse dependency tree:
        for word in sent:
            if word.dep_ == 'advcl':
                if word.head.dep_ in ('ROOT', 'auxpass'):
                    advcltree = word.subtree
            if word.dep_ == 'nsubjpass':
                if word.head.dep_ == 'ROOT':
                    subjpass = ''.join(w.text_with_ws.lower() if w.tag_ not in ('NNP','NNPS') else w.text_with_ws for w in word.subtree).strip()
            if word.dep_ == 'nsubj':
                subj = ''.join(w.text_with_ws.lower() if w.tag_ not in ('NNP','NNPS') else w.text_with_ws for w in word.subtree).strip()
                if word.head.dep_ == 'auxpass':
                    if word.head.head.dep_ == 'ROOT':
                        subjpass = subj
            if word.dep_ in ('advmod','npadvmod'):
                if word.head.dep_ == 'ROOT':
                    if verb == '':
                        adverb['bef'] = ''.join(w.text_with_ws.lower() if w.tag_ not in ('NNP','NNPS') else w.text_with_ws for w in word.subtree).strip()
                    else:
                        adverb['aft'] = ''.join(w.text_with_ws.lower() if w.tag_ not in ('NNP','NNPS') else w.text_with_ws for w in word.subtree).strip()
            if word.dep_ == 'auxpass':
                if word.head.dep_ == 'ROOT':
                    if not subjpass:
                        subjpass = subj
            if word.dep_ in ('aux','auxpass','neg'):
                if word.head.dep_ == 'ROOT':
                    aux += [word]
            if word.dep_ == 'ROOT':
                verb = word.text
                if word.tag_ == 'VB':
                    verbtense = en.INFINITIVE
                elif word.tag_ == 'VBD':
                    verbtense = en.PAST
                elif word.tag_ == 'VBG':
                    verbtense = en.PRESENT
                    verbaspect = en.PROGRESSIVE
                elif word.tag_ == 'VBN':
                    verbtense = en.PAST
                else:
                    verbtense = en.tenses(word.text)[0][0]
            if word.dep_ == 'prt':
                if word.head.dep_ == 'ROOT':
                    part = ''.join(w.text_with_ws.lower() if w.tag_ not in ('NNP','NNPS') else w.text_with_ws for w in word.subtree).strip()
            if word.dep_ == 'prep':
                if word.head.dep_ == 'ROOT':
                    prep = ''.join(w.text_with_ws.lower() if w.tag_ not in ('NNP','NNPS') else w.text_with_ws for w in word.subtree).strip()
            if word.dep_.endswith('obj'):
                if word.head.dep_ == 'agent':
                    if word.head.head.dep_ == 'ROOT':
                        agent = ''.join(w.text + ', ' if w.dep_=='appos' else (w.text_with_ws.lower() if w.tag_ not in ('NNP','NNPS') else w.text_with_ws) for w in word.subtree).strip()
                        aplural = word.tag_ in ('NNS','NNPS')
            if word.dep_ in ('xcomp','ccomp','conj'):
                if word.head.dep_ == 'ROOT':
                    xcomp = ''.join(w.text_with_ws.lower() if w.tag_ not in ('NNP','NNPS') else w.text_with_ws for w in word.subtree).strip()
            if word.dep_ == 'punct':
                punc = word.text

        # exit if not passive:
        if subjpass == '':
            newdoc += str(sent) + ' '
            return False #active

        return True #passive


#Testing

y_true = []
y_pred = []
with open("minisets.txt") as f:
    for line in f:
        if re.match(r'^\s*$', line):
            continue
        elif line.split('\n'):
            line = [line for line in line.split('\n') if line.strip() != ''][0]
            if (len(line.split(".")) == 2):
                sentence, label = line.split(".")
                label = label.strip().lower()
                detection = pass_act_detect(sentence)
                if detection:
                    y_pred.append("P")
                else:
                    y_pred.append("A") # false means active

                if label == "(passive)":
                    y_true.append("P")
                elif label == "(active)":
                    y_true.append("A") # false means active
                else:
                    print("something went wrong")


print ("prediction completed, generating confusion matrix")

cnf_matrix = confusion_matrix(y_true, y_pred)
np.set_printoptions(precision=2)
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=["Active","Passive"],
                      title='Confusion matrix, without normalization')
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=["Active","Passive"], N=True,
                      title='Normalized confusion matrix')

plt.show()
