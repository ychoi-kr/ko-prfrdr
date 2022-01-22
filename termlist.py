import sys
import re
import argparse
from collections import Counter

import fileutil
import fileconverter as fc

import docx2txt


def main(infile):
    filetoread = fc.convert(infile)

    try:
        text = read_manuscript(filetoread)
    except PermissionError:
        print(f"Failed!!! Please close {filetoread} and retry...", file=sys.stderr)
        sys.exit()
    
    global term_counter, width
    term_counter = Counter()
    width = 50
    
    for paragraph in text.splitlines(True):
        for line in re.split(r'(?<=[.?]) ', paragraph):
            check(line)
    
    display_summary()

def debug(k, v):
    if _dbg_:
        print(f'#DEBUG# {k}: {v}')
        input()

def read_manuscript(filename):
    if filename.endswith('.docx'):
        text = docx2txt.process(filename)
    elif filename.endswith('.txt'):
        text = open(filename).read()
    else:
        sys.exit('Unable to parse file!')
    return text

def check(line):
    for s in re.findall(r'[가-힣 ]+\([^)]+\)?', line):
        t = re.split('[()]', s)
        if not korean(t[0]) or korean(t[1]):
            continue
        if t[1].startswith('http'):
            continue
        if re.match('[A-Za-z]+', t[1]) and len(re.findall(',', t[1])) <= 1 :
            term_counter[t[1]] += 1


def korean(s):
    return len(list(filter(lambda x: '가' < x < '힣', s))) > 0

def message(kind, name, bad, good, desc):
    if bad.startswith(". "):  # do not use lstrip() because it works differently
        bad = bad[2:]
    guide = " → ".join(filter(None, [bad, good]))
    ref = " : ".join(filter(None, [name, desc]))
    print(f'  => {guide}\t ({ref})\n\n')

def display_summary():
    print(f"{'TERM': <{width}} COUNT")
    for t in sorted(term_counter, key=str.casefold):
        cnt = term_counter[t]
        print(f'{t: <{width}} {cnt}')


if __name__ == '__main__':
    global _dbg_
    _dbg_ = True
    
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", type=str)
    #parser.add_argument("-f", "--filename", help="filename", default=fileutil.latest_file(['.docx']), type=str)
    args = parser.parse_args()
    
    main(args.filename)
