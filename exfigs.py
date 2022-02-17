#!/usr/bin/python3

import os
import pathlib
import sys
import zipfile


def extract_figs(path):
    if os.path.isfile(path) and path.endswith('.docx'):
        z = zipfile.ZipFile(path, 'r')
        for name in z.namelist():
            if name.startswith('word/media/') and name.split('.')[-1] in ['jpg', 'png']:
                print(f"extracting {name} ...")
                p = pathlib.Path(path).parents[0] / pathlib.Path(name).name
                p.write_bytes(z.read(name))
        z.close()


if __name__ == '__main__':
    arg1 = sys.argv[1]
    if not os.path.isfile(arg1) or not arg1.endswith('.docx'):
        sys.exit(1)
    else:
        extract_figs(arg1)
