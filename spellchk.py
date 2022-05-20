#!/usr/bin/python3

import os
import argparse
import correct

parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs="?", type=str)

default_rules = ['ko_spelling_rules.json', 'ko_spacing_rules.json',
         'foreign_sound_rules.json']
parser.add_argument("-r", "--rulefile", default=' '.join(default_rules))
parser.add_argument("--show_all_lines", action="store_true")
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()
    
correct.main(args.filename, args.rulefile, args.show_all_lines, args.debug)
