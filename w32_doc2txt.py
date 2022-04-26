import glob
import re
import os
import sys

import win32com.client

from natsort import natsorted

newext = "txt"
wdFormatEncodedText = 7

for f in natsorted(glob.glob('*.doc')):
    p = os.getcwd() + os.sep + f
    print(f'Converting {f} to {newext}...')
    word = win32com.client.Dispatch('Word.Application')
    doc = word.Documents.Open(p)

    doc.SaveAs(re.sub(r'\.\w+$', '.' + newext, os.path.abspath(p)), wdFormatEncodedText)
    doc.Close()
else:
    print('Done.')
    sys.exit(0)
