#!/usr/bin/python3

import os
import sys
import re
import json
import argparse
from pathlib import Path
from collections import Counter
import zipfile

from kosound import hasfinalconsonant
import kostr
import koletter
import koeomi
import kojosa
import koword
import fileconverter as fc
import fileutil

import docx2txt

print(f'Trying to import KoNLPy...')
try:
    from konlpy.tag import Komoran
    global komoran
    dicpath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'dic.txt'
    )
    komoran = Komoran(userdic=dicpath)

    from konlpy.tag import Okt
    global okt
    okt = Okt()
except:
    pass


def _debug(k, v=None):
    if '_dbg_' in globals() and _dbg_ == True :
        print(f"#DEBUG# {k}", end='')
        if v:
            print(f": {v}")
        #input()


def main(infile, rulefile, debug=False):
    global _dbg_
    _dbg_ = debug
    
    _rules = loadrules(rulefile)
    
    if not infile:
        infile = fileutil.latest_file()
    
    filetoread = fc.convert(infile)

    try:
        text = read_manuscript(filetoread)
    except PermissionError:
        sys.exit(f"Failed!!! Please close {filetoread} and retry...")
    
    global warnings_counter
    warnings_counter = Counter()
    
    try:
        for paragraph in text.splitlines(True):
            for line in re.split(r'(?<=[.?]) ', paragraph):
                corrections = check(_rules, line)
                display_corrections(line, corrections)
        display_summary()
    except BrokenPipeError:  # when user hits 'q' during using pipe
        pass  


def loadrules(rulefile):
    allrules = []
    for filename in rulefile.split(' '):
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
                try:
                    caselist.append(('~' + rc[0][1] + rc[0][4:], '~' + rc[1][1] + rc[1][4:]))
                except:
                    caselist.append(('~' + rc[0][1] + rc[0][4:], rc[1]))
                try: 
                    caselist.append(('~' + rc[0][3] + rc[0][4:], '~' + rc[1][3] + rc[1][4:]))
                except:
                    caselist.append(('~' + rc[0][3] + rc[0][4:], rc[1]))
            else:
                caselist.append((rc[0], rc[1]))
        table.append((rule['kind'], rule['name'], rule['desc'], caselist, rule['exception']))
    return table


