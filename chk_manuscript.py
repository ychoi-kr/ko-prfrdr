#!/usr/bin/python3

import os
import glob
import sys
import re
import json
import argparse
from pathlib import Path
from collections import Counter

from kosound import hasfinalconsonant
import fileconverter as c

import docx2txt

TAG_PACKAGE = 'Komoran'
print(f'Trying to import KoNLPy...')
try:
    from konlpy.tag import Komoran
    from konlpy.tag import Okt
    global komoran
    dicpath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'dic.txt'
    )
    komoran = Komoran(userdic=dicpath)
    global okt
    okt = Okt()
except:
    pass

def _debug(k, v=None):
    if _dbg_:
        print(f"#DEBUG# {k}", end='')
        if v:
            print(f": {v}")
        #input()


def main(infile, rulefile, debug=False):
    global _dbg_
    _dbg_ = debug
    
    _rules = loadrules(rulefile)
    
    if not infile:
        infile = latest_docx()
    
    ext = Path(infile).suffix
    
    if ext == '.pdf':
        if not c.pdfsupport():
            sys.exit('Failed!!! PDF support is not enabled.')
        if c.pdftotext(infile):
            infile = Path(infile).stem + '.txt'
    elif ext == '.hwp':
        if not c.hwpsupport():
            sys.exit('Failed!!! HWP support is not enabled.')
        if c.hwptotext(infile):
            infile = Path(infile).stem + '.txt'
    elif ext in ['.docx', '.txt', '']:
        pass
    else:
        sys.exit(f'Failed!!! {ext} is not supported')
    
    try:
        text = read_manuscript(infile)
    except PermissionError:
        print(f"Failed!!! Please close {infile} and retry...", file=sys.stderr)
        sys.exit()
    
    global warnings_counter
    warnings_counter = Counter()
    
    try:
        for paragraph in text.splitlines(True):
            for line in re.split(r'(?<=[.?]) ', paragraph):
                check(_rules, line)
        display_summary()
    except BrokenPipeError:  # when user hits 'q' during using pipe
        pass  


def loadrules(rulefile):
    allrules = []
    for filename in rulefile:
        path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), filename
        )
        
        print(f"Loading rule file: {filename}...")
        fileobj = open(path, "rt", encoding='utf8')
        pyobj = decodejson(fileobj, filename)
        
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
            if len(rc[0]) > 4 and rc[0][:4] in ['~은/는', '~이/가', '~을/를', '~와/과']:
                caselist.append(('~' + rc[0][1] + rc[0][4:], '~' + rc[1][1] + rc[1][4:]))
                caselist.append(('~' + rc[0][3] + rc[0][4:], '~' + rc[1][3] + rc[1][4:]))
            else:
                caselist.append((rc[0], rc[1]))
        table.append((rule['kind'], rule['name'], rule['desc'], caselist, rule['exception']))
    return table


def read_manuscript(infile):
    ext = Path(infile).suffix
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
        sys.exit(f'Failed!!! Unable to parse file: {infile}')
    return text


def check(rules, line):
    # avoid false positive on rule108
    if not korean(line):
        return None
    
    _debug('line', line)

    def parse(sentence):
        return ' '.join([''.join(komoran.morphs(eojeol)) for eojeol in sentence.split()])

    for rule in rules:
        kind, name, desc, cases, exceptions = rule
        for cs in cases:
            bad, good = cs[0], cs[1]
            mode = None
             
            if bad == '?':  
                _debug("possible charset problem")
                continue
             
            elif any(map(lambda x: x in '[]\+?|', bad)):
                _debug("regex match")
                _debug('bad', bad)
                m = re.search(bad, line)
                if m:
                    if (
                        'without_final_consonant' in bad
                        and hasfinalconsonant(m.group('without_final_consonant')[-1])
                    ) or (
                        'with_final_consonant' in bad
                        and not hasfinalconsonant(m.group('with_final_consonant')[-1])
                    ):
                        continue
                    
                    bad = bad_root = m.group()
                    for g in m.groups():
                        good = good.replace('()', g, 1)
                else:
                    continue
             
            else: 
                bad_root = bad
                if bad.endswith(')') and korean(bad.rstrip(')').rsplit('(', 1)[1]):
                    bad_root = bad.rsplit('(', 1)[0]

                # Part of Speech match
                if 'okt' in globals() and ('<Verb>' in bad_root or '<Josa>' in bad_root):
                    _debug('Okt POS exists in bad_root', bad_root)
                    _debug('okt.pos(line)', okt.pos(line))
                    _bad = bad
                    _bad_root = bad_root
                    _good = good
                    for a in re.findall('<\w+>', bad_root):
                        for b in [m for m, p in okt.pos(line) if f'<{p}>' == a]:
                            _bad = _bad.replace(a, b, 1)
                            _bad_root = _bad_root.replace(a, b, 1)
                            _debug('_bad_root', _bad_root)
                            _good = _good.replace(a, b, 1)
                            
                            _debug('parse(line)', parse(line)) 
                            if parse(_bad_root) in parse(line):
                                bad = _bad
                                bad_root = _bad_root
                                good = _good
                        else:
                            continue
                        break
                elif 'komoran' in globals() and re.search(r"<\w+>", bad_root):
                    _debug('komoran.pos(line)', komoran.pos(line))
                    if '<Noun>' in bad_root:
                        _debug('<Noun> exists in bad_root', bad_root)
                        nouns = komoran.nouns(line)
                        for n in nouns:
                            candidate = bad_root.replace('<Noun>', n)
                            if candidate in line:
                                bad = bad_root = candidate
                                good = good.replace('()', n)
                                break
                    else:
                        _debug("POS tag other than <Noun> exists in bad_root", bad_root)
                        _bad = bad
                        _bad_root = bad_root
                        _good = good
                        for a in re.findall('<\w+>', bad_root):
                            for b in [m for m, p in komoran.pos(line) if f'<{p}>' == a]:
                                _bad = _bad.replace(a, b, 1)
                                _bad_root = _bad_root.replace(a, b, 1)
                                _debug('_bad_root', _bad_root)
                                _good = _good.replace(a, b, 1)
                                
                                _debug('parse(line)', parse(line)) 
                                if parse(_bad_root) in parse(line):
                                    bad = _bad
                                    bad_root = _bad_root
                                    good = _good
                            else:
                                continue
                            break 
                 
                # Plaintext match
                else:
                    if bad_root.startswith('~'):
                         bad_root = bad_root.lstrip('~')
    
            # common
            if bad_root in line or parse(bad_root) in parse(line):
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
    exts = [".txt", ".docx", ".pdf", ".hwp", '']
    files = []
    for ext in exts:
        files.extend(glob.glob('*' + ext))
    
    try:
        return max(files, key=os.path.getctime)
    except:
        sys.exit(f"Failed!!! Cannot find file in {'|'.join(exts)}.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", type=str)
    parser.add_argument("-r", "--rulefile", nargs='+',
                        default=['ko_spelling_rules.json', 'ko_spacing_rules.json', 'foreign_sound_rules.json',
                                 'en_ko_style_correction.json', 'jp_ko_style_correction.json',
                                 'wikibook_style_guide.json', 'simple_style.json'])
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    
    main(args.filename, args.rulefile, args.debug)
