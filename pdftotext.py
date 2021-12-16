#!/usr/bin/python3

import os
import sys
import re
import argparse
from pathlib import Path

from pikepdf import Pdf


WIDTH_LIMIT = 700
MINIMUM_HEIGHT = 600
SUPPRESS_OUTPUT = True

def main(pdf_file, header, footer, password):
    quiet = '-q' if SUPPRESS_OUTPUT else ''

    if password:
        user_password = f'-upw "{password}"'
        pdf = Pdf.open(pdf_file, password=password)
    else:
        user_password = ''
        pdf = Pdf.open(pdf_file)
    
    with open(Path(pdf_file).stem + ".txt", 'wt') as f:
        for n in range(len(pdf.pages)):
            pagenum = f'-f {n + 1} -l {n + 1}'
    
            # check every page's dimension because all pages are not same always
            p = pdf.pages[n]
            width, height = int(p.trimbox[2]), int(p.trimbox[3])
    
            # horizontal dimensions
            area_per_side = []
            if width < WIDTH_LIMIT:  # single-sided
                area_per_side.append(f'-x 0 -W {width}')
            else:  #double-sided
                area_per_side.append(f'-x 0 -W {width // 2}')
                area_per_side.append(f'-x {width // 2} -W {width // 2}')
    
            for area in area_per_side:
                # vertical dimensions
                if height > MINIMUM_HEIGHT:
                    area += f' -y {header} -H {height - header - footer}'
                else:
                    area += f' -y 0 -H {height}'
                
                # extract text
                cmd = f'pdftotext {pagenum} {area} {user_password} {quiet} -nopgbrk "{pdf_file}"  -'
                #print(cmd)
                s = os.popen(cmd).read()
                s = re.sub(r"(.*?[^.:][^‐/])\n+([a-z0-9가-힣(]|" + nnp() + ')', r'\1 \2', s)
                s = re.sub(r"(.*?[^.:])[ ‐/]\n+(\w)", r'\1\2', s)
                f.write(s)


def page_info(filename, password):
    try:
        if password:
            pdf = Pdf.open(filename, password=password)
        else:
            pdf = Pdf.open(filename)
        ret = {}
        ret['pagenum'] = len(pdf.pages)
        b = pdf.pages[pagenum].trimbox
        ret['width'] = int(b[2])
        ret['height'] = int(b[3])
        return ret
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
    parser.add_argument("--header", default=50, type=int) 
    parser.add_argument("--footer", default=60, type=int) 
    parser.add_argument("--password", type=str) 
    args = parser.parse_args()
    main(args.pdf_file, args.header, args.footer, args.password)

