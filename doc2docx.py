import glob
import re
import os
import win32com.client
import sys

for f in glob.glob('*.doc'):
    p = os.getcwd() + os.sep + f
    print(f'Converting {f} to docx...')
    word = win32com.client.Dispatch('Word.Application')
    doc = word.Documents.Open(p)

    doc.SaveAs(re.sub(r'\.\w+$', '.docx', os.path.abspath(p)), 16)
    doc.Close()
else:
    print('Done.')
    sys.exit(0)