def read_manuscript(infile):
    ext = Path(infile).suffix
    if ext == ".docx":
        print(f'Loading docx file: {infile}...')
        try:
            text = docx2txt.process(infile)
        except zipfile.BadZipFile:
            print('Failed to load file! Please try agian after sync completed')
            sys.exit(1)

    elif ext in ['.txt', '.md', '.yaml']:
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

    result = []

    #_debug('line', line)
    #_debug('komoran.pos(line)', komoran.pos(line))

    for rule in rules:
        kind, name, desc, cases, exceptions = rule
        for cs in cases:
            bad, good = cs[0], cs[1]
            mode = None
             
            if bad == '?':  
                mode = "Error"
                #_debug('mode', mode)
                continue

            elif re.match('^(ignored|dup)[:]', bad):
                continue
                 
            elif any(map(lambda x: x in '[]\+?|', bad)):
                mode = "regex"
                #_debug('mode', mode)

                for x in dir(koletter): 
                    if 'KL' in x:
                        bad = bad.replace(x, getattr(koletter, x))
                for x in dir(koeomi): 
                    if x.startswith('KE'):
                        bad = bad.replace(f'({x})', f'({getattr(koeomi, x)})')
                for x in dir(kojosa): 
                    if x.startswith('KJ'):
                        bad = bad.replace(f'({x})', f'({getattr(kojosa, x)})')
                for x in dir(koword): 
                    if x.startswith('KW') or 'KC' in x:
                        bad = bad.replace(f'({x})', f'({getattr(koword, x)})')

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

                    # use slicing and buffer approach instead of replace() method
                    # to process parentheses in patterns properly
                    strbuf = ''
                    remain = good
                    for i, g in enumerate(m.groups(), start=1):
                        if '_dbg_' in globals() and _dbg_:
                            strbuf += remain[:remain.index('()')] + g
                            remain = remain[remain.index('()') + len('()'):]
                        if f'({i})' in remain:
                            strbuf += remain[:remain.index(f'({i})')] + g
                            remain = remain[remain.index(f'({i})') + len(f'({i})'):]
                        elif '()' in remain:
                            strbuf += remain[:remain.index('()')] + g
                            remain = remain[remain.index('()') + len('()'):]
                        else:
                            pass
                    good = strbuf
                else:
                    continue
                 
            else: 
                bad_root = bad
                if bad.endswith(')') and korean(bad.rstrip(')').rsplit('(', 1)[1]):
                    bad_root = bad.rsplit('(', 1)[0]
                 
                # Part of Speech match
                if 'okt' in globals() and any(x in bad_root for x in ['<Adjective>', '<Adverb>', '<Verb>', '<Josa>']):
                    mode = 'Okt'
                    _debug('mode', mode)
                    #_debug('okt.pos(line)', okt.pos(line))
                    _bad = bad
                    _bad_root = bad_root
                    _good = good
                    for a in re.findall('<\w+>', bad_root):
                        for b in [m for m, p in okt.pos(line) if f'<{p}>' == a]:
                            _bad = _bad.replace(a, b, 1)
                            _bad_root = _bad_root.replace(a, b, 1)
                            #_debug('_bad_root', _bad_root)
                            _good = _good.replace(a, b, 1)
                            
                            if _bad_root in line:
                                _debug('okt.pos(line)', okt.pos(line))
                                bad = _bad
                                bad_root = _bad_root
                                good = _good
                        else:
                            continue
                        break

                # below looks very expensive. may need some optimization.
                elif 'komoran' in globals() and re.search(r"<\w+>", bad_root):
                    # remove errornous characters before using tagger
                    line = re.sub(r'[^\w\s!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~]', '', line)
                    #_debug('line', line)
                    morphs_line = ' '.join([''.join(komoran.morphs(eojeol)) for eojeol in line.split()])
                    if '<Noun>' in bad_root:
                        mode = 'Komoran_Noun'
                        _debug('mode', mode)
                        _debug('<Noun> exists in bad_root', bad_root)
                        nouns = komoran.nouns(line)
                        #_debug('nouns', nouns)
                        for n in nouns:
                            candidate = bad_root.replace('<Noun>', n)
                            if candidate in line:
                                _debug('komoran.pos(line)', komoran.pos(line))
                                bad = bad_root = candidate
                                good = good.replace('<Noun>', n)
                                good = good.replace('()', n)
                                break
                    else:
                        #_debug('komoran.pos(line)', komoran.pos(line))
                        mode = 'Komoran_POS'
                        #_debug('mode', mode)
                        #_debug('bad', bad)
                        _bad = bad
                        _bad_root = bad_root
                        _good = good
                        for a in re.findall('<\w+>', bad_root):
                            for b in [m for m, p in komoran.pos(line) if f'<{p}>' == a]:
                                _bad = _bad.replace(a, b, 1)
                                _bad_root = _bad_root.replace(a, b, 1)
                                #_debug('_bad_root', _bad_root)
                                _good = _good.replace(a, b, 1)
                                
                                #_debug('morphs_line', morphs_line) 
                                if _bad_root in line or _bad_root in morphs_line:
                                    _debug('morphs_line', morphs_line)
                                    bad_root = _bad_root
                                    _debug('_bad_root', _bad_root)
                                    _debug('bad_root', bad_root)
                                    _debug('_bad', _bad)
                                    #bad = kostr.join(komoran.morphs(_bad))
                                    bad = ' '.join([kostr.join(komoran.morphs(eojeol)) for eojeol in _bad.split()])
                                    _debug('bad', bad)
                                    good = ' '.join([kostr.join(komoran.morphs(eojeol)) for eojeol in _good.split()])
                                    _debug('good', good)
                            else:
                                continue
                            break 
                 
                # Plaintext match
                else:
                    mode = 'Plaintext'
                    #_debug('mode', mode)
                    if bad_root.startswith('~'):
                         bad_root = bad_root.lstrip('~')
                 
            # common
            if bad_root in line or (
                mode.startswith('Komoran') and ''.join(komoran.morphs(bad_root)) in morphs_line
            ):
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
                    if 'warnings_counter' in globals():
                        warnings_counter[name] += 1

                    result.append((loc, kind, name, bad, good, desc))

    return result


def display_corrections(line, corrections):
    if line.strip() in ['true cases:', 'false cases:']:
        print(line.strip())
    elif corrections:
        bullet = ''  # '*'
        space = ''  # ' '
        offset = len(bullet) + len(space)
        print(bullet + space + line)
        for cor in corrections:
            loc, kind, name, bad, good, desc = cor
            cl = carret_loc(line, loc)
            print(' ' * offset + ' ' * cl + '^')
            message(kind, name, bad, good, desc)


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
    arr = '\n   →  ' if len(bad) > 20 else ' →  '
    guide = arr.join(filter(None, [bad, good]))
    ref = " : ".join(filter(None, [name, desc]))
    print(f'   => {guide}\t ({ref})\n')
    sys.stdout.flush()


def display_summary():
    print('=== Summary ===')
    for ele in sorted(warnings_counter):
        print(f'{ele} ==> count: {warnings_counter[ele]}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", type=str)
    
    default_rules = ['ko_spelling_rules.json', 'ko_spacing_rules.json',
                     'foreign_sound_rules.json', 'en_ko_style_correction.json',
                     'ja_ko_style_correction.json', 'wikibook_style_guide.json',
                     'simple_style.json']
    parser.add_argument("-r", "--rulefile", default=' '.join(default_rules))
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    
    main(args.filename, args.rulefile, args.debug)
