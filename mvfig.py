import csv
import shutil
import os

with open('fig_list.tsv', 'r') as f:
    for line in csv.reader(f, delimiter='\t'):
        old, new = line[0], line[1]
        for ext in ['png', 'jpg']:
            filea = f'{old}.{ext}'
            fileb = f'{new}.{ext}'
            if os.path.isfile(filea):
                shutil.move(filea, fileb)
                break
