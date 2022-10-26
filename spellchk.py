#!/usr/bin/python3

import os
import argparse
import proofread as prf

parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs="?", type=str)

default_rules = [
    'en_spelling_rules.json',
    'ko_foreign_word.json',
    'ko_spacing_rules.json',
    'ko_spelling_rules.json',
    'ko_terms_error.json',
]
parser.add_argument("-r", "--rulefile", default=' '.join(default_rules))
parser.add_argument("--show_all_lines", action="store_true")
parser.add_argument("--debug", action="store_true")
parser.add_argument("--profile", action="store_true")
args = parser.parse_args()
    
prf.main(args.filename, args.rulefile, args.show_all_lines, args.debug, args.profile)
