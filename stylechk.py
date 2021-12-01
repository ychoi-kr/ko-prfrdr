#!/usr/bin/python3

import os
import argparse
import chk_manuscript

parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs="?", type=str)
parser.add_argument("-r", "--rulefile", nargs='+', 
                    default=['en_ko_style_correction.json', 'jp_ko_style_correction.json',
                             'wikibook_style_guide.json', 'simple_style.json'])
args = parser.parse_args()

chk_manuscript.main(args.filename, args.rulefile)
