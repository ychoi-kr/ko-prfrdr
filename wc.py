from win32com.client import Dispatch
import os
import sys

from natsort import natsorted


def process(path='.'):
    #open Word
    word = Dispatch('Word.Application')
    word.Visible = False

    file_list = natsorted(os.listdir(path))

    cumm = 0
    for filename in file_list:
        filepath = path + '/' + filename
        if filename.endswith('.docx') or filename.endswith('.doc'):
            doc_path = os.path.abspath(filepath)
            doc = word.Documents.Open(doc_path)
            doc.Repaginate()
            num_of_sheets = doc.ComputeStatistics(2)
            cumm += num_of_sheets

            # print('{:30}\t{:5}\t{:5}'.format(filename, num_of_sheets, cumm))
            print('{}\t{:5}\t{:5}'.format(filename, num_of_sheets, cumm))

            doc.Close()

    word.Quit()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        process()
    else:
        process(sys.argv[1])