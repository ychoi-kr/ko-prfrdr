import glob
import os
from pdf2docx import Converter


pdf_file = max(glob.glob('*.pdf'), key=os.path.getctime)
docx_file = pdf_file + '.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()