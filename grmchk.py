#!/usr/bin/python3

import os
import argparse
import proofread as prf

parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs="?", type=str)

default_rules = ['ko_grammar.json']
parser.add_argument("-r", "--rulefile", default=' '.join(default_rules))
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()
    
prf.main(args.filename, args.rulefile, args.debug)
