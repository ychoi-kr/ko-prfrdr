import os
import sys
import json
import argparse
from collections import Counter

import docx2txt

def main(infile):
    text = read_manuscript(infile)
    
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "ko_spelling_rules.json"
    )
    with open(path) as json_file:
        rules = json.load(json_file)
    
    global warnings_counter
    warnings_counter = Counter()
    
    for paragraph in text.split('\n'):
        lines = paragraph.split(". ")
        if len(lines) > 1:
            for line in lines[:-1]:
                check(rules, line + '.')
        check(rules, lines[-1])
    
    display_summary()

def read_manuscript(infile):
    if infile.endswith('.docx'):
        text = docx2txt.process(infile)
    elif infile.endswith('.txt'):
        text = open(textfile).read()
    else:
        sys.exit('Unable to parse file!')
    return text

def check(rules, line):

    # avoid false positive on rule 1.8
    korean_sentence = False
    for c in line:
        if korean(c):
            korean_sentence = True
            break
    if not korean_sentence:
        return None
    
    for rule in rules:
        for case in rule['cases']:
            bad, good = case[0], case[1]
            bad_stripped = bad.lstrip('~').rstrip('(다)')
            if bad_stripped in line:
                loc = line.find(bad_stripped)
                skip = False
                for exception in rule['exception']:
                    offset = exception.find(bad_stripped)
                    if line[loc - offset:].startswith(exception):
                        skip = True
                if not skip:
                    loc = calculate_loc(line, loc)
                    print('* ' + line)
                    print('  ' + ' ' * loc + '^')
                    message(rule['kind'], rule['name'], bad.replace('(다)', '다'), good.replace('(다)', '다'), rule['desc'])
                    
                    warnings_counter[rule['name']] += 1

def calculate_loc(s, loc):
    for c in s[:loc]:
        if korean(c):
            loc += 1
    return loc

def korean(c):
    return '가' < c < '힣'

def message(kind, name, bad, good, desc):
    if bad.startswith(". "):  # do not use lstrip() because it works differently
        bad = bad[2:]
    guide = " → ".join(filter(None, [bad, good]))
    ref = " : ".join(filter(None, [name, desc]))
    print(f'  => {guide}\t ({ref})\n\n')

def display_summary():
    print('=== Summary ===')
    for ele in sorted(warnings_counter):
        print(f'{ele} ==> count: {warnings_counter[ele]}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="filename")
    args = parser.parse_args()
    
    main(args.filename)
