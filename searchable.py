import argparse
import os
import platform
import pathlib
import tempfile

from pdf2image import convert_from_path
import pytesseract
import numpy as np
from PyPDF2 import PdfFileMerger

custom_config = r'--oem 1 --psm 4 -c preserve_interword_spaces=1'


def main(filename, lang):
    
    if not pdfsupport():
        sys.exit('Failed!!! Cannot find pdfimages.exe.')
    
    stem = pathlib.Path(filename).stem
    bookname = f"searchable_{stem}"
    
    merger = PdfFileMerger()
    
    for pil_image in convert_from_path(filename, fmt='tif'):
        opencv_image = np.array(pil_image)[:, :, ::-1]  # https://stackoverflow.com/a/14140796/1558946
        
        result = pytesseract.image_to_pdf_or_hocr(
            opencv_image,
            lang=lang,
            config=custom_config
        )
        
        fp = tempfile.TemporaryFile()
        fp.write(bytearray(result))
        merger.append(fp)
    
    merger.write(f"searchable_{filename}")
    merger.close()


def pdfsupport():
    if platform.system() == 'Windows':
        # check if pdfimages.exe works
        if os.system('pdfimages -v > NUL') == 0:
            return True
        else:
            # not implemented
            return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-lang", default='kor+eng')
    parser.add_argument("PDF_file", nargs='?', help="filename", type=str)
    args = parser.parse_args()
    
    main(args.PDF_file, args.lang)

