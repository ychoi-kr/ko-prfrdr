import os
import sys
import platform
from pathlib import Path


def pdfsupport():
    # I decided to reuse "pdftotext.exe" from Xpdf tools (http://www.xpdfreader.com/about.html)
    # which is already installed on my PC.
    # Python package equivalents are too hard to set up on Windows.
    # https://github.com/jalan/pdftotext/issues/16#issuecomment-399963100

    cmd = 'pdftotext -v > /dev/null'
    wincmd = 'pdftotext -v > NUL'
    return runcmd(cmd, wincmd=wincmd)


def hwpsupport():
    cmd = 'hwp5txt -h > /dev/null'
    wincmd = 'hwp5txt -h > NUL'
    return runcmd(cmd, wincmd= wincmd)


def pdftotext(infile):
    print(f'Converting {infile} to txt...')
    cmd = 'pdftotext "{infile}" > /dev/null'
    wincmd = 'pdftotext "{infile}" > NUL'
    return runcmd(cmd, wincmd=wincmd, infile=infile)


def hwptotext(infile):
    print(f'Converting {infile} to txt...')
    cmd = 'hwp5txt "{infile}" > "{outfile}"'
    return runcmd(cmd, infile=infile)


def runcmd(cmd, wincmd=None, infile=None):
    d = {}

    if infile:
        d['infile'] = infile
        d['outfile'] = Path(infile).stem + ".txt"

    if platform.system() == 'Windows':
        d['cmd'] = wincmd if wincmd else cmd
    else:
        d['cmd'] = cmd

    cmd = cmd.format(**d)

    rc = os.system(cmd)
    if rc == 0:
        return True
    else:
        return False


def convert(filename):
    result = None
    ext = Path(filename).suffix
    
    if ext == '.pdf':
        if not pdfsupport():
            sys.exit('Failed!!! PDF support is not enabled.')
        if pdftotext(filename):
            result = Path(filename).stem + '.txt'
    elif ext == '.hwp':
        if not hwpsupport():
            sys.exit('Failed!!! HWP support is not enabled.')
        if hwptotext(filename):
            result = Path(filename).stem + '.txt'
    elif ext in ['.docx', '.txt', '.yaml', '']:
        result = filename
    else:
        sys.exit(f'Failed!!! {ext} is not supported')

    return result
