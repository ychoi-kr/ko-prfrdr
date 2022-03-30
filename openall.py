import glob
import win32com.client as win32
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-R", "--recursive", action="store_true")
args = parser.parse_args()

word = win32.Dispatch('Word.Application')
word.Visible = True

files = glob.iglob(r'**/*.docx', recursive=True) if args.recursive else glob.iglob(r'*.docx')

for f in files:
    p = os.getcwd() + os.sep + f
    print(f'Opening {p}...')
    word.Documents.Open(p)
