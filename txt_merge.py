#!/usr/bin/python

import argparse
from glob import glob
import os


def main(bookname, directory, encoding, sub_dir='merged'):
    if directory:
        os.chdir(directory)
    
    if not os.path.isdir(sub_dir):
        os.mkdir(sub_dir)
    
    try:
        with open(f"{sub_dir}/{bookname}.txt", "wt", encoding=encoding) as outfile:
            for title in get_sorted_filenames(bookname):
                infile = open(title, "rt", encoding=encoding)
                outfile.write(title + '\n')
                outfile.write('-' * len(title) + '\n')
                outfile.write(infile.read() + "\n\n")
    except UnicodeDecodeError as e:
        print("An Exception raised:", e)
        print("Try again with option: -e utf-8")


def get_sorted_filenames(title):
    possible_delimiter = '-_'
    for d in possible_delimiter:
        filenames = glob(f"{title}{d}*.txt")
        prefix = title + d
        suffix = '.txt'
        if all([f.startswith(prefix) and f.endswith(suffix) for f in filenames]):
            middle = [int(f.replace(prefix, '').replace(suffix, '')) for f in filenames]
            filenames = [prefix + str(m) + suffix for m in sorted(middle)]
            break

    return filenames


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="directory where files to be merged live")
    parser.add_argument("bookname")
    parser.add_argument("-e", "--encoding", help="specify encoding(ex: utf-8)")
    args = parser.parse_args()
    directory = args.directory
    bookname = args.bookname
    encoding = args.encoding
    
    main(args.bookname, args.directory, args.encoding)
