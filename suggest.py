#!/usr/bin/python3

import os
import argparse
import proofread as prf

parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs="?", type=str)
parser.add_argument("-r", "--rulefile", default=' '.join(prf.suggest_rules))
parser.add_argument("--show_all_lines", action="store_true")
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()
    
prf.main(args.filename, args.rulefile, args.show_all_lines, args.debug)
