import glob
import os
from pdf2docx import Converter


if __name__ == '__main__':
    pdf_file = max(glob.glob('*.pdf'), key=os.path.getctime)
    docx_file = pdf_file + '.docx'

    cv = Converter(pdf_file)
    cv.convert(docx_file)
    #cv.convert(docx_file, multi_processing=True, cpu_count=4)
    cv.close()