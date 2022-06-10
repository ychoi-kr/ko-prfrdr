import glob
import os
import re
from natsort import natsorted


def latest_file(exts=[".txt", ".docx", ".pdf", ".hwp", '']):
    assert type(exts) is list
    files = []
    for ext in exts:
        files.extend(glob.glob('*' + ext))
    
    try:
        return max(files, key=os.path.getctime)
    except:
        sys.exit(f"Failed!!! Cannot find file in {'|'.join(exts)}.")
        

def rename_numbered_files(startfile, insertmode, dry_run):
    msghead = "Dry-run: " if dry_run else ''
    m = re.match(r"(.*)(\d)([.-])(\d+)(.*)", startfile)
    pre, ch, dash, startfig, post = m.groups()

    delta = 1 if insertmode else -1

    for thisfile in natsorted(glob.glob('*.*'), reverse=insertmode):
        oldname = thisfile 

        filename, ext = os.path.splitext(thisfile)
        m = re.match(r"(.*)(\d)([.-])(\d+)(.*)", filename)
        pre, ch, dash, thisfig, post = m.groups()

        if startfile == thisfile and delta < 0:
            print(msghead + f"Removing {thisfile} ...")
            if not dry_run:
                os.remove(thisfile)

        elif (startfile == thisfile and delta > 0) or (int(startfig) < int(thisfig)):
            newfig = int(thisfig) + delta
            newname = f'{pre}{ch}{dash}{newfig}{post}{ext}'
            print(msghead + f'Renaming {oldname} to {newname} ...')
            if not dry_run:
                os.rename(oldname, newname)

        else:
            print(msghead + f'{thisfile} will not be changed.')

    print('Done.')
