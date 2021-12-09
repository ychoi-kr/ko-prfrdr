#!/usr/bin/python3

import os
import sys
import re
import argparse
from pathlib import Path

from pdfrw import PdfReader


def main(pdf_file, header, footer):
    y = header
    H = height(pdf_file) - header - footer
    W = 700
    cmd = f"pdftotext -y {y} -H {H} -W {W} -nopgbrk {pdf_file} -"
    s = os.popen(cmd).read()
    with open(Path(pdf_file).stem + ".txt", 'wt') as f:
        f.write(
            re.sub(r"(.*?[^.:])[‐]?\n+([a-z0-9(]|" + nnp() + ')', r'\1 \2', s)
        )


def height(pdf_file):
    return round(float(PdfReader(pdf_file).pages[0].MediaBox[3]))


def nnp():
    words = []
    dicpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'dic.txt')
    for l in open(dicpath).readlines():
        w, pos = l.split('\t')
        if pos.rstrip() == 'NNP':
            words.append(w)
    return '|'.join(words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_file", type=str)
    parser.add_argument("--header", default=70, type=int) 
    parser.add_argument("--footer", default=50, type=int) 
    args = parser.parse_args()
    main(args.pdf_file, args.header, args.footer)

