import os
import argparse
import chk_manuscript

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help="filename", type=str)
parser.add_argument("-r", "--rulefile", nargs='+', 
                    default=['en_ko_style_correction.json', 'jp_ko_style_correction.json', 'wikibook_style_guide.json'])
args = parser.parse_args()

chk_manuscript.main(args.filename, args.rulefile)
