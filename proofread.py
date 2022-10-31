#!/usr/bin/python3

import os
import sys
import re
import json
import argparse
from pathlib import Path
from collections import Counter
import zipfile
from time import process_time
from tqdm import tqdm

from kosound import hasfinalconsonant
import kostr
import koletter
import koeomi
import kojosa
import koword
import fileconverter as fc

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(iterator, *args, **kwargs):
        return iterator
    

profiler = dict()

def import_KoNLPy():
    print("Trying to import KoNLPy...")
    try:
        from konlpy.tag import Komoran
        global komoran
        dicpath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'dic.txt'
        )
        komoran = Komoran(userdic=dicpath)
        print("Komoran enabled")
    
        from konlpy.tag import Okt
        global okt
        okt = Okt()
        print("Okt enabled")
    except:
        pass


def _debug(k, v=None):
    if '_dbg_' in globals() and _dbg_ == True :
        print(f"#DEBUG# {k}", end='')
        if v:
            print(f": {v}")
        #input()


def main(infile, rulefile, show_all_lines=False, debug=False, profile=False):

    # needs to be here to avoid waisting time when '--help' option is used
    import_KoNLPy()

    global _dbg_
    _dbg_ = debug
    
    global warnings_counter
    warnings_counter = Counter()
    
    _rules = loadrules(rulefile)
    
    if infile:
        filetoread = fc.convert(infile)
        try:
            text = read_manuscript(filetoread)
        except PermissionError:
            sys.exit(f"Failed!!! Please close {filetoread} and retry...")

        paragraphs = text.splitlines(True)
    else:
        paragraphs = sys.stdin

    lines = []
    for paragraph in paragraphs:
        lines += re.split(r'(?<=[.?]) ', paragraph)

    try:
        for line in tqdm(lines):
            corrections = check(_rules, line, show_all_lines)
            display_corrections(line, corrections, show_all_lines)
        display_summary()
    except BrokenPipeError:  # when user hits 'q' during using pipe
        pass  
    
    if profile:
        print("***Profile***")
        for x in profiler.keys():
            print(x.split('_')[0], profiler[x])

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

        profiler[rule['name']] = 0

    return table


def read_manuscript(infile):
    ext = Path(infile).suffix
    if ext == ".docx":
        try:
            print("Trying to import docx2txt package...")
            import docx2txt
        except:
            sys.exit("Cannot import docx2txt!")

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


def check(rules, line, show_all_lines, profiler=profiler):

    line = line.replace('“', '"').replace('”', '"')
    line = line.replace("‘", "'").replace("’", "'")

    if show_all_lines:
        print(line)

    # avoid false positive on rule108
    if not korean(line):
        return None

    result = []

    if not show_all_lines:
        _debug('line', line)

    for rule in rules:
        kind, name, desc, cases, exceptions = rule
        start = process_time()
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

                    k = 1
                    for s in re.findall("(?<=[(])[1-9]*(?=[)])", good):
                        n = int(s) if len(s) > 0 else k 
                        k += 1

                        if '_dbg_' in globals() and _dbg_:
                            if '()' in remain:
                                strbuf += remain[:remain.index('()')] + m.group(n)
                                remain = remain[remain.index('()') + len('()'):]
                        if f'({n})' in remain:
                            strbuf += remain[:remain.index(f'({n})')] + m.group(n)
                            remain = remain[remain.index(f'({n})') + len(f'({n})'):]
                        elif '()' in remain:
                            try:
                                strbuf += remain[:remain.index('()')] + m.group(n)
                                remain = remain[remain.index('()') + len('()'):]
                            except:
                                sys.exit("Failed!!! Parenthesis not match in rule " + name)
                        else:
                            pass

                    good = strbuf + remain
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
                    #morphs_line = ' '.join([''.join(komoran.morphs(eojeol)) for eojeol in line.split()])
                    morphs_line = ''.join(
                        [''.join(komoran.morphs(x) if komoran.morphs(x) else x) for x in re.split('(\W)', line) if x != '']
                    )
                    if '<Noun>' in bad_root:
                        mode = 'Komoran_Noun'
                        _debug('mode', mode)
                        _debug('<Noun> exists in bad_root', bad_root)
                        nouns = komoran.nouns(line)
                        _debug('nouns', nouns)
                        for n in nouns:
                            candidate = bad_root.replace('<Noun>', n)
                            if candidate in line:
                                _debug('komoran.pos(line)', komoran.pos(line))
                                bad = bad_root = candidate
                                good = good.replace('<Noun>', n)
                                good = good.replace('()', n)
                                break
                        _debug('good', good) 
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
                                    bad = ''.join([(kostr.join(komoran.morphs(x)) if x != ' ' else x) for x in re.split('(\W)', _bad) if x != ''])
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
        end = process_time()

        profiler[name] += (end - start)

    return result


def display_corrections(line, corrections, show_all_lines):
    if line.strip() in ['true cases:', 'false cases:']:
        if not show_all_lines:
            print(line.strip())
    elif corrections:
        bullet = ''  # '*'
        space = ''  # ' '
        offset = len(bullet) + len(space)
        if not show_all_lines:
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

spellchk_rules = [
    'en_spelling_rules.json',
    'ko_foreign_word.json',
    'ko_spacing_rules.json',
    'ko_spelling_rules.json',
    'ko_terms_error.json',
]

stylechk_rules = [
    'en_ko_style_correction.json',
    'ja_ko_style_correction.json',
    'concise_writing.json',
    'wikibook_style_guide.json',
    'ko_grammar.json',
]

suggest_rules = [
    'ko_electric_terms.json',
    'ko_forest_terms.json',
    'ko_gov_terms_2012.json',
    'ko_norm_2002.json',
    'ko_plain.json',
    'ko_standard_terms.json',
    'ko_unbiased.json',
]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", type=str)
    
    default_rules = spellchk_rules + stylechk_rules + suggest_rules
    parser.add_argument("-r", "--rulefile", default=' '.join(default_rules))

    parser.add_argument("--show_all_lines", action="store_true")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--profile", action="store_true")
    args = parser.parse_args()
    
    main(args.filename, args.rulefile, args.show_all_lines, args.debug, args.profile)
