import glob
import os


def latest_file(exts=[".txt", ".docx", ".pdf", ".hwp", '']):
    assert type(exts) is list
    files = []
    for ext in exts:
        files.extend(glob.glob('*' + ext))
    
    try:
        return max(files, key=os.path.getctime)
    except:
        sys.exit(f"Failed!!! Cannot find file in {'|'.join(exts)}.")