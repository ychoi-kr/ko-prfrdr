#!/usr/bin/python

import argparse
from glob import glob
import os


def main(book_title, directory, encoding, sub_dir='merged'):
    if directory:
        os.chdir(directory)
    
    if not os.path.isdir(sub_dir):
        os.mkdir(sub_dir)
    
    try:
        with open(f"{sub_dir}/{bookname}.txt", "wt", encoding=encoding) as outfile:
            for title in glob(f"{book_title}*.txt"):
                infile = open(title, "rt", encoding=encoding)
                outfile.write(title + '\n')
                outfile.write('-' * len(title) + '\n')
                outfile.write(infile.read() + "\n\n")
    except UnicodeDecodeError as e:
        print("An Exception raised:", e)
        print("Try again with option: -e utf-8")


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
