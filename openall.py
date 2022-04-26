from glob import glob, iglob
import win32com.client as win32
import os
import argparse

from natsort import natsorted

parser = argparse.ArgumentParser()
parser.add_argument("-R", "--recursive", action="store_true")
args = parser.parse_args()

word = win32.Dispatch('Word.Application')
word.Visible = True

if args.recursive:
    files = list(iglob(r'**/*.docx', recursive=True)) + list(iglob(r'**/*.doc', recursive=True))
else:
    files = glob(r'*.docx') + glob(r'*.doc')

for f in natsorted(files):
    p = os.getcwd() + os.sep + f
    print(f'Opening {p}...')
    word.Documents.Open(p)
