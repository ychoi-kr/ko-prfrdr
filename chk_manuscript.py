import os
import glob
import sys
import re
import json
import argparse
import pathlib
from collections import Counter

import docx2txt


def debug(k, v):
    if _dbg_:
        print(f'#DEBUG# {k}: {v}')
        input()


def main(infile, rulefile):
    global _dbg_
    _dbg_ = False
    
    debug('infile', infile)
    if not infile:
        infile = latest_docx()
    
    _rules = loadrules(rulefile)
    
    try:
        text = read_manuscript(infile)
    except PermissionError:
        print(f"Failed!!! Please close {infile} and retry...", file=sys.stderr)
        sys.exit()
    
    global warnings_counter
    warnings_counter = Counter()
    
    for paragraph in text.splitlines(True):
        for line in re.split(r'(?<=[.?]) ', paragraph):
            check(_rules, line)
    
    display_summary()


def loadrules(rulefile):
    allrules = []
    for filename in rulefile:
        path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), filename
        )
        
        print(f"Loading rule {filename}...")
        try:
            fileobj = open(path, "rt")
            pyobj = decodejson(fileobj, filename)
        except UnicodeDecodeError as ude:
            fileobj = open(path, "rt", encoding='utf8')
            pyobj = decodejson(fileobj, filename)
        else:
            allrules += ruletable(pyobj)
    
    return allrules


def decodejson(fileobj, filename):
    try:
        return json.load(fileobj)
    except json.decoder.JSONDecodeError as jde:
        sys.exit(f'Unable to decode {filename}\n{jde}')


def ruletable(obj):
    table = []
    for rule in obj:
        caselist = []
        for rc in rule['cases']:
            if len(rc[0]) > 4 and rc[0][:4] in ['~은/는', '~이/가', '~을/를']:
                caselist.append(('~' + rc[0][1] + rc[0][4:], rc[1]))
                caselist.append(('~' + rc[0][3] + rc[0][4:], rc[1]))
            else:
                caselist.append((rc[0], rc[1]))
        table.append((rule['kind'], rule['name'], rule['desc'], caselist, rule['exception']))
    return table


def read_manuscript(infile):
    ext = pathlib.Path(infile).suffix
    debug('ext', ext)
    if ext == ".docx":
        print(f'Loading docx file: {infile}...')
        text = docx2txt.process(infile)
    elif ext in ['.txt', '.md']:
        try:
            print(f'Loading text file: {infile}...')
            text = open(infile).read()
        except UnicodeDecodeError:
            print(f'Retrying to load text file in UTF-8: {infile}...')
            text = open(infile, encoding='utf8').read()
    else:
        sys.exit('Unable to parse file!')
    return text


def check(rules, line):

    # avoid false positive on rule108
    if not korean(line):
        return None
    
    for rule in rules:
        kind, name, desc, cases, exceptions = rule
        for cs in cases:
            bad, good = cs[0], cs[1]
            
            if bad == '?':  # possible charset problem
                continue
            
            bad_root = bad
            if bad.startswith('~'):
                bad_root = bad.lstrip('~')
            if bad.endswith(')') and korean(bad.rstrip(')').rsplit('(', 1)[1]):
                bad_root = bad_root.rsplit('(', 1)[0]
            
            debug('line', line)
            debug('bad_root', bad_root)
            
            if bad_root in line:
                loc = line.find(bad_root)
                skip = False
                for ex in exceptions:
                    beg, end = 0, -1
                    sz = 10
                    if loc > sz:
                        beg = loc - sz
                    if len(line) - loc > 10:
                        end = loc + sz
                    window = line[beg:end]
                    
                    if ex in window:
                        skip = True
                    
                if not skip:
                    cl = carret_loc(line, loc)
                    print('* ' + line)
                    print('  ' + ' ' * cl + '^')
                    message(kind, name, bad, good, desc)
                    warnings_counter[name] += 1


def carret_loc(s, loc):
    for c in s[:loc]:
        if korean(c):
            loc += 1
    return loc


def korean(s):
    return len(list(filter(lambda x: '가' < x < '힣', s))) > 0


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


def latest_docx():
    ext = 'docx'
    try:
        return max(glob.glob(f'*.{ext}'), key=os.path.getctime)
    except:
        sys.exit(f"Failed!!! Cannot find {ext} file.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="filename", type=str)
    parser.add_argument("-r", "--rulefile", nargs='+',
                        default=['ko_spelling_rules.json', 'ko_spacing_rules.json', 'foreign_sound_rules.json',
                                 'en_ko_style_correction.json', 'jp_ko_style_correction.json', 'wikibook_style_guide.json'])
    args = parser.parse_args()
    
    main(args.filename, args.rulefile)
