#!/usr/bin/python3

import os
import argparse
import chk_manuscript

parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs="?", type=str)

default_rules = ['en_ko_style_correction.json', 'ja_ko_style_correction.json',
         'wikibook_style_guide.json', 'simple_style.json']
parser.add_argument("-r", "--rulefile", default=' '.join(default_rules))
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()
    
chk_manuscript.main(args.filename, args.rulefile, args.debug)
