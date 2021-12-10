#!/usr/bin/python3

import os
import sys
import re
import argparse
from pathlib import Path

from pikepdf import Pdf


def main(pdf_file, header, footer, password):
    y = header
    W = 700
    height = page_height(pdf_file, password)
    options_to_remove_header_and_footer = f'-y {header} -H {height - header - footer} -W {W}' if height else ''
    user_password_option = f'-upw {password}' if password else ''
    cmd = f"pdftotext {options_to_remove_header_and_footer} {user_password_option} -nopgbrk {pdf_file} -"
    s = os.popen(cmd).read()
    with open(Path(pdf_file).stem + ".txt", 'wt') as f:
        f.write(
            re.sub(r"(.*?[^.:])[‐]?\n+([a-z0-9(]|" + nnp() + ')', r'\1 \2', s)
        )


def page_height(filename, password):
    try:
        if password:
            pdf = Pdf.open(filename, password=password)
        else:
            pdf = Pdf.open(filename)
        firstpage = pdf.pages[0]
        return int(firstpage.MediaBox[3])
    except:
        print('Cannot get page height. Fallback.')
        return None


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
    parser.add_argument("--password", type=str) 
    args = parser.parse_args()
    main(args.pdf_file, args.header, args.footer, args.password)

