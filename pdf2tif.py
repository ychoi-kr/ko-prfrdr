#!/usr/bin/python3
from pdf2image import convert_from_path, convert_from_bytes
import argparse
import os
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("pdffile", type=str)
parser.add_argument("--dpi", default=300, type=int)
parser.add_argument("-S", "--start", default=1, type=int)
args = parser.parse_args()

# You have to get images before changing working directory
images = convert_from_path(os.path.abspath(args.pdffile), dpi=args.dpi)

dirname = Path(args.pdffile).stem
if not os.path.isdir(dirname):
    os.mkdir(dirname)
os.chdir(dirname)

for i, image in enumerate(images):
    image.save(f'{i + args.start}.tif')

