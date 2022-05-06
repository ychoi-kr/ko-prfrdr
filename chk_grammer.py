#!/usr/bin/python3

import os
import argparse
import correct

parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs="?", type=str)

default_rules = ['ko_grammer.json']
parser.add_argument("-r", "--rulefile", default=' '.join(default_rules))
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()
    
correct.main(args.filename, args.rulefile, args.debug)
