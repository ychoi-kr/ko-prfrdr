import argparse
from glob import glob
import os

from PyPDF2 import PdfFileMerger

def main(book_title, directory=".", sub_dir='merged'):
    merger = PdfFileMerger()
    
    for f in glob(f"{directory}/{book_title}*.pdf"):
        merger.append(f)

    os.chdir(directory)
    if not os.path.isdir(sub_dir):
        os.mkdir(sub_dir)

    merger.write(f"{directory}/{sub_dir}/{bookname}.pdf")
    merger.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="directory where files to be merged live")
    parser.add_argument("bookname")
    args = parser.parse_args()
    directory = args.directory
    bookname = args.bookname
    
    main(args.bookname, args.directory)
